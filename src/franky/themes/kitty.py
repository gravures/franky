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
"""Kitty Franky theme."""

from __future__ import annotations

from pathlib import Path

from franky import UI, Ansi, Markup, Swatch, Theme
from franky.theme import Place


def main() -> Theme:
    return {
        "content": f"""
# The basic colors
background {Swatch.mantle}
foreground {Swatch.text}
selection_background {UI.selection.bg}
selection_foreground {UI.selection.fg}

# The 16 terminal colors
color0 {Ansi.black}
color1 {Ansi.red}
color2 {Ansi.green}
color3 {Ansi.yellow}
color4 {Ansi.blue}
color5 {Ansi.magenta}
color6 {Ansi.cyan}
color7 {Ansi.white}
color8 {Ansi.bright_black}
color9 {Ansi.bright_red}
color10 {Ansi.bright_green}
color11 {Ansi.bright_yellow}
color12 {Ansi.bright_blue}
color13 {Ansi.bright_magenta}
color14 {Ansi.bright_cyan}
color15 {Ansi.bright_white}

# Cursor colors
cursor {UI.cursor.bg}
cursor_text_color {UI.cursor.fg}

# Scrollbar colors
scrollbar_handle_color  {UI.scrollbar_knob.fg}
scrollbar_track_color   {UI.scrollbar_track.fg}

# URL color when hovering with mouse
url_color               {Markup.link_text.fg}

# Kitty window border colors
active_border_color     {Swatch.subtext1}
inactive_border_color   {Swatch.surface2}
bell_border_color       {Swatch.yellow}

# OS Window titlebar colors
wayland_titlebar_color system
macos_titlebar_color system

# Tab bar colors
active_tab_foreground   {Swatch.crust}
active_tab_background   {Swatch.mauve}
inactive_tab_foreground {Swatch.subtext0}
inactive_tab_background {Swatch.mantle}
tab_bar_background      {Swatch.crust}

# Colors for marks (marked text in the terminal)
mark1_foreground {Swatch.mantle}
mark1_background {Swatch.subtext1}
mark2_foreground {Swatch.mantle}
mark2_background {Swatch.flamingo}
mark3_foreground {Swatch.mantle}
mark3_background {Swatch.sapphire}
""",
        "place": Place(
            posix=Path.home() / ".config" / "kitty" / "themes",
            darwin=Path.home() / ".config" / "kitty" / "themes",
            windows=None,
        ),
        "file": "franky.conf",
        "doc": """
to activate this theme you could run kitten and select <franky> from the list:
kitty +kitten themes --reload-in=all
""",
    }
