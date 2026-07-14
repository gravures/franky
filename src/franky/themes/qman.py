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
"""Qman Franky theme."""

from __future__ import annotations

from pathlib import Path

from franky import UI, Mod, Style, Swatch, Theme


def format(style: Style) -> str:  # noqa: A001
    bold = "true" if Mod.bold in style.mods else "false"
    formatted = (
        f"{style.fg}" if style.fg else f"{Swatch.text}",
        f"{style.bg}" if style.bg else f"{Swatch.mantle}",
        bold,
    )
    return "   ".join(formatted)


def main() -> Theme:
    return {
        "content": f"""; frany.conf
; Qman theme
; description: franky: a dark theme for Qman
; tags:        rgb, unicode, dark
; TERM:        xterm-kitty
; based on:    https://github.com/gravures/franky/blob/main/src/franky/themes/qman.py
; author:      gilles coissac

[chars]
sbar_top=           ┳
sbar_vline=         ┃
sbar_bottom=        ┻
sbar_block=         █
trans_mode_name=    ┇
trans_name_loc=     ┇
box_hline=          ─
box_vline=          │
box_tl=             ╭
box_tr=             ╮
box_bl=             ╰
box_br=             ╯
arrow_up=           ⇡
arrow_down=         ⇣
arrow_lr=           ⇄

[colours]
;                   fg        bg        bold
text=               {format(UI.tui_background)}
search=             {format(Style(Swatch.yellow, Swatch.base))}
mark=               {format(Style(Swatch.yellow, Swatch.surface0))}
link_man=           {format(Style(Swatch.lang_purple, Swatch.mantle))}
link_man_f=         {format(Style(Swatch.pink, Swatch.mantle, (Mod.bold,)))}
link_http=          {format(Style(Swatch.lang_blue, Swatch.mantle))}
link_http_f=        {format(Style(Swatch.sky, Swatch.mantle, (Mod.bold,)))}
link_email=         {format(Style(Swatch.lang_blue, Swatch.mantle))}
link_email_f=       {format(Style(Swatch.sky, Swatch.mantle, (Mod.bold,)))}
link_file=          {format(Style(Swatch.lang_blue, Swatch.mantle))}
link_file_f=        {format(Style(Swatch.sky, Swatch.mantle, (Mod.bold,)))}
link_ls=            {format(Style(Swatch.maroon, Swatch.mantle))}
link_ls_f=          {format(Style(Swatch.lang_yellow, Swatch.mantle, (Mod.bold,)))}
sb_line=            {format(UI.scrollbar_track)}
sb_block=           {format(UI.scrollbar_knob)}
stat_indic_mode=    {format(UI.status_line_select)}
stat_indic_name=    {format(UI.status_line)}
stat_indic_loc=     {format(UI.status_line)}
stat_input_prompt=  {format(Style(Swatch.text, UI.status_line.bg))}
stat_input_help=    {format(Style(Swatch.green, UI.status_line.bg))}
stat_input_em=      {format(Style(Swatch.red, UI.status_line.bg))}
imm_border=         {format(Style(Swatch.uv2, Swatch.crust))}
imm_title=          {format(Style(Swatch.mauve, Swatch.crust))}
sp_input=           {format(Style(Swatch.text, Swatch.crust))}
sp_text=            {format(Style(Swatch.subtext1, Swatch.crust))}
sp_text_f=          {format(Style(Swatch.maroon, Swatch.crust))}
help_text=          {format(Style(Swatch.subtext1, Swatch.crust))}
help_text_f=        {format(Style(Swatch.maroon, Swatch.crust))}
history_text=       {format(Style(Swatch.subtext1, Swatch.crust))}
history_text_f=     {format(Style(Swatch.maroon, Swatch.crust))}
toc_text=           {format(Style(Swatch.subtext1, Swatch.crust))}
toc_text_f=         {format(Style(Swatch.maroon, Swatch.crust))}
""",
        "place": {
            "posix": Path.home() / ".config" / "qman" / "themes",
            "darwin": Path.home() / ".config" / "qman" / "themes",
            "windows": None,
        },
        "file": "franky.conf",
    }
