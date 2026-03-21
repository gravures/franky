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
# ruff: noqa: PIE796
"""Franky theme palette."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, StrEnum
from typing import TYPE_CHECKING, TypedDict


if TYPE_CHECKING:
    from pathlib import Path


class Place(TypedDict):
    """Emplacement where Theme should be installed."""

    posix: Path | None
    darwin: Path | None
    windows: Path | None


class Theme(TypedDict):
    """Interface for franky theme implementations."""

    content: str
    place: Place
    file: str


class Swatch(StrEnum):
    """Franky colour swatch enumeration."""

    # Foreground and Background
    text = "#c9c9c9"
    base = "#1e1e2e"

    rosewater = "#f5e0dc"
    flamingo = "#f2cdcd"
    pink = "#fc8dc7"
    mauve = "#cba6f7"
    red = "#bb3831"
    maroon = "#ba8d45"
    peach = "#fab387"
    yellow = "#ffdeaa"
    green = "#57ab5a"
    teal = "#94e2d5"
    sky = "#539bf5"
    sapphire = "#74c7ec"
    blue = "#2764b1"
    lavender = "#b4befe"

    # Lang
    lang_blue = "#749fd4"
    lang_green = "#569352"
    lang_yellow = "#daaa3f"
    lang_pink = "#ff938a"
    lang_red = "#d85651"
    lang_purple = "#977ebc"
    subtext1 = "#b1b1b1"
    subtext0 = "#a6a596"
    overlay2 = "#909dab"
    overlay1 = "#7f849c"
    overlay0 = "#6f6b58"

    # UI
    surface2 = "#54595f"
    surface1 = "#373e47"
    surface0 = "#2a2a3c"
    mantle = "#181825"
    crust = "#141817"
    uv2 = "#521f9c"
    uv1 = "#340c6f"
    uv0 = "#16101f"

    # None
    none = ""


class Ansi(StrEnum):
    """Ansi 16 basic colour names."""

    black = Swatch.surface1
    red = Swatch.red
    green = Swatch.green
    yellow = Swatch.maroon
    blue = Swatch.blue
    magenta = Swatch.pink
    cyan = Swatch.teal
    white = Swatch.subtext0

    bright_black = Swatch.surface2
    bright_red = Swatch.pink
    bright_green = Swatch.teal
    bright_yellow = Swatch.yellow
    bright_blue = Swatch.sky
    bright_magenta = Swatch.flamingo
    bright_cyan = Swatch.sapphire
    bright_white = Swatch.subtext1


class Mod(StrEnum):
    """Style's modifier enumeration."""

    normal = ""
    bold = "bold"
    bright = bold
    dim = "dim"
    italic = "italic"
    slow_blink = "slow_blink"
    rapid_blink = "rapid_blink"
    reversed = "reversed"
    inverted = reversed  # noqa: A003
    hidden = "hidden"
    invisible = hidden
    crossed_out = "crossed_out"
    strike_through = crossed_out
    underlined = "underline"


@dataclass
class Style:
    """Style datatype."""

    fg: Swatch = Swatch.none
    bg: Swatch = Swatch.none
    mods: tuple[Mod, ...] = ()

    def _join_mods(self) -> str:
        return f"{' '.join(self.mods)}" if self.mods else ""

    def _join_mods_pygments(self) -> str:
        def to_pygments(mod: Mod) -> str:
            if mod in {Mod.bold, Mod.italic, Mod.underlined}:
                return mod.value
            return ""

        mods = map(
            to_pygments,
            self.mods,
        )
        return f"{' '.join(mods)}" if self.mods else ""

    def pygments(self) -> str:
        """Return pygments formatted string."""
        return (
            f"{f'{self.fg} ' if self.fg else ''}"
            f"{f'bg:{self.bg} ' if self.bg else ''}"
            f"{self._join_mods_pygments()}"
        ).rstrip()


class Lang(Style, Enum):
    """Style names for code highlighting."""

    comment = (Swatch.lang_green, Swatch.none, (Mod.italic,))
    number = Swatch.lang_pink
    string = Swatch.lang_blue
    escape = Swatch.lang_pink
    keyword = Swatch.lang_red
    builtin = Swatch.lang_blue
    variable = Swatch.text
    constant = Swatch.lang_blue
    type = (Swatch.subtext0, Swatch.none, (Mod.italic,))
    constructor = Swatch.lang_purple
    function = Swatch.lang_purple
    decorator = Swatch.lang_purple
    macro = Swatch.lang_purple
    label = Swatch.lang_yellow
    namespace = Swatch.text
    operator = Swatch.lang_red
    magic = Swatch.lang_blue
    exception = (Swatch.subtext0, Swatch.none, (Mod.italic,))


class Meta(Style, Enum):
    """Style names for special forms."""

    whitespace = (Swatch.base, Swatch.text, (Mod.underlined,))
    caret = ()
    filename = Swatch.lang_blue
    filename_emphasis = (Swatch.lang_blue, Swatch.none, (Mod.bold,))


class Generic(Style, Enum):
    """Style names for generic modifiers."""

    deleted = (Swatch.subtext0, Swatch.none, (Mod.crossed_out,))
    emphasis = (Swatch.none, Swatch.none, (Mod.italic,))
    strong = (Swatch.none, Swatch.none, (Mod.bold,))
    emphasis_strong = (Swatch.none, Swatch.none, (Mod.bold, Mod.italic))


class UI(Style, Enum):
    """Style names for ui elements."""

    cursor = Swatch.base, Swatch.rosewater
    selection = Swatch.text, Swatch.blue
    exc_name = Swatch.lang_purple
    topline = Swatch.lang_purple
    linenr = Swatch.surface2
    linenr_select = Swatch.overlay2
    cursor_line = (Swatch.base, Swatch.surface0)
    breakpoint = Swatch.text
    breakpoint_active = Swatch.sky
