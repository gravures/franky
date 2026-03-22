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
"""Helix Franky theme."""

from __future__ import annotations

import os
from pathlib import Path

from franky import UI, Lang, Markup, Mod, Style, Swatch, Theme


def format(style: Style) -> str:  # noqa: A001
    mods = tuple(f'"{m.value}"' for m in filter(lambda m: m is not Mod.underlined, style.mods))

    underline = None
    if style.underline:
        color = f'color = "{style.underline.color}", ' if style.underline.color else ""
        underline = f'underline = {{ {color}style = "{style.underline.style}" }}'

    formatted = filter(
        None,
        (
            f'fg = "{style.fg}"' if style.fg else None,
            f'bg = "{style.bg}"' if style.bg else None,
            f"modifiers = [{', '.join(mods)}]" if mods else None,
            underline,
        ),
    )
    return f"{{ {', '.join(formatted)} }}" if formatted else ""


def main() -> Theme:
    return {
        "content": f"""
##
# Helix Franky Theme

# LANGUAGE
attribute = {format(Lang.attribute)}
keyword = {format(Lang.keyword)}
'keyword.control' = {format(Lang.control)}
'keyword.control.conditional' = {format(Lang.control_conditional)}
'keyword.control.repeat' = {format(Lang.control_repeat)}
'keyword.control.import' = {format(Lang.control_import)}
'keyword.control.retun' = {format(Lang.control_return)}
'keyword.control.exception' = {format(Lang.control_exception)}
'keyword.directive' = {format(Lang.directive)}  # -- preprocessor comments (#if in C)
'keyword.operator' = {format(Lang.keyword_operator)}
'keyword.function' = {format(Lang.keyword_function)}
'keyword.storage.type' = {format(Lang.keyword_storage_type)}
'keyword.storage.modifier' = {format(Lang.keyword_storage_modifier)}

'namespace' = {format(Lang.namespace)}

'punctuation' = {format(Lang.punctuation)}
'punctuation.bracket' = {format(Lang.punctuation_bracket)}
'punctuation.delimiter' = {format(Lang.punctuation_delimiter)}
'punctuation.special' = {format(Lang.punctuation_special)}

'operator' = {format(Lang.operator)}
'special' = {format(Lang.special)}  # fuzzy highlight

'variable' = {format(Lang.variable)}
'variable.builtin' = {format(Lang.variable_builtin)}
'variable.parameter' = {format(Lang.variable_parameter)}
'variable.other.member' = {format(Lang.variable_other_member)}
'variable.other.member.private' = {format(Lang.variable_other_member_private)}
# TODO: mutable

'type' = {format(Lang.type)}
'type.builtin' = {format(Lang.type_builtin)}
'type.enum.variant' = {format(Lang.type_enum_member)}

'constructor' = {format(Lang.constructor)}

'function' = {format(Lang.function)}
'function.method' = {format(Lang.function_method)}
'function.method.private' = {format(Lang.function_method_private)}
'function.macro' = {format(Lang.macro)}
'function.builtin' = {format(Lang.builtin)}
'function.special' = {format(Lang.function_special)}

'comment' = {format(Lang.comment)}
'comment.line' = {format(Lang.comment)}
'comment.block' = {format(Lang.comment)}
'comment.unused' = {format(Style(mods=(Mod.italic,)))}

'string' = {format(Lang.string)}
'string.regexp' = {format(Lang.string)}
'string.special.path' = {format(Lang.string)}
'string.special.url' = {format(Lang.string)}
'string.special.symbol' = {format(Lang.string)}

'constant' = {format(Lang.constant)}
'constant.builtin' = {format(Lang.constant)}
'constant.builtin.boolean' = {format(Lang.constant)}
'constant.numeric.integer' = {format(Lang.number)}
'constant.numeric.float' = {format(Lang.number)}
'constant.character.escape' = {format(Lang.escape)}

'label' = {format(Lang.label)}  # used for lifetimes, .class, #id in CSS, etc.
'tag' = {format(Lang.tag)}
'tag.builtin' = {format(Lang.tag)}


# MARKUP
'markup' = {format(Markup.markup)}
'markup.heading.marker' = {format(Markup.heading_marker)}
'markup.heading.1' = {format(Markup.heading_1)}
'markup.heading.2' = {format(Markup.heading_2)}
'markup.heading.3' = {format(Markup.heading_3)}
'markup.heading.4' = {format(Markup.heading_4)}
'markup.heading.5' = {format(Markup.heading_5)}
'markup.heading.6' = {format(Markup.heading_6)}

'markup.list.unnumbered' = {format(Markup.list_unnumbered)}
'markup.list.numbered' = {format(Markup.list_numbered)}
'markup.list.unchecked' = {format(Markup.list_unchecked)}
'markup.list.checked' = {format(Markup.list_checked)}

'markup.bold' = {format(Markup.bold)}
'markup.italic' = {format(Markup.italic)}
'markup.strikethrough' = {format(Markup.strike_through)}

'markup.link.url' = {format(Markup.link_url)}
'markup.link.label' = {format(Markup.link_label)}
'markup.link.text' = {format(Markup.link_text)}

'markup.quote' = {format(Markup.quote)}

'markup.raw' = {format(Markup.raw)}
'markup.raw.inline' = {format(Markup.raw_inline)}
'markup.raw.block' = {format(Markup.raw_block)}


# UI CANVAS
'ui.background' = {format(UI.background)}
'ui.background.separator' = {format(UI.background_separator)}

'ui.cursor' = {format(UI.cursor)}
'ui.cursor.insert' = {format(UI.cursor_line)}
'ui.cursor.select' = {format(UI.cursor_select)}
'ui.cursor.match' = {format(UI.cursor_match)}
'ui.cursor.primary' = {format(UI.cursor_primary)}
'ui.cursor.primary.insert' = {format(UI.cursor_primary_insert)}
'ui.cursor.primary.select' = {format(UI.cursor_primary_select)}

'ui.cursorline.primary' = {format(UI.cursor_line)}

'ui.selection' = {format(UI.selection)}
'ui.selection.primary' = {format(UI.selection_primary)}

'ui.virtual.ruler' = {format(UI.ruler)}
'ui.virtual.indent-guide' = {format(UI.indent_guide)}
'ui.virtual.inlay-hint' = {format(UI.inlay_hint)}
'ui.virtual.wrap' = {format(UI.wrap)}
'ui.virtual.jump-label' = {format(UI.jump_label)}

'diagnostic.hint' = {format(UI.diagnostic_hint)}
'diagnostic.info' = {format(UI.diagnostic_info)}
'diagnostic.warning' = {format(UI.diagnostic_warning)}
'diagnostic.error' = {format(UI.diagnostic_error)}
'diagnostic.unnecessary' = {format(UI.diagnostic_unnecessary)}


# GUTTERS
'ui.linenr' = {format(UI.line_number)}
'ui.linenr.selected' = {format(UI.line_number_select)}

hint = {format(UI.hint)}
info = {format(UI.info)}
warning = {format(UI.warning)}
error = {format(UI.error)}

'diff.plus' = {format(UI.diff_plus)}
'diff.minus' = {format(UI.diff_minus)}
'diff.delta' = {format(UI.diff_delta)}
'diff.delta.moved' = {format(UI.diff_delta_moved)}

'ui.debug.breakpoint' = "text"
'ui.debug.active' = "sky"

'ui.gutter' = {format(UI.gutter)}
'ui.gutter.selected' = {format(UI.gutter_selected)}


# STATUS LINE
'ui.statusline' = {format(UI.status_line)}
'ui.statusline.inactive' = {format(UI.status_line_inactive)}
'ui.statusline.normal' = {format(UI.status_line_normal)}
'ui.statusline.insert' = {format(UI.status_line_insert)}
'ui.statusline.select' = {format(UI.status_line_select)}


## BUFFER LINE
'ui.bufferline' = {format(UI.buffer_line)}
'ui.bufferline.active' = {format(UI.buffer_line_active)}
'ui.bufferline.background' = {format(UI.buffer_line_background)}


# WIDGETS
'ui.window' = {format(Style(Swatch.surface1, Swatch.base))}  # window == split
'ui.popup' = {format(Style(None, Swatch.surface1))}
'ui.popup.info' = {format(Style(Swatch.mauve))}  # popup border & title
'ui.text.info' = {format(Style(Swatch.subtext0))}
'ui.help' = {format(Style(Swatch.subtext0, Swatch.crust))}
'ui.text' = {format(Style(Swatch.subtext1))}  # markdown text also (very annoying !!!)
'ui.text.focus' = {format(Style(Swatch.teal))}
'ui.text.inactive' = {format(Style(Swatch.overlay0))}
'ui.text.directory' = {format(Style(Swatch.sky))}
# Highlighted lines in picker preview and lsp symbol
'ui.highlight' = {format(Style(Swatch.rosewater, Swatch.surface0))}
# TODO: ui.highlight.frameline  # debugger active line
'ui.menu' = {format(Style(Swatch.subtext1, Swatch.uv0))}
'ui.menu.selected' = {format(Style(Swatch.rosewater, Swatch.uv2))}
'ui.menu.scroll' = {format(Style(Swatch.green, Swatch.uv0))}
""",
        "place": {
            "posix": Path.home() / ".config" / "helix" / "themes",
            "darwin": Path.home() / ".config" / "helix" / "themes",
            "windows": Path(os.getenv("APPDATA", Path.home() / "AppData" / "Roaming"))
            / "helix"
            / "themes",
        },
        "file": "franky.toml",
    }
