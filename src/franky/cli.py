# Copyright (c) 2025 - Gilles Coissac
# This file is part of franky library.
#
# franky is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# franky is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with franky. If not, see <https://www.gnu.org/licenses/>
#
# ruff: noqa: D101, D102, D103, ARG002
"""Franky cli."""

from __future__ import annotations

import json
import pkgutil
import sys
from datetime import datetime
from enum import StrEnum
from importlib import import_module
from importlib.resources import files
from os import environ
from pathlib import Path
from typing import TYPE_CHECKING, Final, Literal, NamedTuple, Never, cast

from deluxe import mureq
from deluxe.availability import hints
from deluxe.console.cli import Cli, CliError

from franky import Theme, _version


if TYPE_CHECKING:
    import argparse
    from argparse import Namespace

    from deluxe.console.argparser import PrettyParser

import pretty_errors


pretty_errors.configure(  # pyright: ignore[reportUnknownMemberType]
    separator_character="*",
    filename_display=pretty_errors.FILENAME_COMPACT,
    line_number_first=True,
    display_link=False,
    lines_before=5,
    lines_after=2,
    line_color=f"{pretty_errors.RED}> {pretty_errors.default_config.line_color}",
    code_color=f"  {pretty_errors.default_config.line_color}",
    truncate_code=True,
    display_locals=True,
    trace_lines_before=True,
    display_trace_locals=True,
)


PROG_NAME: Final[str] = "franky"
HOME: Final[Path] = Path.home()
CONFIG_DIR: Path = Path(environ.get("XDG_CONFIG_HOME", HOME / ".config")) / PROG_NAME
STATE_DIR: Path = Path(environ.get("XDG_STATE_HOME", HOME / ".local" / "state")) / PROG_NAME
DATA_DIR: Path = Path(environ.get("XDG_DATA_HOME", HOME / ".local" / "share")) / PROG_NAME
PLATFORM: Literal["posix", "darwin", "windows"] = (
    "darwin" if "darwin" in hints() else "windows" if "windows" in hints() else "posix"
)


class ThemeError(Exception): ...


CliError.register(
    OSError,
    ThemeError,
    mureq.HTTPErrorStatus,
)


class Franky(Cli):
    """Franky command line interface."""

    def __init__(self) -> None:
        super().__init__(
            prog=PROG_NAME,
            version=_version.__version__,
            prefix=True,
            shell_completion=False,
        )

    def configure(self, parser: PrettyParser) -> None:
        install = self.add_command(
            self.install,
            "install a franky theme",
        )
        install.add_argument(
            "themes",
            help="which theme(s) to install (set 'all' to install all themes)",
            nargs="+",
            default=[],
            choices=["all", *list_theme_modules()],
        )
        install.add_argument(
            "-y",
            "--yes",
            help="do not ask for confirmation",
            action="store_true",
        )
        self.add_command(
            self.list_themes,
            help="list available themes",
            name="list",
        )

    def main(self, namespace: Namespace) -> None:
        if not hasattr(namespace, "callback"):
            self.parser.print_help()

    def cleanup(self, namespace: Namespace) -> None:  # noqa: PLR6301
        return

    def install(self, opts: argparse.Namespace) -> None:  # noqa: PLR6301
        for theme in opts.themes:
            install_theme(theme, not opts.yes)

    def list_themes(self, _opts: argparse.Namespace) -> None:  # noqa: PLR6301
        sys.stdout.write("\n".join(list_theme_modules()) + "\n")


def install_theme(name: str, ask: bool) -> None:
    try:  # noqa: PLW0717
        mod = import_module(f"franky.themes.{name}")
        theme: Theme = mod.main()
        if not (place := theme["place"][PLATFORM]):
            msg = f"{name} theme is not installable on {PLATFORM} platform."
            raise ThemeError(msg)
        write_theme(name, place, theme["file"], theme["content"], ask)
    except (AttributeError, KeyError, LookupError) as err:
        msg = "malformed theme."
        raise ThemeError(msg) from err


def write_theme(name: str, path: Path, file: str, content: str, ask: bool) -> None:
    install_path = Path(path, file)
    sys.stderr.write(f"the {name} theme will be installed here:\n")
    sys.stderr.write(f"  {install_path}\n")

    if ask and (_ := input("accept? [Y/n]: ")) and _ in "nN":
        return

    if install_path.exists():
        if (
            ask
            and (_ := input(f"a <{file}> file already exists, replace it? [Y/n]: "))
            and _ in "nN"
        ):
            return
        # TODO: add option to backup the file
        install_path.unlink()

    if not path.is_dir():
        path.mkdir(parents=True)

    install_path.write_text(content, encoding="UTF-8")
    sys.stderr.write(f"theme for {name} is now installed\n")


def list_theme_modules() -> list[str]:
    """Return a list of module names available in the franky.themes package."""
    # NOTE: should we filter modules for user PLATFORM?
    themes_dir = files("franky.themes")
    themes = list({name for _, name, _ in pkgutil.iter_modules([str(themes_dir)])})
    themes.sort()
    return themes


def list_themes_remotely():
    timestamp: str = datetime.now().strftime("%y_%m_%d")  # noqa: DTZ005
    cache = STATE_DIR / f"themes@{timestamp}"
    if cache.exists():
        with cache.open("r") as file:
            themes = json.loads(file.read())
    else:
        themes = list_github_directory(
            "gravures",
            "franky",
            "themes",
        )
    return themes


class GithubContentType(StrEnum):
    FILE = "file"
    DIR = "dir"
    LINK = "symlink"
    SUBMODULE = "submodule"


class GitHubContent(NamedTuple):
    """Single item returned by github."""

    type: GithubContentType
    name: str
    path: str
    sha: str


def list_github_directory(
    owner: str,
    repo: str,
    directory: str = "",
    *,
    token: str | None = None,
) -> list[GitHubContent]:
    """Returns the contents of a GitHub repository directory.

    Raises:
        OSError: if fetching content failed for any raison.
    """
    github_api: Final[str] = "https://api.github.com"
    accept_header: Final[str] = "application/vnd.github+json"
    endpoint: str = f"{github_api}/repos/{owner}/{repo}/contents/{directory}"
    headers: dict[str, str] = {"Accept": accept_header, "X-GitHub-Api-Version": "2022-11-28"}

    if token is not None:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = mureq.get(endpoint, headers=headers, timeout=3)
        response.raise_for_status()
        tmp = cast("list[dict[str, str]] | dict[str, str]", response.json())
    except (OSError, mureq.HTTPErrorStatus) as err:
        raise OSError from err

    payload: list[dict[str, str]] = [tmp] if isinstance(tmp, dict) else tmp
    return [
        GitHubContent(
            type=GithubContentType(e["type"]),
            name=e["name"],
            path=e["path"],
            sha=e["sha"],
        )
        for e in payload
    ]


def main() -> Never:
    cli = Franky()
    sys.exit(cli())
