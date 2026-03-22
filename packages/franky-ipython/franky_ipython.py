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
# ruff: noqa: D101, D102, D103
"""IPython extension for Franky theme support."""

from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING

from franky import UI, Generic, Lang, Meta, Swatch
from IPython.terminal.prompts import Prompts
from IPython.utils.PyColorize import (
    Theme,
    theme_table,
)
from prompt_toolkit.formatted_text import OneStyleAndTextTuple, fragment_list_width  # noqa: F401
from pygments.token import Token, _TokenType  # pyright: ignore[reportPrivateUsage]


if TYPE_CHECKING:
    from IPython.core.interactiveshell import InteractiveShell


saved_theme: str = "linux"


def load_ipython_extension(ipython: InteractiveShell) -> None:
    global saved_theme  # noqa: PLW0603
    theme_table["franky"] = Theme("franky", None, FRANKY_PYGMENTS, symbols=SYMBOLS)
    saved_theme = ipython.colors
    ipython.colors = "franky"
    # ipython.prompts = IPsterPrompts(ipython)  # _pyright: ignore[reportAttributeAccessIssue]


def unload_ipython_extension(ipython: InteractiveShell) -> None:
    del theme_table["franky"]
    ipython.colors = saved_theme


FRANKY_PYGMENTS: dict[object, str] = {
    # LANG
    Token.Comment: Lang.comment.pygments(),
    Token.Number: Lang.number.pygments(),
    Token.String: Lang.string.pygments(),
    Token.String.Escape: Lang.escape.pygments(),
    Token.Keyword: Lang.keyword.pygments(),
    Token.Operator: Lang.operator.pygments(),
    Token.Name.Variable: Lang.variable.pygments(),
    Token.Name.Constant: Lang.constant.pygments(),
    Token.Name.Builtin: Lang.builtin.pygments(),
    Token.Name.Namespace: Lang.namespace.pygments(),
    Token.Name.Class: Lang.type.pygments(),
    Token.Name.Function: Lang.function.pygments(),
    Token.Name.Decorator: Lang.decorator.pygments(),
    Token.Name.Variable.Magic: Lang.magic.pygments(),
    Token.Name.Exception: Lang.exception.pygments(),
    # META
    Token.Whitespace: Meta.whitespace.pygments(),
    Token.Caret: Meta.caret.pygments(),
    Token.Filename: Meta.filename.pygments(),
    Token.FilenameEm: Meta.filename_emphasis.pygments(),
    # GENERIC
    Token.Generic.Deleted: Generic.deleted.pygments(),
    Token.Generic.Emph: Generic.emphasis.pygments(),
    Token.Generic.Strong: Generic.strong.pygments(),
    Token.Generic.EmphStrong: Generic.emphasis_strong.pygments(),
    # UI
    Token.Normal: "",
    Token.NormalEm: Generic.emphasis.pygments(),
    Token.ExcName: UI.exc_name.pygments(),
    Token.Topline: UI.topline.pygments(),
    Token.Line: UI.cursor_line.pygments(),
    Token.Lineno: UI.line_number.pygments(),
    Token.LinenoEm: UI.line_number_select.pygments(),
    Token.Breakpoint: "",
    Token.Breakpoint.Disabled: UI.breakpoint.pygments(),
    Token.Breakpoint.Enabled: UI.breakpoint_active.pygments(),
    # Token.ValEm: C2,
    # Token.VName: C2,
    # Token.TB.Name: C6,
    # Token.TB.NameEm: C7,
    # Token.Header: C3,
    #
    # PROMPT
    Token.Prompt: Swatch.sapphire.value,
    Token.PromptNum: Swatch.green.value,
    Token.Prompt.Continuation: UI.line_number.pygments(),
    # Token.Prompt.Continuation.L1: Swatch.flamingo.value,
    Token.OutPrompt: Swatch.pink.value,
    Token.OutPromptNum: Swatch.peach.value,
    # Token.Header: "ansibrightred",
    # Token.ValEm: "ansibrightblue",
    # Token.VName: "ansicyan",
    # Token.TB.Name: "ansimagenta",
    # Token.TB.NameEm: "ansibrightmagenta",
}

SYMBOLS: dict[str, str] = {
    "arrow_body": "\u2500",
    "arrow_head": "\u25b6",
    "top_line": "\u2500",
}


LinePrompt = list[tuple[_TokenType, str]]


class IPsterPrompts(Prompts):
    def __init__(self, shell: InteractiveShell) -> None:
        self.shell: InteractiveShell = shell

        virtual_env = os.path.basename(os.path.normpath(sys.prefix))  # noqa: PTH119
        self.prompt_virtualenv: LinePrompt = [
            (Token.IPsterPromptVirtualenv, " \ue73c " + virtual_env + " "),
            (Token.IPsterPowerlinePromptVirtualenv, "\ue0b0"),
            (Token.Prompt, " "),
        ]

    @staticmethod
    def is_venv() -> bool:
        """Returns true if running inside a virtual environment."""
        return hasattr(sys, "real_prefix") or (
            hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
        )

    def add_segment(self, line: LinePrompt) -> LinePrompt:
        """Add Virtual Environments segment if activated."""  # noqa: DOC201
        if self.is_venv():
            return self.prompt_virtualenv + line
        return [(Token.Prompt, " "), *line]

    def in_prompt_tokens(self) -> LinePrompt:
        prompt_in: LinePrompt = [
            (Token.Prompt, "In ["),
            (Token.PromptNum, str(self.shell.execution_count)),
            (Token.Prompt, "] "),
            (Token.IPsterPowerlinePrompt, "\ue0b0"),
            (Token.IPsterPromptSpace, " "),
        ]
        return self.add_segment(prompt_in)

    def _width(self) -> int:
        return fragment_list_width(self.in_prompt_tokens())  # pyright: ignore[reportArgumentType]

    def continuation_prompt_tokens(
        self,
        width: int | None = None,
        *,
        lineno: int | None = None,  # noqa: ARG002
        wrap_count: int | None = None,  # noqa: ARG002
    ) -> LinePrompt:
        if width is None:
            width = self._width()
        return [(Token.Prompt, (" " * (width - 2))), (Token.IPsterPowerlinePrompt, "\ue0b0")]

    def out_prompt_tokens(self) -> LinePrompt:
        prompt_out = [
            (Token.OutPrompt, "Out["),
            (Token.OutPromptNum, str(self.shell.execution_count)),
            (Token.OutPrompt, "] "),
            (Token.IPsterPowerlinePrompt, "\ue0b0"),
            (Token.IPsterPromptSpace, " "),
        ]
        return self.add_segment(prompt_out)
