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
# ruff: noqa: D103
"""Delta Franky theme."""

from __future__ import annotations

import os
from pathlib import Path

from franky import UI, Mod, Style, Swatch, Theme
from franky.theme import Place


def format(style: Style) -> str:  # noqa: A001
    bold = "true" if Mod.bold in style.mods else "false"
    formatted = (
        f"{style.fg}" if style.fg else f"{Swatch.text}",
        f"{style.bg}" if style.bg else f"{Swatch.mantle}",
        bold,
    )
    return "   ".join(formatted)


PLACE = Place(
    posix=Path.home() / ".config" / "delta" / "themes",
    darwin=Path.home() / ".config" / "delta" / "themes",
    windows=Path(os.getenv("APPDATA", Path.home() / "AppData" / "Roaming")) / "delta" / "themes",
)


def main() -> Theme:
    return {
        "content": f"""
[delta "franky"]
blame-palette = "#1e1e2e #181825 {Swatch.mantle} {Swatch.surface1} {Swatch.surface2}"
commit-decoration-style = "{Swatch.overlay0}" bold box ul
dark = true
file-decoration-style = "{Swatch.overlay0}"
file-style = "{Swatch.subtext1}"
hunk-header-decoration-style = "{Swatch.overlay0}" box ul
hunk-header-file-style = bold
hunk-header-line-number-style = bold "{Swatch.subtext0}"
hunk-header-style = file line-number syntax
line-numbers-left-style = "{UI.line_number.fg}"
line-numbers-minus-style = bold "{UI.diff_minus.fg}"
line-numbers-plus-style = bold "{UI.diff_plus.fg}"
line-numbers-right-style = "{UI.line_number.fg}"
line-numbers-zero-style = "{UI.line_number.fg}"
# 35% red 65% base
minus-emph-style = bold syntax "#694559"
# 20% red 80% base
minus-style = syntax "#493447"
# 35% green 65% base
plus-emph-style = bold syntax "#4e6356"
# 20% green 80% base
plus-style = syntax "#394545"
map-styles = \
	bold purple => syntax "#5b4e74", \
	bold blue => syntax "#445375", \
	bold cyan => syntax "#446170", \
	bold yellow => syntax "#6b635b"
# Should match the name of the bat theme
syntax-theme = franky
""",
        "place": PLACE,
        "file": "franky.gitconfig",
        "doc": f"""
Delta uses git config (~/.gitconfig) for its configuration,
now you could include the theme by adding these lines to your gitconfig file:

[include]
	path = {PLACE.current()!s}
[delta]
	features = franky
""",
    }
