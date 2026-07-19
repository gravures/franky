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
from typing import TYPE_CHECKING, Literal, NotRequired, TypedDict

from franky._plaftorm import PLATFORM


if TYPE_CHECKING:
    from pathlib import Path


@dataclass
class Place:
    """Emplacement where Theme should be installed."""

    posix: Path | None
    darwin: Path | None
    windows: Path | None

    def current(self) -> Path | None:
        """Returns theme install Path.

        Returns: a Path if theme is available on this platform, otherwise None.
        """
        return getattr(self, PLATFORM)


class File(TypedDict):
    """Interface for additional files."""

    path: Path
    content: str


class Theme(TypedDict):
    """Interface for franky theme implementations."""

    content: str
    place: Place
    file: str
    files: NotRequired[list[File]]
    doc: NotRequired[str]


class Swatch(StrEnum):
    """Franky colour swatch."""

    # Foreground and Background
    text = "#c9c9c9"
    base = "#151524"  # "#1e1e2e"

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

    mantle = "#110E17"
    crust = "#0B090F"

    uv2 = "#521f9c"
    uv1 = "#340c6f"
    uv0 = "#09070D"


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
    """Style's modifier."""

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
class Underline:
    """Underline style."""

    color: Swatch | None = None
    style: Literal["line", "curl", "dashed", "dotted", "double_line"] = "line"


@dataclass
class Style:
    """Style datatype."""

    fg: Swatch | None = None
    bg: Swatch | None = None
    mods: tuple[Mod, ...] = ()
    underline: Underline | None = None

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

    attribute = Swatch.text
    builtin = Swatch.lang_blue
    comment = (Swatch.surface2, None, (Mod.italic,))
    constant = Swatch.lang_blue
    constructor = Swatch.lang_purple
    control = Swatch.lang_red
    control_conditional = Swatch.lang_red
    control_repeat = Swatch.lang_red
    control_import = Swatch.lang_red
    control_return = Swatch.lang_red
    control_exception = Swatch.lang_red
    decorator = Swatch.lang_purple
    directive = Swatch.lang_pink
    escape = Swatch.lang_pink
    exception = (Swatch.subtext0, None, (Mod.italic,))
    function = Swatch.lang_purple
    function_method = Swatch.lang_purple
    function_method_private = Swatch.lang_purple
    function_special = Swatch.lang_purple
    keyword = Swatch.lang_red
    keyword_operator = Swatch.lang_red
    keyword_function = Swatch.lang_red
    keyword_storage = Swatch.lang_red
    keyword_storage_type = Swatch.lang_red
    keyword_storage_modifier = Swatch.lang_red
    label = Swatch.lang_yellow
    magic = Swatch.lang_blue
    macro = Swatch.lang_purple
    namespace = Swatch.text
    number = Swatch.lang_pink
    operator = Swatch.lang_red
    punctuation = Swatch.overlay0
    punctuation_bracket = Swatch.overlay0
    punctuation_delimiter = Swatch.overlay0
    punctuation_special = Swatch.overlay0
    string = Swatch.lang_blue
    special = Swatch.lang_yellow
    tag = Swatch.lang_yellow
    type = (Swatch.subtext0, None, (Mod.italic,))
    type_builtin = Swatch.lang_blue
    type_enum_member = Swatch.lang_blue
    variable = Swatch.text
    variable_builtin = Swatch.lang_blue
    variable_parameter = (Swatch.subtext0, None, (Mod.italic,))
    variable_other = Swatch.text
    variable_other_member = Swatch.text
    variable_other_member_private = Swatch.text


class Meta(Style, Enum):
    """Style names for special forms."""

    whitespace = (Swatch.base, Swatch.text, (Mod.underlined,), Underline(style="line"))
    caret = Swatch.rosewater
    filename = Swatch.lang_blue
    filename_emphasis = (Swatch.lang_blue, None, (Mod.bold,))


class Generic(Style, Enum):
    """Style names for generic modifiers."""

    deleted = (Swatch.subtext0, None, (Mod.crossed_out,))
    emphasis = (None, None, (Mod.italic,))
    strong = (None, None, (Mod.bold,))
    emphasis_strong = (None, None, (Mod.bold, Mod.italic))


class UI(Style, Enum):
    """Style names for ui elements."""

    background = Swatch.subtext1, Swatch.base
    background_separator = Swatch.subtext1, Swatch.base
    tui_background = Swatch.subtext1, Swatch.mantle

    cursor = Swatch.base, Swatch.overlay2
    cursor_insert = Swatch.base, Swatch.overlay2
    cursor_select = Swatch.base, Swatch.overlay2
    cursor_match = Swatch.yellow, Swatch.base
    cursor_primary = Swatch.base, Swatch.overlay2
    cursor_primary_insert = Swatch.base, Swatch.text
    cursor_primary_select = Swatch.base, Swatch.text

    cursor_line = (Swatch.base, Swatch.surface0)

    selection = Swatch.maroon, Swatch.uv0
    selection_primary = Swatch.maroon, Swatch.uv0

    ruler = None, Swatch.mantle
    indent_guide = Swatch.surface1
    inlay_hint = Swatch.surface2, None, (Mod.italic,)
    wrap = Swatch.surface2
    jump_label = Swatch.lang_yellow, Swatch.uv2

    exc_name = Swatch.lang_purple
    topline = Swatch.lang_purple
    line_number = Swatch.surface1
    line_number_select = Swatch.overlay2
    breakpoint = Swatch.text
    breakpoint_active = Swatch.sky

    hint = Swatch.blue, Swatch.base
    info = Swatch.sky, Swatch.base
    warning = Swatch.maroon, Swatch.base
    error = Swatch.red, Swatch.base

    diagnostic_hint = None, None, (Mod.underlined,), Underline(Swatch.base, "dotted")
    diagnostic_info = None, None, (Mod.underlined,), Underline(Swatch.base, "dotted")
    diagnostic_warning = None, None, (Mod.underlined,), Underline(Swatch.base, "dotted")
    diagnostic_error = None, None, (Mod.underlined,), Underline(Swatch.red, "dotted")
    diagnostic_unnecessary = None, None, (Mod.dim,)

    diff_plus = Swatch.green
    diff_minus = Swatch.red
    diff_delta = Swatch.yellow
    diff_delta_moved = Swatch.sky

    gutter = None, Swatch.base
    gutter_selected = None, Swatch.uv1

    status_line = Swatch.overlay2, Swatch.mantle
    status_line_inactive = Swatch.surface2, Swatch.mantle
    status_line_normal = Swatch.uv0, Swatch.teal, (Mod.bold,)
    status_line_insert = Swatch.uv0, Swatch.yellow, (Mod.bold,)
    status_line_select = Swatch.uv0, Swatch.mauve, (Mod.bold,)

    buffer_line = Swatch.overlay0
    buffer_line_active = Swatch.mauve
    buffer_line_background = Swatch.subtext0, Swatch.uv0

    scrollbar_track = Swatch.uv0, Swatch.uv0
    scrollbar_knob = Swatch.lang_purple, Swatch.uv0

    popup = Swatch.subtext0, Swatch.surface1
    popup_boder = Swatch.mauve
    popup_info = Swatch.mauve


class Markup(Style, Enum):
    """Style names for Markup language."""

    markup = Swatch.subtext1
    heading_marker = Swatch.uv2, Swatch.uv2
    heading_1 = Swatch.pink, Swatch.uv1, (Mod.bold,)
    heading_2 = None, Swatch.uv2, (Mod.bold,)
    heading_3 = Swatch.subtext0, Swatch.uv1, (Mod.bold,)
    heading_4 = Swatch.subtext1, Swatch.uv1
    heading_5 = Swatch.subtext1, Swatch.uv1
    heading_6 = Swatch.subtext1, Swatch.uv1

    list_unnumbered = Swatch.flamingo, None, (Mod.bold,)
    list_numbered = Swatch.flamingo, None, (Mod.bold,)
    list_unchecked = Swatch.surface2
    list_checked = Swatch.green

    bold = None, None, (Mod.bold,)
    italic = None, None, (Mod.italic,)
    strike_through = None, None, (Mod.crossed_out,)

    link_url = Swatch.base, Swatch.surface2, (Mod.reversed,)
    link_label = Swatch.teal, None, (Mod.bold,)
    link_text = Swatch.sky, None, (Mod.underlined,), Underline(style="line")

    quote = None, Swatch.surface0, (Mod.italic,)

    raw = Swatch.lang_yellow
    raw_inline = Swatch.lang_yellow, Swatch.surface1
    raw_block = Swatch.text, Swatch.uv0


def Trans(color: str) -> str:  # noqa: N802
    """Returns franky Hex color from Catppuccin one."""
    map_: dict[str, str] = {
        "#f5e0dc": Swatch.rosewater,
        "#f2cdcd": Swatch.flamingo,
        "#f5c2e7": Swatch.pink,
        "#cba6f7": Swatch.mauve,
        "#f38ba8": Swatch.red,
        "#eba0ac": Swatch.maroon,
        "#fab387": Swatch.peach,
        "#f9e2af": Swatch.yellow,
        "#a6e3a1": Swatch.green,
        "#94e2d5": Swatch.teal,
        "#89dceb": Swatch.sky,
        "#74c7ec": Swatch.sapphire,
        "#89b4fa": Swatch.blue,
        "#b4befe": Swatch.lavender,
        "#cdd6f4": Swatch.text,
        "#bac2de": Swatch.subtext1,
        "#a6adc8": Swatch.subtext0,
        "#9399b2": Swatch.overlay2,
        "#7f849c": Swatch.overlay1,
        "#6c7086": Swatch.overlay0,
        "#585b70": Swatch.surface2,
        "#45475a": Swatch.surface1,
        "#313244": Swatch.surface0,
        "#1e1e2e": Swatch.base,
        "#181825": Swatch.mantle,
        "#11111b": Swatch.crust,
    }
    return map_[color]
