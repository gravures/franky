# Franky Theme API Reference

## Theme TypedDict

```python
class Theme(TypedDict):
    content: str           # Full file content (f-string recommended)
    place: Place           # Per-platform install paths
    file: str              # Output filename
    doc: NotRequired[str]  # Post install hints (how to activate the theme)
```

## Place Dataclass

```python
@dataclass
class Place:
    posix: Path | None
    darwin: Path | None
    windows: Path | None

    def current(self) -> Path | None:
        """Returns theme install Path.

        Returns: a Path if theme is available on this platform, otherwise None.
        """
        ...
```

## Swatch Enum

Franky colour swatch. Values are hex strings.

```python
Swatch.rosewater     # "#f5e0dc"
Swatch.flamingo      # "#f2cdcd"
Swatch.pink          # "#fc8dc7"
Swatch.mauve         # "#cba6f7"
Swatch.red           # "#bb3831"
Swatch.maroon        # "#ba8d45"
Swatch.peach         # "#fab387"
Swatch.yellow        # "#ffdeaa"
Swatch.green         # "#57ab5a"
Swatch.teal          # "#94e2d5"
Swatch.sky           # "#539bf5"
Swatch.sapphire      # "#74c7ec"
Swatch.blue          # "#2764b1"
Swatch.lavender      # "#b4befe"

Swatch.text          # "#c9c9c9"  — default foreground
Swatch.base          # "#151524"  — default background
Swatch.subtext1      # "#b1b1b1"
Swatch.subtext0      # "#a6a596"
Swatch.overlay2      # "#909dab"
Swatch.overlay1      # "#7f849c"
Swatch.overlay0      # "#6f6b58"
Swatch.surface2      # "#54595f"
Swatch.surface1      # "#373e47"
Swatch.surface0      # "#2a2a3c"
Swatch.mantle        # "#110E17"
Swatch.crust         # "#0B090F"

Swatch.uv2           # "#521f9c"  — purple accent
Swatch.uv1           # "#340c6f"
Swatch.uv0           # "#09070D"

# Language highlighting colours
Swatch.lang_blue     # "#749fd4"
Swatch.lang_green    # "#569352"
Swatch.lang_yellow   # "#daaa3f"
Swatch.lang_pink     # "#ff938a"
Swatch.lang_red      # "#d85651"
Swatch.lang_purple   # "#977ebc"
```

## Ansi Enum

16 basic ANSI terminal colours, mapped from Swatch.

```python
Ansi.black, Ansi.red, Ansi.green, Ansi.yellow, Ansi.blue, Ansi.magenta, Ansi.cyan, Ansi.white
Ansi.bright_black, Ansi.bright_red, Ansi.bright_green, Ansi.bright_yellow
Ansi.bright_blue, Ansi.bright_magenta, Ansi.bright_cyan, Ansi.bright_white
```

## Mod Enum

```python
Mod.normal, Mod.bold, Mod.dim, Mod.italic
Mod.slow_blink, Mod.rapid_blink, Mod.reversed, Mod.hidden
Mod.crossed_out, Mod.underlined
```

Aliases: `Mod.bright = Mod.bold`, `Mod.inverted = Mod.reversed`, `Mod.strike_through = Mod.crossed_out`, `Mod.invisible = Mod.hidden`

## Style Dataclass

```python
@dataclass
class Style:
    fg: Swatch | None = None
    bg: Swatch | None = None
    mods: tuple[Mod, ...] = ()
    underline: Underline | None = None
```

## Underline Dataclass

```python
@dataclass
class Underline:
    color: Swatch | None = None
    style: Literal["line", "curl", "dashed", "dotted", "double_line"] = "line"
```

## Trans Function

Converts Catppuccin hex values to franky Swatch values:

```python
Trans("#f5e0dc")  # → Swatch.rosewater
Trans("#1e1e2e")  # → Swatch.base
```

Catppuccin mapping:
| Catppuccin | Franky |
|------------|--------|
| `#f5e0dc` | `rosewater` |
| `#f2cdcd` | `flamingo` |
| `#f5c2e7` | `pink` |
| `#cba6f7` | `mauve` |
| `#f38ba8` | `red` |
| `#eba0ac` | `maroon` |
| `#fab387` | `peach` |
| `#f9e2af` | `yellow` |
| `#a6e3a1` | `green` |
| `#94e2d5` | `teal` |
| `#89dceb` | `sky` |
| `#74c7ec` | `sapphire` |
| `#89b4fa` | `blue` |
| `#b4befe` | `lavender` |
| `#cdd6f4` | `text` |
| `#bac2de` | `subtext1` |
| `#a6adc8` | `subtext0` |
| `#9399b2` | `overlay2` |
| `#7f849c` | `overlay1` |
| `#6c7086` | `overlay0` |
| `#585b70` | `surface2` |
| `#45475a` | `surface1` |
| `#313244` | `surface0` |
| `#1e1e2e` | `base` |
| `#181825` | `mantle` |
| `#11111b` | `crust` |

## Lang Enum

Syntax highlighting styles. All values are `Style` or `(Swatch, ...)` tuples.

```python
# General
Lang.attribute, Lang.builtin, Lang.comment, Lang.constant
Lang.constructor, Lang.decorator, Lang.directive, Lang.escape
Lang.exception, Lang.function, Lang.macro, Lang.namespace
Lang.number, Lang.operator, Lang.punctuation, Lang.special
Lang.string, Lang.tag, Lang.type, Lang.variable

# Control flow
Lang.control, Lang.control_conditional, Lang.control_repeat
Lang.control_import, Lang.control_return, Lang.control_exception

# Keywords
Lang.keyword, Lang.keyword_operator, Lang.keyword_function
Lang.keyword_storage, Lang.keyword_storage_type, Lang.keyword_storage_modifier

# Functions
Lang.function_method, Lang.function_method_private, Lang.function_special

# Variables
Lang.variable_builtin, Lang.variable_parameter, Lang.variable_other
Lang.variable_other_member, Lang.variable_other_member_private

# Types
Lang.type_builtin, Lang.type_enum_member

# Punctuation
Lang.punctuation_bracket, Lang.punctuation_delimiter, Lang.punctuation_special

# Language colours (direct Swatch values)
Lang.lang_blue, Lang.lang_green, Lang.lang_yellow, Lang.lang_pink, Lang.lang_red, Lang.lang_purple
```

## UI Enum

UI element styles.

```python
UI.background, UI.background_separator, UI.tui_background
UI.cursor, UI.cursor_insert, UI.cursor_select, UI.cursor_match
UI.cursor_primary, UI.cursor_primary_insert, UI.cursor_primary_select
UI.cursor_line
UI.selection, UI.selection_primary
UI.ruler, UI.indent_guide, UI.inlay_hint, UI.wrap, UI.jump_label
UI.exc_name, UI.topline, UI.line_number, UI.line_number_select
UI.breakpoint, UI.breakpoint_active
UI.hint, UI.info, UI.warning, UI.error
UI.diagnostic_hint, UI.diagnostic_info, UI.diagnostic_warning, UI.diagnostic_error, UI.diagnostic_unnecessary
UI.diff_plus, UI.diff_minus, UI.diff_delta, UI.diff_delta_moved
UI.gutter, UI.gutter_selected
UI.status_line, UI.status_line_inactive, UI.status_line_normal, UI.status_line_insert, UI.status_line_select
UI.buffer_line, UI.buffer_line_active, UI.buffer_line_background
UI.scrollbar_track, UI.scrollbar_knob
```

## Markup Enum

Markup language styles (Markdown, HTML, etc.).

```python
Markup.markup, Markup.heading_marker
Markup.heading_1, Markup.heading_2, Markup.heading_3
Markup.heading_4, Markup.heading_5, Markup.heading_6
Markup.list_unnumbered, Markup.list_numbered
Markup.list_unchecked, Markup.list_checked
Markup.bold, Markup.italic, Markup.strike_through
Markup.link_url, Markup.link_label, Markup.link_text
Markup.quote
Markup.raw, Markup.raw_inline, Markup.raw_block
```

## Meta Enum

Special form styles.

```python
Meta.whitespace, Meta.caret, Meta.filename, Meta.filename_emphasis
```

## Generic Enum

Generic modifiers.

```python
Generic.deleted, Generic.emphasis, Generic.strong, Generic.emphasis_strong
```
