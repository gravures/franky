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
"""Ghostty Franky theme."""

from __future__ import annotations

from pathlib import Path

from franky import UI, Ansi, Swatch, Theme
from franky.theme import Place


def main() -> Theme:
    return {
        "content": f"""
palette = 0={Ansi.black}
palette = 1={Ansi.red}
palette = 2={Ansi.green}
palette = 3={Ansi.yellow}
palette = 4={Ansi.blue}
palette = 5={Ansi.magenta}
palette = 6={Ansi.cyan}
palette = 7={Ansi.white}

palette = 8={Ansi.bright_black}
palette = 9={Ansi.bright_red}
palette = 10={Ansi.bright_green}
palette = 11={Ansi.bright_yellow}
palette = 12={Ansi.bright_blue}
palette = 13={Ansi.bright_magenta}
palette = 14={Ansi.bright_cyan}
palette = 15={Ansi.bright_white}

background = {Swatch.mantle}
foreground = {Swatch.text}

cursor-text = {UI.cursor.fg}
cursor-color = {UI.cursor.bg}

selection-background = {UI.selection.bg}
selection-foreground = {UI.selection.fg}
""",
        "place": Place(
            posix=Path.home() / ".config" / "ghostty" / "themes",
            darwin=Path.home() / ".config" / "ghostty" / "themes",
            windows=None,
        ),
        "file": "franky",
    }
