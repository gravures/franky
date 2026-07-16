---
name: franky-theme
description: |-
  Create new franky themes for target applications by mapping the franky color palette
  into application-specific config formats. Use for adding themes to src/franky/themes/.
  Use proactively when user asks to add a theme, create a theme for an app, or port
  catppuccin to a new application.

  Examples:
  - user: "Add a theme for kitty terminal" → create src/franky/themes/kitty.py with main()
  - user: "Create a theme for vscode" → create src/franky/themes/vscode.py with main()
  - user: "Port catppuccin to foot terminal" → create franky theme using Swatch mappings
  - user: "Add a zathura theme" → create src/franky/themes/zathura.py with main()
---

# Franky Theme Creator

## Overview

This skill guides creating new franky themes. Franky themes map a consistent color
palette into application-specific config file formats. The theme is a Python module
that exports `main() -> Theme` and generates the config content as a string.

## Step-by-Step Workflow

### 1. Research the target app

Find out:
- What config file format does it use? (key=value, TOML, JSON, JSONC, CSS, YAML, etc.)
- Where does it store theme/config files on each platform?
- Does the app have a catppuccin port already?

Search for the catppuccin port at `github.com/catppuccin/<appname>`. If it exists,
use it as a reference for how colors map to the app's config structure.

### 2. Find the catppuccin port's theme file

The catppuccin port repo will contain the mocha theme file (usually named
`catppuccin-mocha.toml` or similar). Study this file to understand:
- Which color names are used (e.g., `Rosewater`, `Red`, `Base`, etc.)
- How the app structures its color config (sections, nesting, key names)

Catppuccin mocha hex values (the source of truth):

```
Rosewater  #f5e0dc    Flamingo   #f2cdcd    Pink       #f5c2e7    Mauve      #cba6f7
Red        #f38ba8    Maroon     #eba0ac    Peach      #fab387    Yellow     #f9e2af
Green      #a6e3a1    Teal       #94e2d5    Sky        #89dceb    Sapphire   #74c7ec
Blue       #89b4fa    Lavender   #b4befe    Text       #cdd6f4    Subtext1   #bac2de
Subtext0   #a6adc8    Overlay2   #9399b2    Overlay1   #7f849c    Overlay0   #6c7086
Surface2   #585b70    Surface1   #45475a    Surface0   #313244    Base       #1e1e2e
Mantle     #181825    Crust      #11111b
```

### 3. Map catppuccin colors to franky Swatch

Use `Trans()` from `franky.theme` to translate catppuccin hex → franky Swatch name.
The mapping is defined in `src/franky/theme.py:Trans()`:

```python
from franky.theme import Trans

# Trans("#f5e0dc") returns Swatch.rosewater
# Trans("#1e1e2e") returns Swatch.base
# Trans("#cdd6f4") returns Swatch.text
```

For colors that don't map directly (e.g., app-specific accent colors), use
franky's extended Swatch values: `lang_blue`, `lang_green`, `lang_yellow`,
`lang_pink`, `lang_red`, `lang_purple`, `uv0`, `uv1`, `uv2`.

### 4. Determine which franky enums to import

Choose based on what the app supports:

| App supports | Import |
|-------------|--------|
| Only ANSI 16 colors | `Ansi`, `Swatch` |
| ANSI + cursor/selection | `UI`, `Ansi`, `Swatch` |
| Full syntax highlighting | `UI`, `Lang`, `Markup`, `Meta`, `Generic`, `Mod`, `Style`, `Swatch` |

**IMPORTANT**: For syntax highlighting, you MUST use semantic enums (`Lang`, `UI`, `Meta`, `Generic`, `Markup`) instead of raw `Swatch` values. These enums define the MEANING of code elements (e.g., `Lang.string` = string color, `Lang.keyword_operator` = operator color), not just colors.

Reference: `src/franky/themes/helix.py` is the canonical example of proper enum usage.

### 5. Study existing themes for scope mapping patterns

Before writing a new theme with syntax highlighting, **always study existing themes**:

1. **Read `src/franky/themes/helix.py`** - This is the reference implementation for complex syntax highlighting. Note how it maps TextMate scopes to semantic enums.

2. **Key mappings to remember**:
   - `keyword.operator` → `Lang.keyword_operator` (NOT `Lang.operator`)
   - `keyword.storage.type` → `Lang.keyword_storage_type`
   - `keyword.storage.modifier` → `Lang.keyword_storage_modifier`
   - `punctuation.special` → `Lang.punctuation_special`
   - `entity.name.function.method.private` → `Lang.function_method_private`
   - `variable.other.member.private` → `Lang.variable_other_member_private`
   - `special` (fuzzy highlight) → `Lang.special`

3. **Scope specificity matters**: Some scopes are language-specific:
   - `comment.documentation` may catch Python docstrings (use `comment.block.documentation` instead)
   - `string.quoted.docstring` is Python-specific
   - Always check if a scope needs language suffix (e.g., `.python`, `.js`)

### 6. Write the theme module

Create `src/franky/themes/<appname>.py` with this structure:

```python
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
"""<Appname> Franky theme."""

from __future__ import annotations

import os
from pathlib import Path

from franky import <needed imports>, Theme


def format(style: Style) -> str:  # noqa: A001
    # Convert Style to app's config syntax
    ...


def main() -> Theme:
    return {
        "content": f"""...""",
        "place": {
            "posix": Path.home() / ".config" / "<app>" / "<subdir>",
            "darwin": Path.home() / ".config" / "<app>" / "<subdir>",
            "windows": Path(os.getenv("APPDATA", Path.home() / "AppData" / "Roaming"))
            / "<app>" / "<subdir>",
        },
        "file": "<filename>.<ext>",
    }
```

### 6. Write the format() helper

The `format()` function serializes `Style` objects into the app's config syntax.
Style has: `fg` (Swatch|None), `bg` (Swatch|None), `mods` (tuple[Mod,...]),
`underline` (Underline|None).

**Key=value format** (ghostty-style) — no format() needed, use f-strings directly:
```python
background = {Swatch.mantle}
foreground = {Swatch.text}
```

**TOML format** (helix-style):
```python
def format(style: Style) -> str:
    mods = tuple(f'"{m.value}"' for m in filter(lambda m: m is not Mod.underlined, style.mods))
    underline = None
    if style.underline:
        color = f'color = "{style.underline.color}", ' if style.underline.color else ""
        underline = f'underline = {{ {color}style = "{style.underline.style}" }}'
    formatted = filter(None, (
        f'fg = "{style.fg}"' if style.fg else None,
        f'bg = "{style.bg}"' if style.bg else None,
        f"modifiers = [{', '.join(mods)}]" if mods else None,
        underline,
    ))
    return f"{{ {', '.join(formatted)} }}" if formatted else ""
```

**Space-separated format** (qman-style):
```python
def format(style: Style) -> str:
    return "   ".join((
        f"{style.fg}" if style.fg else f"{Swatch.text}",
        f"{style.bg}" if style.bg else f"{Swatch.mantle}",
        "true" if Mod.bold in style.mods else "false",
    ))
```

**JSON format**:
```python
import json

def format(style: Style) -> str:
    d = {}
    if style.fg: d["foreground"] = f"#{style.fg.value}"
    if style.bg: d["background"] = f"#{style.bg.value}"
    if style.mods: d["fontStyle"] = " ".join(m.value for m in style.mods)
    return json.dumps(d, indent=2)
```

### 7. Set the place dict

Platform-specific install paths. Set to `None` if unsupported.

Common patterns:
- Terminal emulators: `Path.home() / ".config" / "<app>" / "themes"`
- Editors: `Path.home() / ".config" / "<app>" / "themes"` or `.../colors`
- Windows: `Path(os.getenv("APPDATA", Path.home() / "AppData" / "Roaming")) / "<app>" / "themes"`

### 8. Write the content string

Use f-strings to compose the config. Map each app config key to a franky style:

```python
# For a key=value app with ANSI colors + UI elements:
content = f"""
palette = 0={Ansi.black}
palette = 1={Ansi.red}
...
background = {Swatch.mantle}
foreground = {Swatch.text}
cursor-text = {UI.cursor.fg}
cursor-color = {UI.cursor.bg}
selection-background = {UI.selection.bg}
selection-foreground = {UI.selection.fg}
"""
```

For apps with syntax highlighting, map the app's highlight keys to `Lang.*`,
`Markup.*`, and `UI.*` enums using your `format()` helper.

### 9. Validate and test

**Step 1: Lint and typecheck**
```bash
mise run lint src/franky/themes/<appname>.py
mise run typecheck src/franky/themes/<appname>.py
```

**Step 2: Verify XML/format validity** (for XML-based themes)
```python
import xml.etree.ElementTree as ET
from franky.themes.<appname> import main
t = main()
try:
    root = ET.fromstring(t['content'])
    print('XML is valid')
except ET.ParseError as e:
    print(f'XML parse error: {e}')
```

**Step 3: Install and test with actual output**
```bash
franky install <appname> -y
# For bat: bat cache --build
# Test with a file containing various syntax elements
echo 'def hello():
    """Docstring."""
    print("Hello")' | <app> --theme=franky --language=python
```

**Step 4: Verify colors are correct**
Check that:
- Comments are grey (not blue like strings)
- Strings are blue (not grey like comments)
- Keywords are red
- Functions are purple
- Types are italic
- Docstrings are strings (blue), not comments (grey)

## Creating Custom Styles

Use `Style(fg, bg, mods, underline)` for ad-hoc styles not covered by enums:

```python
Style(Swatch.lang_purple, Swatch.mantle)           # fg + bg
Style(Swatch.pink, Swatch.mantle, (Mod.bold,))     # with modifier
Style(Swatch.sky, UI.status_line.bg)                # use UI enum as base
```

## Common Pitfalls

1. **Wrong operator mapping**: `keyword.operator` should use `Lang.keyword_operator`, NOT `Lang.operator`. The `Lang.operator` is for assignment operators only.

2. **Missing enum members**: Always check all available members in `Lang`, `UI`, `Meta`, `Generic`, `Markup` enums. Common missing ones:
   - `Lang.function_method_private`
   - `Lang.variable_other_member_private`
   - `Lang.special` (fuzzy highlight)
   - `Lang.punctuation_special`

3. **Scope specificity**: TextMate scopes can be language-specific:
   - `comment.documentation` catches Python docstrings → use `comment.block.documentation`
   - `string.quoted.docstring` is Python-specific
   - Always test with actual files to verify scope matching

4. **Line length issues**: Use data-driven approach with `_SCOPES` list to avoid E501 errors:
   ```python
   _SCOPES: list[tuple[str, str, Style]] = [
       ("Name", "scope", Style),
       ...
   ]

   def main() -> Theme:
       scope_entries = "\n".join(itertools.starmap(_entry, _SCOPES))
   ```

5. **XML escaping**: Escape `&` as `&amp;` in scope names and strings for XML-based formats.

6. **Verification**: Always test with actual files to verify colors are correct. Check that:
   - Comments are grey
   - Strings are blue
   - Keywords are red
   - Functions are purple
   - Docstrings are strings (blue), not comments (grey)

## References

- **`src/franky/themes/helix.py`** - Reference implementation for complex syntax highlighting
- **`src/franky/theme.py`** - Full API with all enums (`Lang`, `UI`, `Meta`, `Generic`, `Markup`, `Mod`, `Style`, `Swatch`)
- Load `references/theme-api.md` for the full theme.py API
- Catppuccin palette: `github.com/catppuccin/palette` — palette.json has all hex values
- Catppuccin ports: `github.com/catppuccin/<appname>` — each port has mocha theme file
