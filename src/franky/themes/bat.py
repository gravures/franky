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
# ruff: noqa: D103
"""Bat Franky theme."""

from __future__ import annotations

import itertools
import os
from pathlib import Path

from franky import UI, Generic, Lang, Markup, Meta, Mod, Style, Swatch, Theme


_SCOPES: list[tuple[str, str, Style]] = [
    # ==========================================
    # COMMENTS
    # ==========================================
    ("Comment", "comment", Lang.comment),
    ("Comment Line", "comment.line", Lang.comment),
    ("Comment Block", "comment.block", Lang.comment),
    ("Comment Documentation", "comment.documentation", Lang.comment),
    ("Comment Documentation Python", "comment.documentation.python", Lang.string),
    ("Comment Block Documentation", "comment.block.documentation", Lang.string),
    (
        "Comment Preprocessor",
        "comment.preprocessor",
        Style(Swatch.lang_red, mods=(Mod.italic,)),
    ),
    ("Comment Preprocessor File", "comment.preprocessor.file", Lang.comment),
    ("Comment Special", "comment.special", Lang.comment),
    ("Comment TODO", "comment.todo", Style(Swatch.lang_yellow, mods=(Mod.bold,))),
    ("Comment FIXME", "comment.fixme", Style(Swatch.red, mods=(Mod.bold,))),
    ("Comment XXX", "comment.xxx", Style(Swatch.red, mods=(Mod.bold,))),
    # ==========================================
    # STRINGS
    # ==========================================
    ("String", "string", Lang.string),
    ("String Affix", "string.affix", Lang.string),
    ("String Backtick", "string.backtick", Lang.string),
    ("String Decorator", "string.decorator", Lang.string),
    ("String Double Quote", "string.double", Lang.string),
    ("String Single Quote", "string.single", Lang.string),
    ("String Triple Quote", "string.triple", Lang.string),
    ("String Interpolated", "string.interpolated", Lang.string),
    ("String Regex", "string.regexp", Lang.string),
    ("String Other", "string.other", Lang.string),
    (
        "String Escape",
        "string.escape constant.character.escape",
        Lang.escape,
    ),
    ("String Character", "string.character", Lang.string),
    ("String Numeric", "string.numeric", Lang.number),
    ("String Symbol", "string.symbol", Lang.string),
    ("String Template", "string.template", Lang.string),
    ("String Type", "string.type", Lang.string),
    (
        "String URL",
        "string.unquoted.url markup.underline.link",
        Style(Swatch.sky, mods=(Mod.underlined,)),
    ),
    ("String IP Address", "string.other.ip", Lang.string),
    ("String Entity", "string.entity", Lang.string),
    (
        "String Regular Expression",
        "string.regexp constant.character.regexp",
        Lang.string,
    ),
    ("String Other", "string.other.color", Lang.string),
    ("String Other Link", "string.other.link", Lang.string),
    ("String Other Marker", "string.other.marker", Lang.string),
    ("String Other Parameter", "string.other.param", Lang.string),
    ("String Other Prefix", "string.other.prefix", Lang.string),
    ("String Other Suffix", "string.other.suffix", Lang.string),
    # ==========================================
    # KEYWORDS
    # ==========================================
    ("Keyword", "keyword", Lang.keyword),
    ("Keyword Control", "keyword.control", Lang.control),
    (
        "Keyword Control Conditional",
        "keyword.control.conditional",
        Lang.control_conditional,
    ),
    (
        "Keyword Control Repeat",
        "keyword.control.repeat",
        Lang.control_repeat,
    ),
    (
        "Keyword Control Import",
        "keyword.control.import keyword.control.from",
        Lang.control_import,
    ),
    (
        "Keyword Control Return",
        "keyword.control.return keyword.control.exception",
        Lang.control_return,
    ),
    (
        "Keyword Control Exception",
        "keyword.control.exception",
        Lang.control_exception,
    ),
    ("Keyword Control Copy", "keyword.control.copy", Lang.control),
    (
        "Keyword Control Operator",
        "keyword.control.operator",
        Lang.keyword_operator,
    ),
    ("Keyword Control Regex", "keyword.control.regex", Lang.keyword),
    ("Keyword Control Shell", "keyword.control.shell", Lang.keyword),
    ("Keyword Control SQL", "keyword.control.sql", Lang.keyword),
    ("Keyword Control Haskell", "keyword.control.haskell", Lang.keyword),
    (
        "Keyword Operator",
        "keyword.operator",
        Lang.keyword_operator,
    ),
    (
        "Keyword Operator Assignment",
        "keyword.operator.assignment",
        Lang.keyword_operator,
    ),
    (
        "Keyword Operator Arithmetic",
        "keyword.operator.arithmetic",
        Lang.keyword_operator,
    ),
    (
        "Keyword Operator Comparison",
        "keyword.operator.comparison",
        Lang.keyword_operator,
    ),
    (
        "Keyword Operator Logical",
        "keyword.operator.logical",
        Lang.keyword_operator,
    ),
    (
        "Keyword Operator Bitwise",
        "keyword.operator.bitwise",
        Lang.keyword_operator,
    ),
    (
        "Keyword Operator Word",
        (
            "keyword.operator.word keyword.operator.new keyword.operator.delete"
            " keyword.operator.instanceof keyword.operator.typeof"
            " keyword.operator.alignmentof keyword.operator.sizeof"
            " keyword.operator.cast"
        ),
        Lang.keyword_operator,
    ),
    ("Keyword Operator Pointer", "keyword.operator.pointer", Lang.keyword_operator),
    (
        "Keyword Operator Variadic",
        "keyword.operator.variadic",
        Lang.keyword_operator,
    ),
    ("Keyword Function", "keyword.function", Lang.keyword_function),
    ("Keyword Namespace", "keyword.namespace", Lang.keyword),
    ("Keyword Placeholder", "keyword.placeholder", Lang.keyword),
    (
        "Keyword Storage",
        "keyword.storage",
        Lang.keyword_storage,
    ),
    (
        "Keyword Storage Type",
        "keyword.storage.type",
        Lang.keyword_storage_type,
    ),
    (
        "Keyword Storage Modifiers",
        (
            "keyword.storage.modifier keyword.storage.type.annotation"
            " keyword.storage.type.class keyword.storage.type.function"
            " keyword.storage.type.namespace keyword.storage.type.property"
            " keyword.storage.type.variable"
        ),
        Lang.keyword_storage_modifier,
    ),
    ("Keyword Type", "keyword.type", Lang.keyword_storage_type),
    ("Keyword Other", "keyword.other", Lang.keyword),
    ("Keyword Unit", "keyword.other.unit", Lang.number),
    ("Keyword Decspecial", "keyword.decspecial", Lang.keyword),
    ("Keyword Predeclared", "keyword.predeclared", Lang.keyword),
    ("Keyword Variable", "keyword.variable", Lang.keyword),
    ("Keyword Directive", "keyword.directive", Lang.directive),
    ("Keyword Directive Define", "keyword.directive.define", Lang.directive),
    ("Keyword Directive Include", "keyword.directive.include", Lang.directive),
    # ==========================================
    # OPERATORS
    # ==========================================
    (
        "Operator",
        "keyword.operator.assignment keyword.operator.assignment.compound",
        Lang.keyword_operator,
    ),
    # ==========================================
    # NAMESPACES
    # ==========================================
    ("Namespace", "entity.name.namespace", Lang.namespace),
    # ==========================================
    # SPECIAL
    # ==========================================
    ("Special", "special", Lang.special),
    # ==========================================
    # PUNCTUATION
    # ==========================================
    ("Punctuation", "punctuation", Lang.punctuation),
    (
        "Punctuation Definition",
        "punctuation.definition",
        Lang.punctuation_delimiter,
    ),
    (
        "Punctuation Definition Comment",
        "punctuation.definition.comment",
        Lang.punctuation,
    ),
    (
        "Punctuation Definition String",
        "punctuation.definition.string",
        Lang.punctuation,
    ),
    (
        "Punctuation Definition Variable",
        "punctuation.definition.variable",
        Lang.punctuation,
    ),
    (
        "Punctuation Definition Parameters",
        "punctuation.definition.parameters",
        Lang.punctuation_bracket,
    ),
    (
        "Punctuation Definition String Beginning",
        "punctuation.definition.string.begin",
        Lang.punctuation,
    ),
    (
        "Punctuation Definition String End",
        "punctuation.definition.string.end",
        Lang.punctuation,
    ),
    (
        "Punctuation Definition Blocks",
        (
            "punctuation.definition.block"
            " punctuation.definition.block.begin"
            " punctuation.definition.block.end"
        ),
        Lang.punctuation_bracket,
    ),
    (
        "Punctuation Definition List",
        (
            "punctuation.definition.list"
            " punctuation.definition.list.begin"
            " punctuation.definition.list.end"
        ),
        Lang.punctuation_bracket,
    ),
    (
        "Punctuation Definition Dictionary",
        (
            "punctuation.definition.dictionary"
            " punctuation.definition.dictionary.begin"
            " punctuation.definition.dictionary.end"
        ),
        Lang.punctuation_bracket,
    ),
    (
        "Punctuation Section",
        "punctuation.section punctuation.section.block punctuation.section.group",
        Lang.punctuation,
    ),
    (
        "Punctuation Separator",
        "punctuation.separator",
        Lang.punctuation_delimiter,
    ),
    (
        "Punctuation Separator Continuation",
        "punctuation.separator.continuation",
        Lang.punctuation_delimiter,
    ),
    (
        "Punctuation Separator Key",
        "punctuation.separator.key",
        Lang.punctuation_delimiter,
    ),
    (
        "Punctuation Separator Key-Value",
        "punctuation.separator.key-value",
        Lang.punctuation_delimiter,
    ),
    ("Punctuation Accessor", "punctuation.accessor", Lang.punctuation_delimiter),
    (
        "Punctuation Terminator",
        "punctuation.terminator",
        Lang.punctuation_delimiter,
    ),
    (
        "Punctuation Terminator Statement",
        "punctuation.terminator.statement",
        Lang.punctuation_delimiter,
    ),
    (
        "Punctuation Separator Pipe",
        "punctuation.separator.pipe",
        Lang.punctuation_delimiter,
    ),
    (
        "Punctuation Type",
        "punctuation.type",
        Lang.punctuation,
    ),
    (
        "Punctuation Section Import",
        "punctuation.section.import",
        Lang.punctuation,
    ),
    (
        "Punctuation Section Function",
        "punctuation.section.function",
        Lang.punctuation,
    ),
    (
        "Punctuation Infix Hyper",
        "punctuation.infix.hyper",
        Lang.punctuation,
    ),
    (
        "Punctuation Def KeyValuePair",
        "punctuation.def.keyValuePair",
        Lang.punctuation_delimiter,
    ),
    (
        "Punctuation Separator Colon",
        "punctuation.separator.colon",
        Lang.punctuation_delimiter,
    ),
    (
        "Punctuation Separator Comma",
        "punctuation.separator.comma",
        Lang.punctuation_delimiter,
    ),
    (
        "Punctuation Separator Dot",
        "punctuation.separator.dot",
        Lang.punctuation_delimiter,
    ),
    (
        "Punctuation Section Method",
        "punctuation.section.method",
        Lang.punctuation,
    ),
    (
        "Punctuation Definition Generic",
        "punctuation.definition.generic",
        Lang.punctuation_bracket,
    ),
    (
        "Punctuation Definition Arguments",
        "punctuation.definition.arguments",
        Lang.punctuation_bracket,
    ),
    (
        "Punctuation Definition Class Body",
        "punctuation.definition.class.body punctuation.definition.module.body",
        Lang.punctuation_bracket,
    ),
    (
        "Punctuation Section Brace",
        "punctuation.section.block.begin punctuation.section.block.end",
        Lang.punctuation_bracket,
    ),
    (
        "Punctuation Definition Interpolation",
        "punctuation.definition.interpolation",
        Lang.punctuation_special,
    ),
    (
        "Punctuation Section Embedded",
        "punctuation.section.embedded",
        Lang.punctuation_special,
    ),
    (
        "Punctuation Definition Tag",
        "punctuation.definition.tag",
        Lang.punctuation,
    ),
    (
        "Punctuation Definition Keyword",
        "punctuation.definition.keyword",
        Lang.punctuation,
    ),
    (
        "Punctuation Special",
        "punctuation.special",
        Lang.punctuation_special,
    ),
    # ==========================================
    # CONSTANT
    # ==========================================
    ("Constant", "constant", Lang.constant),
    ("Constant Language", "constant.language", Lang.constant),
    (
        "Constant Language Boolean",
        (
            "constant.language.boolean constant.language.null"
            " constant.language.nan constant.language.infinity"
        ),
        Lang.constant,
    ),
    ("Constant Language Nil", "constant.language.nil", Lang.constant),
    ("Constant Language Empty", "constant.language.empty", Lang.constant),
    (
        "Constant Language Continuation",
        "constant.language.continuation",
        Lang.constant,
    ),
    ("Constant Language Default", "constant.language.default", Lang.constant),
    ("Constant Language End", "constant.language.end", Lang.constant),
    ("Constant Language Key", "constant.language.key", Lang.constant),
    ("Constant Language Marked", "constant.language.marked", Lang.constant),
    ("Constant Language Special", "constant.language.special", Lang.constant),
    ("Constant Language Escape", "constant.language.escape", Lang.escape),
    (
        "Constant Other",
        "constant.other",
        Lang.constant,
    ),
    (
        "Constant Other Placeholder",
        "constant.other.placeholder",
        Lang.constant,
    ),
    ("Constant Other Key", "constant.other.key", Lang.constant),
    # ==========================================
    # NUMBERS
    # ==========================================
    ("Number", "constant.numeric", Lang.number),
    ("Number Integer", "constant.numeric.integer", Lang.number),
    ("Number Float", "constant.numeric.float", Lang.number),
    ("Number Hex", "constant.numeric.hex", Lang.number),
    ("Number Octal", "constant.numeric.octal", Lang.number),
    ("Number Binary", "constant.numeric.binary", Lang.number),
    ("Number Real", "constant.numeric.real", Lang.number),
    ("Number Scientific", "constant.numeric.scientific", Lang.number),
    ("Number Complex", "constant.numeric.complex", Lang.number),
    ("Number Hex Float", "constant.numeric.hex.float", Lang.number),
    ("Number Octal Float", "constant.numeric.octal.float", Lang.number),
    ("Number Binary Float", "constant.numeric.binary.float", Lang.number),
    # ==========================================
    # VARIABLES
    # ==========================================
    ("Variable", "variable", Lang.variable),
    (
        "Variable Language",
        "variable.language",
        Lang.variable_builtin,
    ),
    (
        "Variable Language Builtin",
        "variable.language.builtin",
        Lang.variable_builtin,
    ),
    (
        "Variable Language This",
        "variable.language.this variable.language.self",
        Lang.variable_builtin,
    ),
    (
        "Variable Other",
        "variable.other",
        Lang.variable_other,
    ),
    (
        "Variable Other Read Write",
        "variable.other.readwrite",
        Lang.variable_other,
    ),
    (
        "Variable Other Member",
        "variable.other.member",
        Lang.variable_other_member,
    ),
    (
        "Variable Other Member Private",
        "variable.other.member.private",
        Lang.variable_other_member_private,
    ),
    (
        "Variable Other Constant",
        "variable.other.constant",
        Lang.variable_other,
    ),
    (
        "Variable Other Class",
        "variable.other.class",
        Lang.variable,
    ),
    (
        "Variable Other Object",
        "variable.other.object",
        Lang.variable,
    ),
    (
        "Variable Other Property",
        "variable.other.property",
        Lang.variable_other_member,
    ),
    (
        "Variable Other Block",
        "variable.other.block",
        Lang.variable,
    ),
    (
        "Variable Other Deprecated",
        "variable.other.deprecated",
        Style(Swatch.subtext0, mods=(Mod.crossed_out,)),
    ),
    (
        "Variable Parameter",
        "variable.parameter",
        Lang.variable_parameter,
    ),
    (
        "Variable Builtin",
        "variable.builtin",
        Lang.variable_builtin,
    ),
    # ==========================================
    # FUNCTIONS
    # ==========================================
    (
        "Entity Name Function",
        "entity.name.function",
        Lang.function,
    ),
    (
        "Function Builtin",
        "entity.name.function.builtin support.function.builtin support.function",
        Lang.builtin,
    ),
    (
        "Function Special",
        "entity.name.function.special support.function.special",
        Lang.function_special,
    ),
    (
        "Function Preprocessor",
        "keyword.control.import keyword.control.import.*",
        Lang.keyword,
    ),
    (
        "Function Developer Defined Identifier",
        "entity.other.developer.defined-identifier",
        Lang.function,
    ),
    (
        "Function Deprecated",
        "entity.name.function.deprecated",
        Style(Swatch.subtext0, mods=(Mod.crossed_out,)),
    ),
    (
        "Entity Name Method",
        "entity.name.function.method",
        Lang.function_method,
    ),
    (
        "Entity Name Method Private",
        "entity.name.function.method.private",
        Lang.function_method_private,
    ),
    (
        "Entity Name Type Function",
        "entity.name.type.function",
        Lang.function,
    ),
    # ==========================================
    # TYPES
    # ==========================================
    (
        "Support Type",
        "support.type",
        Lang.type_builtin,
    ),
    (
        "Support Other Namespace",
        "support.other.namespace",
        Lang.type_builtin,
    ),
    (
        "Entity Name Type",
        "entity.name.type entity.name.class entity.name.struct entity.name.union",
        Lang.type,
    ),
    (
        "Entity Name Type Parameter",
        "entity.name.type.parameter",
        Lang.type,
    ),
    (
        "Entity Other Inherited Class",
        "entity.other.inherited-class",
        Lang.type,
    ),
    (
        "Entity Name Type Class",
        "entity.name.type.class",
        Lang.type,
    ),
    (
        "Entity Name Type Enum",
        "entity.name.type.enum",
        Lang.type,
    ),
    (
        "Entity Name Type Exception",
        "entity.name.type.exception",
        Lang.exception,
    ),
    (
        "Entity Name Type Struct",
        "entity.name.type.struct",
        Lang.type,
    ),
    (
        "Entity Name Type Union",
        "entity.name.type.union",
        Lang.type,
    ),
    (
        "Entity Name Type Trait",
        "entity.name.type.trait",
        Lang.type,
    ),
    (
        "Entity Name Type Interface",
        "entity.name.type.interface",
        Lang.type,
    ),
    (
        "Entity Name Type Alias",
        "entity.name.type.alias",
        Lang.type,
    ),
    (
        "Entity Name Type Protocol",
        "entity.name.type.protocol",
        Lang.type,
    ),
    (
        "Entity Name Type Template",
        "entity.name.type.template",
        Lang.type,
    ),
    (
        "Entity Name Type Namespace",
        "entity.name.type.namespace",
        Lang.type,
    ),
    (
        "Entity Name Tag",
        "entity.name.tag",
        Lang.tag,
    ),
    (
        "Entity Name Tag Attribute Class",
        "entity.name.tag.attribute.class",
        Lang.tag,
    ),
    (
        "Entity Name Tag Attribute Id",
        "entity.name.tag.attribute.id",
        Lang.tag,
    ),
    (
        "Entity Name Tag Attribute Name",
        "entity.name.tag.attribute.name",
        Lang.attribute,
    ),
    (
        "Entity Name Tag Attribute Value",
        "entity.name.tag.attribute.value",
        Lang.string,
    ),
    (
        "Entity Name Tag Other",
        "entity.name.tag.other",
        Lang.tag,
    ),
    (
        "Entity Name Tag Inline",
        "entity.name.tag.inline",
        Lang.tag,
    ),
    # ==========================================
    # ENUM MEMBERS
    # ==========================================
    (
        "Support Constant",
        "support.constant",
        Lang.type_enum_member,
    ),
    (
        "Variable Other Constant Class",
        "variable.other.constant.class",
        Lang.type_enum_member,
    ),
    (
        "Variable Other Constant Object",
        "variable.other.constant.object",
        Lang.type_enum_member,
    ),
    (
        "Variable Other Constant Property",
        "variable.other.constant.property",
        Lang.type_enum_member,
    ),
    # ==========================================
    # CONSTRUCTORS
    # ==========================================
    (
        "Entity Name Function Constructor",
        "entity.name.function.constructor",
        Lang.constructor,
    ),
    (
        "Support Class",
        "support.class",
        Lang.constructor,
    ),
    # ==========================================
    # DECORATORS
    # ==========================================
    (
        "Entity Name Function Decorator",
        "entity.name.function.decorator",
        Lang.decorator,
    ),
    (
        "Entity Name Function Decorator Preprocessor",
        "entity.name.function.decorator.preprocessor",
        Lang.decorator,
    ),
    # ==========================================
    # LABELS
    # ==========================================
    ("Entity Name Label", "entity.name.label", Lang.label),
    ("Entity Name Section", "entity.name.section", Lang.label),
    # ==========================================
    # SPECIAL
    # ==========================================
    (
        "Entity Name",
        "entity.name",
        Lang.namespace,
    ),
    (
        "Entity Other",
        "entity.other",
        Lang.namespace,
    ),
    (
        "Support Function",
        "support.function",
        Lang.builtin,
    ),
    (
        "Entity Name Instance",
        "entity.name.instance",
        Lang.type,
    ),
    (
        "Entity Name Type Definition",
        "entity.name.type.definition",
        Lang.type,
    ),
    (
        "Entity Name Type Class Python",
        "entity.name.type.class.python",
        Lang.type,
    ),
    (
        "Entity Name Type Exception Python",
        "entity.name.type.exception.python support.function.exception",
        Lang.exception,
    ),
    # ==========================================
    # ATTRIBUTES
    # ==========================================
    (
        "Entity Other Attribute Name",
        "entity.other.attribute-name",
        Lang.attribute,
    ),
    (
        "Entity Other Attribute Name Id",
        "entity.other.attribute-name.id",
        Lang.attribute,
    ),
    (
        "Entity Other Attribute Name Class",
        "entity.other.attribute-name.class",
        Lang.attribute,
    ),
    # ==========================================
    # MARKUP
    # ==========================================
    (
        "Markup Heading",
        "markup.heading markup.heading punctuation.definition.heading",
        Style(Swatch.lang_blue, mods=(Mod.bold,)),
    ),
    (
        "Markup Heading Marker",
        "markup.heading punctuation.definition.heading",
        Style(Swatch.lang_blue),
    ),
    ("Markup Heading Heading 1", "markup.heading.heading-1", Markup.heading_1),
    ("Markup Heading Heading 2", "markup.heading.heading-2", Markup.heading_2),
    ("Markup Heading Heading 3", "markup.heading.heading-3", Markup.heading_3),
    ("Markup Heading Heading 4", "markup.heading.heading-4", Markup.heading_4),
    ("Markup Heading Heading 5", "markup.heading.heading-5", Markup.heading_5),
    ("Markup Heading Heading 6", "markup.heading.heading-6", Markup.heading_6),
    ("Markup Bold", "markup.bold", Markup.bold),
    ("Markup Italic", "markup.italic", Markup.italic),
    ("Markup Strikethrough", "markup.strikethrough", Markup.strike_through),
    ("Markup Underline", "markup.underline", Style(mods=(Mod.underlined,))),
    ("Markup Quote", "markup.quote", Style(Swatch.overlay1, mods=(Mod.italic,))),
    ("Markup Raw Inline", "markup.raw.inline", Markup.raw_inline),
    ("Markup Raw Block", "markup.raw.block", Markup.raw_block),
    ("Markup List", "markup.list", Markup.list_unnumbered),
    ("Markup List Numbered", "markup.list.numbered", Markup.list_numbered),
    ("Markup List Unnumbered", "markup.list.unnumbered", Markup.list_unnumbered),
    ("Markup List Checked", "markup.list.checked", Markup.list_checked),
    ("Markup List Unchecked", "markup.list.unchecked", Markup.list_unchecked),
    (
        "Markup Link",
        "markup.underline.link",
        Style(Swatch.sky, mods=(Mod.underlined,)),
    ),
    ("Markup Link Label", "entity.name.label", Markup.link_label),
    (
        "Markup Link URL",
        "markup.underline.link string.other.link",
        Style(Swatch.sky, mods=(Mod.underlined,)),
    ),
    ("Markup Link Description", "string.other.link.description", Markup.link_text),
    ("Markup Link Title", "string.other.link.title", Markup.link_label),
    (
        "Markup Link Anchor",
        "entity.name.type.instance punctuation.definition.constant",
        Markup.raw,
    ),
    ("Markup Meta Content", "markup.meta.content", Markup.markup),
    ("Markup Meta Delimiter", "markup.meta.delimiter", Markup.markup),
    ("Markup Changed", "markup.changed", Style(Swatch.yellow)),
    ("Markup Deleted", "markup.deleted", Style(Swatch.red)),
    ("Markup Inserted", "markup.inserted", Style(Swatch.green)),
    ("Markup Unused", "markup.unused", Style(Swatch.overlay1, mods=(Mod.italic,))),
    (
        "Markup Unverified",
        "markup.unverified",
        Style(Swatch.overlay1, mods=(Mod.italic,)),
    ),
    # ==========================================
    # GENERIC
    # ==========================================
    ("Generic Deleted", "generic.deleted", Generic.deleted),
    ("Generic Inserted", "generic.inserted", Style(Swatch.green)),
    ("Generic Changed", "generic.changed", Style(Swatch.yellow)),
    ("Generic Emphasis", "generic.emphasis", Generic.emphasis),
    ("Generic Strong", "generic.strong", Generic.strong),
    (
        "Generic Subheading",
        "generic.subheading",
        Style(Swatch.mauve, mods=(Mod.bold,)),
    ),
    (
        "Generic Deleted",
        "markup.deleted punctuation.definition.generic.deleted",
        Generic.deleted,
    ),
    (
        "Generic Inserted",
        "markup.inserted punctuation.definition.generic.inserted",
        Style(Swatch.green),
    ),
    (
        "Generic Changed",
        "markup.changed punctuation.definition.generic.changed",
        Style(Swatch.yellow),
    ),
    (
        "Generic Emphasis",
        "markup.italic punctuation.definition.generic.italic",
        Generic.emphasis,
    ),
    (
        "Generic Strong",
        "markup.bold punctuation.definition.generic.strong",
        Generic.strong,
    ),
    (
        "Generic Subheading",
        "markup.heading punctuation.definition.generic.heading",
        Style(Swatch.mauve, mods=(Mod.bold,)),
    ),
    # ==========================================
    # META
    # ==========================================
    (
        "Meta Preprocessor",
        "meta.preprocessor",
        Style(Swatch.lang_red),
    ),
    (
        "Meta Preprocessor Entity",
        "meta.preprocessor.entity",
        Style(Swatch.lang_blue),
    ),
    (
        "Meta Preprocessor Value",
        "meta.preprocessor.value",
        Style(Swatch.lang_blue),
    ),
    (
        "Meta Preprocessor Function",
        "meta.preprocessor.function",
        Style(Swatch.lang_blue),
    ),
    (
        "Meta Preprocessor Include",
        "meta.preprocessor.include",
        Style(Swatch.lang_red),
    ),
    (
        "Meta Preprocessor Include Path",
        "meta.preprocessor.include.path",
        Style(Swatch.lang_blue),
    ),
    (
        "Meta Embedded",
        "meta.embedded",
        Style(Swatch.text),
    ),
    (
        "Meta Brace",
        "meta.brace",
        Lang.punctuation_bracket,
    ),
    (
        "Meta Delimiter",
        "meta.delimiter",
        Lang.punctuation_delimiter,
    ),
    (
        "Meta Delimiter Period",
        "meta.delimiter.period",
        Lang.punctuation_delimiter,
    ),
    (
        "Meta Delimiter Comma",
        "meta.delimiter.comma",
        Lang.punctuation_delimiter,
    ),
    (
        "Meta Delimiter Whitespace",
        "meta.delimiter.whitespace",
        Lang.punctuation_delimiter,
    ),
    (
        "Meta Module Reference",
        "meta.module.reference",
        Style(Swatch.lang_blue),
    ),
    (
        "Meta Content Reference",
        "meta.content.reference",
        Style(Swatch.lang_blue),
    ),
    (
        "Meta Structure Annotation",
        "meta.structure.annotation",
        Style(Swatch.lang_blue),
    ),
    (
        "Meta Annotation",
        "meta.annotation",
        Lang.decorator,
    ),
    (
        "Meta Annotation punctuation",
        "meta.annotation punctuation",
        Lang.punctuation,
    ),
    (
        "Meta Attribute",
        "meta.attribute",
        Lang.attribute,
    ),
    (
        "Entity Name Namespace",
        "entity.name.namespace",
        Lang.type,
    ),
    # ==========================================
    # DIFF
    # ==========================================
    (
        "Diff Inserted",
        "markup.inserted punctuation.definition.inserted",
        UI.diff_plus,
    ),
    (
        "Diff Deleted",
        "markup.deleted punctuation.definition.deleted",
        UI.diff_minus,
    ),
    (
        "Diff Changed",
        "markup.changed",
        UI.diff_delta,
    ),
    (
        "Diff Meta",
        "meta.diff",
        UI.diff_delta,
    ),
    (
        "Diff Meta Header",
        "meta.diff.header",
        UI.diff_delta,
    ),
    (
        "Diff Meta Separator",
        "meta.diff.separator",
        Style(Swatch.overlay1),
    ),
    # ==========================================
    # CSS / SCSS
    # ==========================================
    (
        "CSS Support Type Property Name",
        "support.type.property-name.css",
        Style(Swatch.sky),
    ),
    (
        "CSS Support Constant",
        (
            "support.constant.property-value.css"
            " support.constant.font-name.css"
            " support.constant.color.css"
        ),
        Style(Swatch.lang_pink),
    ),
    ("CSS Support Constant Numeric", "support.constant.numeric.css", Lang.number),
    ("CSS Entity Name Tag", "entity.name.tag.css", Lang.tag),
    (
        "CSS Entity Other Attribute Name",
        "entity.other.attribute-name.class.css entity.other.attribute-name.id.css",
        Lang.attribute,
    ),
    (
        "CSS Punctuation Definition Keyword",
        "punctuation.definition.keyword.css",
        Lang.keyword,
    ),
    (
        "CSS Punctuation Definition Entity",
        "punctuation.definition.entity.css",
        Lang.punctuation,
    ),
    (
        "CSS Punctuation Section Function",
        "punctuation.section.function.begin.css punctuation.section.function.end.css",
        Lang.punctuation_bracket,
    ),
    ("SCSS Support Function", "support.function.misc.scss", Lang.builtin),
    ("SCSS Variable", "variable.scss", Lang.variable),
    ("SCSS Variable Definition", "variable.other.scss", Lang.variable),
    ("CSS Variable", "variable.css", Lang.variable),
    # ==========================================
    # JAVASCRIPT / TYPESCRIPT
    # ==========================================
    (
        "JS Support Object",
        "support.object.process.nodejs",
        Lang.builtin,
    ),
    (
        "JS Support Class",
        "support.class.math.nodejs",
        Lang.builtin,
    ),
    (
        "JS Support Function",
        "support.function.nodejs support.function.dom",
        Lang.builtin,
    ),
    ("JS Variable Language", "variable.language.js", Lang.variable_builtin),
    ("TS Entity Name Type", "entity.name.type.ts", Lang.type),
    ("TS Support Type", "support.type.primitive.ts", Lang.type_builtin),
    (
        "TS Entity Name Type Module",
        "entity.name.type.module.ts",
        Lang.type,
    ),
    # ==========================================
    # PYTHON
    # ==========================================
    ("Python Self", "variable.language.python self", Lang.variable_builtin),
    (
        "Python Function Decorator",
        "entity.name.function.decorator.python",
        Lang.decorator,
    ),
    ("Python Magic", "support.function.magic.python", Lang.magic),
    (
        "Python Magic Name",
        (
            "variable.parameter.positional.parameters.python"
            " variable.parameter.special.self.python"
            " variable.parameter.special.cls.python"
        ),
        Lang.variable_builtin,
    ),
    (
        "Python Type Hint",
        (
            "meta.function.annotation.python"
            " entity.name.type.annotation.python"
            " support.type.primitive.python"
        ),
        Lang.type,
    ),
    (
        "Python FString",
        (
            "string.quoted.fstring"
            " punctuation.definition.string.begin.python"
            " string.quoted.fstring"
            " punctuation.definition.string.end.python"
        ),
        Lang.punctuation,
    ),
    # ==========================================
    # RUBY
    # ==========================================
    ("Ruby Constant", "variable.other.constant.ruby", Lang.constant),
    (
        "Ruby Function Method",
        "entity.name.function.method.ruby",
        Lang.function_method,
    ),
    (
        "Ruby Instance Variable",
        "variable.other.readwrite.instance.ruby",
        Lang.variable,
    ),
    ("Ruby Global Variable", "variable.other.normal.ruby", Lang.variable),
    (
        "Ruby Class Variable",
        "variable.other.class.ruby",
        Lang.variable,
    ),
    (
        "Ruby Block Parameter",
        "variable.parameter.function.ruby",
        Lang.variable_parameter,
    ),
    (
        "Ruby String Interpolation",
        "meta.embedded.line.ruby support.class.ruby variable.other.readwrite.instance.ruby",
        Lang.string,
    ),
    ("Ruby Symbol", "constant.language.symbol.ruby", Lang.constant),
    (
        "Ruby Punctuation Definition Constant",
        "punctuation.definition.constant.ruby",
        Lang.punctuation,
    ),
    (
        "Ruby Keyword Control",
        "keyword.control.ruby keyword.control.alias.ruby",
        Lang.control,
    ),
    # ==========================================
    # GO
    # ==========================================
    ("Go Type Builtin", "support.type.builtin.go", Lang.type_builtin),
    ("Go Function Builtin", "support.function.builtin.go", Lang.builtin),
    ("Go Variable Builtin", "variable.language.go", Lang.variable_builtin),
    # ==========================================
    # RUST
    # ==========================================
    (
        "Rust Function Builtin",
        "support.function.builtin.rust",
        Lang.builtin,
    ),
    ("Rust Type Builtin", "support.type.rust", Lang.type_builtin),
    ("Rust Macro", "entity.name.macro.rust", Lang.macro),
    (
        "Rust Punctuation",
        "punctuation.definition.lifetime.rust",
        Lang.punctuation,
    ),
    ("Rust Attribute", "meta.attribute.rust", Lang.decorator),
    # ==========================================
    # JAVA
    # ==========================================
    ("Java Support Constant", "support.constant.java", Lang.constant),
    (
        "Java Entity Name Type Class",
        "entity.name.type.class.java",
        Lang.type,
    ),
    ("Java Entity Name Function", "entity.name.function.java", Lang.function),
    # ==========================================
    # C / C++
    # ==========================================
    ("C Type", "entity.name.type.c entity.name.type.cpp", Lang.type),
    ("C Function", "meta.function.c entity.name.function.c", Lang.function),
    (
        "C++ Function",
        "meta.function.cpp entity.name.function.cpp",
        Lang.function,
    ),
    ("C++ Type Builtin", "support.type.cpp", Lang.type_builtin),
    ("C++ Namespace", "entity.name.namespace.cpp", Lang.namespace),
    # ==========================================
    # PHP
    # ==========================================
    ("PHP Variable", "variable.other.php", Lang.variable),
    (
        "PHP String Interpolation",
        (
            "variable.other.php punctuation.definition.variable.php"
            " punctuation.definition.string.begin.php"
            " punctuation.definition.string.end.php"
        ),
        Lang.string,
    ),
    ("PHP Entity Name Type", "entity.name.type.php", Lang.type),
    ("PHP Support Class", "support.class.php", Lang.type),
    ("PHP Keyword Control", "keyword.control.php", Lang.control),
    # ==========================================
    # HTML
    # ==========================================
    ("HTML Entity Name Tag", "entity.name.tag.html", Lang.tag),
    (
        "HTML Entity Other Attribute Name",
        "entity.other.attribute-name.html",
        Lang.attribute,
    ),
    (
        "HTML Punctuation Definition Tag",
        "punctuation.definition.tag.html",
        Lang.punctuation,
    ),
    ("HTML String Interpolated", "string.interpolated.html", Lang.string),
    ("HTML String Double Quote", "string.quoted.double.html", Lang.string),
    ("HTML String Single Quote", "string.quoted.single.html", Lang.string),
    # ==========================================
    # SQL
    # ==========================================
    (
        "SQL Keyword",
        (
            "keyword.other.DML.sql keyword.other.data-integrity-languages.sql"
            " keyword.other.data-definition-languages.sql"
            " keyword.other.schema-control-sql"
            " keyword.other.transactions-locking.sql"
            " keyword.other.grant.sql keyword.other.revoke.sql"
            " keyword.other.set.sql keyword.other.begin.sql"
            " keyword.other.commit.sql keyword.other.rollback.sql"
        ),
        Lang.keyword,
    ),
    (
        "SQL Entity Name",
        "entity.name.table.sql entity.name.function.sql",
        Lang.type,
    ),
    ("SQL Support Function", "support.function.sql", Lang.builtin),
    ("SQL Support Type", "support.type.sql", Lang.type_builtin),
    ("SQL Variable", "variable.other.table.sql", Lang.variable),
    # ==========================================
    # SHELL / BASH
    # ==========================================
    (
        "Shell Variable",
        "variable.other.positional.parameters.shell variable.other.normal.shell",
        Lang.variable,
    ),
    (
        "Shell Variable Definition",
        "variable.other.positional.parameters.shell",
        Lang.variable,
    ),
    ("Shell Function", "entity.name.function.shell", Lang.function),
    ("Shell Keyword", "keyword.control.shell", Lang.control),
    (
        "Shell Command",
        "meta.function-call.shell support.function.builtin.shell",
        Lang.builtin,
    ),
    (
        "Shell String Interpolation",
        "string.interpolated.backtick.shell",
        Lang.string,
    ),
    # ==========================================
    # YAML
    # ==========================================
    ("YAML Key", "entity.name.tag.yaml", Lang.type),
    ("YAML Anchor", "constant.language.anchor.yaml", Lang.constant),
    # ==========================================
    # TOML
    # ==========================================
    ("TOML Key", "entity.name.tag.yaml entity.name.tag.toml", Lang.type),
    # ==========================================
    # JSON
    # ==========================================
    ("JSON Key", "support.type.property-name.json", Lang.type),
    ("JSON Null", "constant.language.json", Lang.constant),
    # ==========================================
    # XML
    # ==========================================
    ("XML Entity Name Tag", "entity.name.tag.xml", Lang.tag),
    (
        "XML Entity Other Attribute Name",
        "entity.other.attribute-name.xml",
        Lang.attribute,
    ),
    (
        "XML Punctuation Definition Tag",
        "punctuation.definition.tag.xml",
        Lang.punctuation,
    ),
    (
        "XML String",
        "string.quoted.double.xml string.quoted.single.xml",
        Lang.string,
    ),
    # ==========================================
    # MARKDOWN
    # ==========================================
    (
        "Markdown Heading",
        "markup.heading markup.heading punctuation.definition.heading.markdown",
        Markup.heading_1,
    ),
    ("Markdown Heading 1", "markup.heading.heading-1", Markup.heading_1),
    ("Markdown Heading 2", "markup.heading.heading-2", Markup.heading_2),
    ("Markdown Heading 3", "markup.heading.heading-3", Markup.heading_3),
    ("Markdown Heading 4", "markup.heading.heading-4", Markup.heading_4),
    ("Markdown Heading 5", "markup.heading.heading-5", Markup.heading_5),
    ("Markdown Heading 6", "markup.heading.heading-6", Markup.heading_6),
    ("Markdown Italic", "markup.italic", Markup.italic),
    ("Markdown Bold", "markup.bold", Markup.bold),
    (
        "Markdown Strikethrough",
        "markup.strikethrough",
        Markup.strike_through,
    ),
    ("Markdown List", "markup.list", Markup.list_unnumbered),
    ("Markdown List Numbered", "markup.list.numbered", Markup.list_numbered),
    ("Markdown List Unnumbered", "markup.list.unnumbered", Markup.list_unnumbered),
    ("Markdown Quote", "markup.quote", Markup.quote),
    ("Markdown Raw Inline", "markup.raw.inline", Markup.raw_inline),
    ("Markdown Raw Block", "markup.raw.block", Markup.raw_block),
    ("Markdown Link Text", "markup.underline.link", Markup.link_text),
    ("Markdown Link Label", "entity.name.label", Markup.link_label),
    (
        "Markdown Link URL",
        "string.other.link.description.title",
        Markup.link_url,
    ),
    (
        "Markdown Link Title",
        "string.other.link.description.title.begin string.other.link.description.title.end",
        Markup.link_label,
    ),
    # ==========================================
    # LAUGHTEX / LATEX
    # ==========================================
    (
        "TEX Entity Name Section",
        "entity.name.section.latex",
        Style(Swatch.lang_blue, mods=(Mod.bold,)),
    ),
    ("TEX Support Class", "support.class.latex", Lang.type_builtin),
    ("TEX Support Function", "support.function.latex", Lang.builtin),
    (
        "TEX Keyword Control",
        "keyword.control.latex keyword.operator.latex",
        Lang.keyword,
    ),
    ("TEX Variable", "variable.other.normal.latex", Lang.variable),
    (
        "TEX Entity Name Function",
        "entity.name.function.latex",
        Lang.function,
    ),
    (
        "TEX String Interpolated",
        "string.interpolated.latex string.other.math.latex",
        Lang.string,
    ),
    (
        "TEX Entity Other Attribute Name",
        "entity.other.attribute-name.latex",
        Lang.attribute,
    ),
    (
        "TEX Punctuation",
        "punctuation.definition.keyword.latex",
        Lang.punctuation,
    ),
    # ==========================================
    # LITERATE HASKELL
    # ==========================================
    (
        "Literate Haskell Meta",
        "meta.function.literate.haskell",
        Style(Swatch.lang_yellow),
    ),
    # ==========================================
    # PERL
    # ==========================================
    (
        "Perl Variable",
        "variable.other.readwrite.global.perl variable.other.predefined.perl",
        Lang.variable,
    ),
    ("Perl Variable Scalar", "variable.other.scalar.perl", Lang.variable),
    ("Perl Variable Array", "variable.other.array.perl", Lang.variable),
    ("Perl Variable Hash", "variable.other.hash.perl", Lang.variable),
    (
        "Perl String Interpolation",
        "string.interpolated.perl",
        Lang.string,
    ),
    (
        "Perl Regex",
        "string.regexp.xile.modperl",
        Lang.string,
    ),
    # ==========================================
    # CLOJURE
    # ==========================================
    (
        "Clojure Core Function",
        "constant.language.clojure",
        Lang.builtin,
    ),
    (
        "Clojure Core Macro",
        "support.function.macro.clojure",
        Lang.macro,
    ),
    # ==========================================
    # SWIFT
    # ==========================================
    ("Swift Function", "entity.name.function.swift", Lang.function),
    ("Swift Type", "entity.name.type.swift", Lang.type),
    # ==========================================
    # KOTLIN
    # ==========================================
    ("Kotlin Function", "entity.name.function.kotlin", Lang.function),
    ("Kotlin Type", "entity.name.type.kotlin", Lang.type),
    # ==========================================
    # Elixir
    # ==========================================
    ("Elixir Module", "entity.name.module.elixir", Lang.type),
    (
        "Elixir Variable",
        "variable.other.readwrite.elixir",
        Lang.variable,
    ),
    ("Elixir Keyword", "keyword.control.elixir", Lang.control),
    # ==========================================
    # ZIG
    # ==========================================
    (
        "Zig Builtin",
        "entity.name.function.builtin.zig",
        Lang.builtin,
    ),
    ("Zig Type Builtin", "support.type.zig", Lang.type_builtin),
    ("Zig Keyword", "keyword.control.zig", Lang.control),
    # ==========================================
    # NIX
    # ==========================================
    ("Nix Keyword", "keyword.control.nix", Lang.control),
]


def _xml_escape(text: str) -> str:
    return text.replace("&", "&amp;")


def _format(style: Style) -> str:
    parts: list[str] = []
    if style.fg:
        parts.append(f"<key>foreground</key>\n          <string>{style.fg}</string>")
    if style.bg:
        parts.append(f"<key>background</key>\n          <string>{style.bg}</string>")
    if style.mods:
        mods: list[str] = []
        for m in style.mods:
            if m is Mod.bold:
                mods.append("bold")
            elif m is Mod.italic:
                mods.append("italic")
            elif m is Mod.underlined:
                mods.append("underline")
            elif m is Mod.crossed_out:
                mods.append("strikethrough")
        if mods:
            parts.append(f"<key>fontStyle</key>\n          <string>{' '.join(mods)}</string>")
    return "\n          ".join(parts)


def _entry(name: str | None, scope: str, style: Style) -> str:
    fmt = _format(style)
    if not fmt:
        return ""
    name_xml = (
        f"\n        <key>name</key>\n        <string>{_xml_escape(name)}</string>" if name else ""
    )
    return (
        f"      <dict>"
        f"{name_xml}"
        f"\n        <key>scope</key>"
        f"\n        <string>{_xml_escape(scope)}</string>"
        f"\n        <key>settings</key>"
        f"\n        <dict>"
        f"\n          {fmt}"
        f"\n        </dict>"
        f"\n      </dict>"
    )


def main() -> Theme:
    scope_entries = "\n".join(itertools.starmap(_entry, _SCOPES))

    content = f"""\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>name</key>
    <string>Franky</string>
    <key>semanticClass</key>
    <string>theme.dark.franky</string>
    <key>uuid</key>
    <string>a1b2c3d4-e5f6-7890-abcd-ef1234567890</string>
    <key>author</key>
    <string>Franky</string>
    <key>colorSpaceName</key>
    <string>sRGB</string>
    <key>settings</key>
    <array>
      <dict>
        <key>settings</key>
        <dict>
          <key>background</key>
          <string>{UI.background.bg}</string>
          <key>foreground</key>
          <string>{UI.background.fg}</string>
          <key>caret</key>
          <string>{Meta.caret.fg}</string>
          <key>selection</key>
          <string>{UI.selection.bg}</string>
          <key>selectionForeground</key>
          <string>{UI.selection.fg}</string>
          <key>lineHighlight</key>
          <string>{UI.cursor_line.bg}</string>
          <key>gutter</key>
          <string>{UI.gutter.bg}</string>
          <key>gutterForeground</key>
          <string>{UI.gutter.fg}</string>
          <key>gutterSelectedForeground</key>
          <string>{UI.line_number_select.fg}</string>
          <key>findHighlightBackground</key>
          <string>{UI.cursor_match.bg}</string>
          <key>guide</key>
          <string>{UI.indent_guide.fg}</string>
          <key>inactiveSelection</key>
          <string>{Swatch.uv0}</string>
          <key>lineNumber</key>
          <string>{UI.line_number.fg}</string>
          <key>lineNumberActive</key>
          <string>{UI.line_number_select.fg}</string>
          <key>invisibles</key>
          <string>{Swatch.surface1}</string>
          <key>lineHighlightBackground</key>
          <string>{UI.cursor_line.bg}</string>
          <key>selectionBackground</key>
          <string>{UI.selection.bg}</string>
          <key>selectionForeground</key>
          <string>{UI.selection.fg}</string>
          <key>selectionBorder</key>
          <string>{Swatch.overlay1}</string>
          <key>activeLineBackground</key>
          <string>{UI.cursor_line.bg}</string>
          <key>activeSelectionBackground</key>
          <string>{UI.selection.bg}</string>
          <key>activeSelectionForeground</key>
          <string>{UI.selection.fg}</string>
          <key>activeSelectionBorder</key>
          <string>{Swatch.overlay1}</string>
          <key>activeGuide</key>
          <string>{Swatch.overlay1}</string>
          <key>bracketsForeground</key>
          <string>{Swatch.rosewater}</string>
          <key>bracketsBackground</key>
          <string></string>
          <key>bracketsOptions</key>
          <string>stippled underline</string>
          <key>bracketContentsForeground</key>
          <string>{Swatch.overlay1}</string>
          <key>bracketContentsBackground</key>
          <string></string>
          <key>bracketContentsOptions</key>
          <string>stippled underline</string>
          <key>tags</key>
          <string>{Swatch.overlay1}</string>
          <key>highlight</key>
          <string>{Swatch.rosewater}</string>
        </dict>
      </dict>
{scope_entries}
    </array>
  </dict>
</plist>
"""
    return {
        "content": content,
        "place": {
            "posix": Path.home() / ".config" / "bat" / "themes",
            "darwin": Path.home() / ".config" / "bat" / "themes",
            "windows": Path(os.getenv("APPDATA", Path.home() / "AppData" / "Roaming"))
            / "bat"
            / "themes",
        },
        "file": "franky.tmTheme",
    }
