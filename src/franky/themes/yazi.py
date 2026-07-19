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
"""Yazi Franky theme."""

from __future__ import annotations

import os
from pathlib import Path
from typing import cast

from franky import UI, Meta, Mod, Style, Swatch, Theme
from franky.theme import Place
from franky.themes.bat import main as bat


def format(style: Style) -> str:  # noqa: A001
    mods = style.mods
    parts = list(
        filter(
            None,
            (
                f'fg = "{style.fg}"' if style.fg else None,
                f'bg = "{style.bg}"' if style.bg else None,
                "bold = true" if Mod.bold in mods else None,
                "italic = true" if Mod.italic in mods else None,
                "underline = true" if Mod.underlined in mods else None,
                "dim = true" if Mod.dim in mods else None,
                "reversed = true" if Mod.reversed in mods else None,
                "crossed = true" if Mod.crossed_out in mods else None,
            ),
        )
    )
    if parts:
        return "{" + ", ".join(parts) + "}"
    return "{}"


ARCHIVES_MIME = (
    "application/{zip,rar,7z*,tar,gzip,xz,zstd,bzip*,lzma,compress,archive,cpio,arj,xar,ms-cab*}"
)

bat_ = bat()
syntect_theme = str(cast("Path", bat_["place"].current()) / bat_["file"])

PLACE = Place(
    posix=Path.home() / ".config" / "yazi" / "flavors" / "franky.yazi",
    darwin=Path.home() / ".config" / "yazi" / "flavors" / "franky.yazi",
    windows=Path(os.getenv("APPDATA", Path.home() / "AppData" / "Roaming"))
    / "yazi"
    / "flavors"
    / "franky.yazi",
)


def main() -> Theme:
    return {
        "content": f"""# Author: Franky Theme <https://github.com/gravures/franky>
# License: GPL-3.0
# Franky - A GitHub-Dark-inspired coding palette fused with the UI flavor of Catppuccin-Mocha

[app]
overall = {{ bg = "{UI.background.bg}" }}

[mgr]
cwd = {format(UI.buffer_line_active)}
find_keyword  = {format(Style(Swatch.yellow, mods=(Mod.italic,)))}
find_position = {format(Style(Swatch.pink, mods=(Mod.italic,)))}
marker_copied   = {format(Style(Swatch.green, Swatch.green))}
marker_cut      = {format(Style(Swatch.red, Swatch.red))}
marker_marked   = {format(Style(Swatch.teal, Swatch.teal))}
marker_selected = {format(Style(Swatch.mauve, Swatch.maroon))}
count_copied   = {format(Style(Swatch.base, Swatch.green, (Mod.bold,)))}
count_cut      = {format(Style(Swatch.base, Swatch.red, (Mod.bold,)))}
count_selected = {format(Style(Swatch.base, Swatch.maroon, (Mod.bold,)))}
border_symbol = "│"
border_style  = {format(UI.indent_guide)}

[tabs]
active   = {format(Style(Swatch.rosewater, Swatch.uv1))}
inactive = {format(Style(Swatch.subtext0, Swatch.uv0))}
sep_inner  = {{ open = "", close = "" }}
sep_outer = {{ open = "", close = "" }}

[mode]
normal_main = {format(UI.status_line_normal)}
normal_alt  = {format(Style(UI.status_line_normal.bg, UI.status_line_normal.fg))}
select_main = {format(UI.status_line_select)}
select_alt  = {format(Style(UI.status_line_select.bg, UI.status_line_select.fg))}
unset_main  = {format(UI.status_line_insert)}
unset_alt   = {format(Style(UI.status_line_insert.bg, UI.status_line_insert.fg))}

[indicator]
parent = {format(Style(bg=Swatch.uv1, fg=Swatch.text))}
current = {format(Style(bg=Swatch.uv1, fg=Swatch.text))}
preview = {format(Style(bg=UI.cursor_line.bg))}

[status]
overall = {format(UI.status_line)}
sep_left  = {{ open = "", close = "" }}
sep_right = {{ open = "", close = "" }}
progress_label  = {format(Style(Swatch.text, mods=(Mod.bold,)))}
progress_normal = {format(UI.status_line_insert)}
progress_error  = {format(UI.error)}
perm_type  = {format(Style(Meta.filename.fg))}
perm_read  = {format(Style(Swatch.yellow))}
perm_write = {format(Style(Swatch.pink))}
perm_exec  = {format(Style(Swatch.teal))}
perm_sep   = {format(UI.background_separator)}

[input]
border   = {format(Style(Swatch.mauve))}
title    = {{}}
value    = {{}}
selected = {format(UI.selection)}

[pick]
border   = {format(Style(Swatch.mauve))}
active   = {format(Style(Swatch.pink))}
inactive = {{}}

[confirm]
border     = {format(Style(Swatch.mauve))}
title      = {format(Style(Swatch.mauve))}
body       = {{}}
list       = {{}}
btn_yes    = {format(UI.selection)}
btn_no     = {{}}

[cmp]
border = {format(Style(Swatch.mauve))}

[tasks]
border  = {format(Style(Swatch.mauve))}
title   = {{}}
hovered = {format(UI.cursor_line)}

[which]
mask            = {format(UI.selection)}
cand            = {format(UI.hint)}
rest            = {format(UI.buffer_line)}
desc            = {format(Style(Swatch.pink))}
separator       = " → "
separator_style = {format(UI.background_separator)}

[help]
on      = {format(Style(Swatch.teal))}
run     = {format(Style(Swatch.mauve))}
desc    = {format(Style(Swatch.text))}
hovered = {format(UI.cursor_line)}
footer  = {format(UI.status_line)}

[notify]
title_info  = {format(UI.info)}
title_warn  = {format(UI.warning)}
title_error = {format(UI.error)}

[spot]
border = {format(UI.popup_border)}
title  = {format(UI.popup)}
tbl_cell = {format(Style(Swatch.mauve, mods=(Mod.reversed,)))}
tbl_col = {format(Style(mods=(Mod.bold,)))}


[filetype]
rules = [
# Media
{{ mime = "image/*", fg = "{Swatch.yellow}" }},
{{ mime = "{{audio,video}}/*", fg = "{Swatch.pink}" }},

# Archives
{{ mime = "{ARCHIVES_MIME}", fg = "{Swatch.red}" }},

# Documents
{{ mime = "application/{{pdf,doc,rtf}}", fg = "{Swatch.sky}" }},

# Virtual file system
{{ mime = "vfs/{{absent,stale}}", fg = "{Swatch.surface1}" }},

# Special file
{{ url = "*", is = "orphan", bg = "{Swatch.red}" }},
{{ url = "*", is = "exec"  , fg = "{Swatch.green}" }},

# Dummy file
{{ url = "*", is = "dummy", bg = "{Swatch.red}" }},
{{ url = "*/", is = "dummy", bg = "{Swatch.red}" }},

# Fallback
{{ url = "*/", fg = "{Meta.filename.fg}" }},
]

[icon]
dirs = [
{{ name = ".config", text = "", fg = "{Meta.filename.fg}" }},
{{ name = ".git", text = "", fg = "{Meta.filename.fg}" }},
{{ name = ".github", text = "", fg = "{Meta.filename.fg}" }},
{{ name = ".npm", text = "", fg = "{Meta.filename.fg}" }},
{{ name = "Desktop", text = "", fg = "{Meta.filename.fg}" }},
{{ name = "Development", text = "", fg = "{Meta.filename.fg}" }},
{{ name = "Documents", text = "", fg = "{Meta.filename.fg}" }},
{{ name = "Downloads", text = "", fg = "{Meta.filename.fg}" }},
{{ name = "Library", text = "", fg = "{Meta.filename.fg}" }},
{{ name = "Movies", text = "", fg = "{Meta.filename.fg}" }},
{{ name = "Music", text = "", fg = "{Meta.filename.fg}" }},
{{ name = "Pictures", text = "", fg = "{Meta.filename.fg}" }},
{{ name = "Public", text = "", fg = "{Meta.filename.fg}" }},
{{ name = "Videos", text = "", fg = "{Meta.filename.fg}" }},
]
conds = [
{{ if = "orphan", text = "", fg = "{Swatch.text}" }},
{{ if = "link", text = "", fg = "{Swatch.subtext0}" }},
{{ if = "block", text = "", fg = "{Swatch.yellow}" }},
{{ if = "char", text = "", fg = "{Swatch.yellow}" }},
{{ if = "fifo", text = "", fg = "{Swatch.yellow}" }},
{{ if = "sock", text = "", fg = "{Swatch.yellow}" }},
{{ if = "sticky", text = "", fg = "{Swatch.yellow}" }},
{{ if = "dummy", text = "", fg = "{Swatch.red}" }},
{{ if = "dir", text = "", fg = "{Meta.filename.fg}" }},
{{ if = "exec", text = "", fg = "{Swatch.green}" }},
{{ if = "!dir", text = "", fg = "{Swatch.text}" }},
]

files = [
{{ name = "eslint.config.cjs", text = "", fg = "{Swatch.surface2}" }},
{{ name = "hyprlandd.conf", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "settings.gradle", text = "", fg = "{Swatch.surface2}" }},
{{ name = "PrusaSlicerGcodeViewer.ini", text = "", fg = "{Swatch.peach}" }},
{{ name = ".nvmrc", text = "", fg = "{Swatch.green}" }},
{{ name = ".gitmodules", text = "", fg = "{Swatch.peach}" }},
{{ name = "tailwind.config.ts", text = "󱏿", fg = "{Swatch.sapphire}" }},
{{ name = "bun.lockb", text = "", fg = "{Swatch.rosewater}" }},
{{ name = ".npmignore", text = "", fg = "{Swatch.red}" }},
{{ name = "wrangler.jsonc", text = "", fg = "{Swatch.peach}" }},
{{ name = ".prettierrc.toml", text = "", fg = "{Swatch.blue}" }},
{{ name = ".zshenv", text = "", fg = "{Swatch.green}" }},
{{ name = "code_of_conduct", text = "", fg = "{Swatch.red}" }},
{{ name = ".Xauthority", text = "", fg = "{Swatch.peach}" }},
{{ name = "gradle-wrapper.properties", text = "", fg = "{Swatch.surface2}" }},
{{ name = ".clang-tidy", text = "", fg = "{Swatch.overlay1}" }},
{{ name = ".prettierrc.cjs", text = "", fg = "{Swatch.blue}" }},
{{ name = ".clangd", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "playwright.config.js", text = "", fg = "{Swatch.green}" }},
{{ name = ".Xresources", text = "", fg = "{Swatch.peach}" }},
{{ name = "weston.ini", text = "", fg = "{Swatch.yellow}" }},
{{ name = "vite.config.mts", text = "", fg = "{Swatch.peach}" }},
{{ name = "vercel.json", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "docker-compose.yaml", text = "󰡨", fg = "{Swatch.blue}" }},
{{ name = "compose.yaml", text = "󰡨", fg = "{Swatch.blue}" }},
{{ name = "build", text = "", fg = "{Swatch.green}" }},
{{ name = ".luaurc", text = "", fg = "{Swatch.blue}" }},
{{ name = "AUTHORS.txt", text = "", fg = "{Swatch.mauve}" }},
{{ name = "pnpm-lock.yaml", text = "", fg = "{Swatch.peach}" }},
{{ name = ".codespellrc", text = "󰓆", fg = "{Swatch.green}" }},
{{ name = "mix.lock", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "hyprlock.conf", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "bspwmrc", text = "", fg = "{Swatch.surface0}" }},
{{ name = ".prettierrc.json5", text = "", fg = "{Swatch.blue}" }},
{{ name = "license.md", text = "", fg = "{Swatch.yellow}" }},
{{ name = ".prettierignore", text = "", fg = "{Swatch.blue}" }},
{{ name = "fp-info-cache", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "kdeglobals", text = "", fg = "{Swatch.blue}" }},
{{ name = ".zshrc", text = "", fg = "{Swatch.green}" }},
{{ name = "webpack", text = "󰜫", fg = "{Swatch.sapphire}" }},
{{ name = "checkhealth", text = "󰓙", fg = "{Swatch.blue}" }},
{{ name = ".npmrc", text = "", fg = "{Swatch.red}" }},
{{ name = "PKGBUILD", text = "", fg = "{Swatch.blue}" }},
{{ name = ".prettierrc.yml", text = "", fg = "{Swatch.blue}" }},
{{ name = "commit_editmsg", text = "", fg = "{Swatch.peach}" }},
{{ name = ".gitattributes", text = "", fg = "{Swatch.peach}" }},
{{ name = ".vimrc", text = "", fg = "{Swatch.green}" }},
{{ name = "xsettingsd.conf", text = "", fg = "{Swatch.peach}" }},
{{ name = "gruntfile.babel.js", text = "", fg = "{Swatch.peach}" }},
{{ name = "xorg.conf", text = "", fg = "{Swatch.peach}" }},
{{ name = "xmonad.hs", text = "", fg = "{Swatch.red}" }},
{{ name = "xmobarrc.hs", text = "", fg = "{Swatch.red}" }},
{{ name = "rakefile", text = "", fg = "{Swatch.surface0}" }},
{{ name = "vite.config.mjs", text = "", fg = "{Swatch.peach}" }},
{{ name = "xdph.conf", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "wrangler.toml", text = "", fg = "{Swatch.peach}" }},
{{ name = ".babelrc", text = "", fg = "{Swatch.yellow}" }},
{{ name = "AUTHORS", text = "", fg = "{Swatch.mauve}" }},
{{ name = "lxde-rc.xml", text = "", fg = "{Swatch.overlay2}" }},
{{ name = "vlcrc", text = "󰕼", fg = "{Swatch.peach}" }},
{{ name = "vitest.config.ts", text = "", fg = "{Swatch.green}" }},
{{ name = "prisma.config.mts", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "vitest.config.mts", text = "", fg = "{Swatch.green}" }},
{{ name = ".env", text = "", fg = "{Swatch.yellow}" }},
{{ name = "vitest.config.mjs", text = "", fg = "{Swatch.green}" }},
{{ name = ".condarc", text = "", fg = "{Swatch.green}" }},
{{ name = ".pre-commit-config.yaml", text = "󰛢", fg = "{Swatch.peach}" }},
{{ name = "_vimrc", text = "", fg = "{Swatch.green}" }},
{{ name = "vitest.config.cts", text = "", fg = "{Swatch.green}" }},
{{ name = "vitest.config.cjs", text = "", fg = "{Swatch.green}" }},
{{ name = "PrusaSlicer.ini", text = "", fg = "{Swatch.peach}" }},
{{ name = "vite.config.ts", text = "", fg = "{Swatch.peach}" }},
{{ name = "xmobarrc", text = "", fg = "{Swatch.red}" }},
{{ name = ".editorconfig", text = "", fg = "{Swatch.rosewater}" }},
{{ name = ".xinitrc", text = "", fg = "{Swatch.peach}" }},
{{ name = "vite.config.cts", text = "", fg = "{Swatch.peach}" }},
{{ name = "prettier.config.mjs", text = "", fg = "{Swatch.blue}" }},
{{ name = "vite.config.cjs", text = "", fg = "{Swatch.peach}" }},
{{ name = "ext_typoscript_setup.txt", text = "", fg = "{Swatch.peach}" }},
{{ name = ".prettierrc", text = "", fg = "{Swatch.blue}" }},
{{ name = "hypridle.conf", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "containerfile", text = "󰡨", fg = "{Swatch.blue}" }},
{{ name = "vagrantfile", text = "", fg = "{Swatch.overlay0}" }},
{{ name = ".gitlab-ci.yml", text = "", fg = "{Swatch.peach}" }},
{{ name = ".gtkrc-2.0", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "unlicense", text = "", fg = "{Swatch.yellow}" }},
{{ name = "tsconfig.json", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "tmux.conf.local", text = "", fg = "{Swatch.green}" }},
{{ name = "justfile", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "readme.md", text = "󰂺", fg = "{Swatch.rosewater}" }},
{{ name = "tailwind.config.js", text = "󱏿", fg = "{Swatch.sapphire}" }},
{{ name = "license", text = "", fg = "{Swatch.yellow}" }},
{{ name = "sym-lib-table", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "sxhkdrc", text = "", fg = "{Swatch.surface0}" }},
{{ name = ".gvimrc", text = "", fg = "{Swatch.green}" }},
{{ name = ".SRCINFO", text = "󰣇", fg = "{Swatch.blue}" }},
{{ name = "svelte.config.js", text = "", fg = "{Swatch.peach}" }},
{{ name = "security.md", text = "󰒃", fg = "{Swatch.subtext1}" }},
{{ name = "Directory.Build.targets", text = "", fg = "{Swatch.blue}" }},
{{ name = "i3status.conf", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "cmakelists.txt", text = "", fg = "{Swatch.text}" }},
{{ name = "robots.txt", text = "󰚩", fg = "{Swatch.overlay0}" }},
{{ name = "gulpfile.ts", text = "", fg = "{Swatch.red}" }},
{{ name = ".dockerignore", text = "󰡨", fg = "{Swatch.blue}" }},
{{ name = "rmd", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "nuxt.config.ts", text = "󱄆", fg = "{Swatch.green}" }},
{{ name = "gruntfile.js", text = "", fg = "{Swatch.peach}" }},
{{ name = "prisma.config.ts", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "cantorrc", text = "", fg = "{Swatch.blue}" }},
{{ name = "tailwind.config.mjs", text = "󱏿", fg = "{Swatch.sapphire}" }},
{{ name = "hyprsunset.conf", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "readme", text = "󰂺", fg = "{Swatch.rosewater}" }},
{{ name = "py.typed", text = "", fg = "{Swatch.yellow}" }},
{{ name = "procfile", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "eslint.config.ts", text = "", fg = "{Swatch.surface2}" }},
{{ name = "ionic.config.json", text = "", fg = "{Swatch.blue}" }},
{{ name = "prettier.config.ts", text = "", fg = "{Swatch.blue}" }},
{{ name = "index.theme", text = "", fg = "{Swatch.green}" }},
{{ name = "prettier.config.cjs", text = "", fg = "{Swatch.blue}" }},
{{ name = "pom.xml", text = "", fg = "{Swatch.surface0}" }},
{{ name = "gruntfile.ts", text = "", fg = "{Swatch.peach}" }},
{{ name = "package-lock.json", text = "", fg = "{Swatch.surface0}" }},
{{ name = "gtkrc", text = "", fg = "{Swatch.rosewater}" }},
{{ name = ".xsession", text = "", fg = "{Swatch.peach}" }},
{{ name = "Directory.Packages.props", text = "", fg = "{Swatch.blue}" }},
{{ name = "brewfile", text = "", fg = "{Swatch.surface0}" }},
{{ name = "playwright.config.mts", text = "", fg = "{Swatch.green}" }},
{{ name = "bun.lock", text = "", fg = "{Swatch.rosewater}" }},
{{ name = ".justfile", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "playwright.config.mjs", text = "", fg = "{Swatch.green}" }},
{{ name = ".prettierrc.js", text = "", fg = "{Swatch.blue}" }},
{{ name = ".gitconfig", text = "", fg = "{Swatch.peach}" }},
{{ name = "kalgebrarc", text = "", fg = "{Swatch.blue}" }},
{{ name = "nuxt.config.mjs", text = "󱄆", fg = "{Swatch.green}" }},
{{ name = "platformio.ini", text = "", fg = "{Swatch.peach}" }},
{{ name = ".bash_profile", text = "", fg = "{Swatch.green}" }},
{{ name = "build.gradle", text = "", fg = "{Swatch.surface2}" }},
{{ name = "package.json", text = "", fg = "{Swatch.red}" }},
{{ name = "playwright.config.ts", text = "", fg = "{Swatch.green}" }},
{{ name = "next.config.js", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "nuxt.config.js", text = "󱄆", fg = "{Swatch.green}" }},
{{ name = ".git-blame-ignore-revs", text = "", fg = "{Swatch.peach}" }},
{{ name = "node_modules", text = "", fg = "{Swatch.red}" }},
{{ name = "next.config.ts", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "go.mod", text = "", fg = "{Swatch.sapphire}" }},
{{ name = ".settings.json", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "favicon.ico", text = "", fg = "{Swatch.yellow}" }},
{{ name = "kdenliverc", text = "", fg = "{Swatch.blue}" }},
{{ name = "makefile", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "prettier.config.js", text = "", fg = "{Swatch.blue}" }},
{{ name = "kritarc", text = "", fg = "{Swatch.mauve}" }},
{{ name = "kritadisplayrc", text = "", fg = "{Swatch.mauve}" }},
{{ name = "mpv.conf", text = "", fg = "{Swatch.base}" }},
{{ name = "kdenlive-layoutsrc", text = "", fg = "{Swatch.blue}" }},
{{ name = "playwright.config.cjs", text = "", fg = "{Swatch.green}" }},
{{ name = "tmux.conf", text = "", fg = "{Swatch.green}" }},
{{ name = ".zprofile", text = "", fg = "{Swatch.green}" }},
{{ name = "lxqt.conf", text = "", fg = "{Swatch.blue}" }},
{{ name = ".mailmap", text = "󰊢", fg = "{Swatch.peach}" }},
{{ name = "security", text = "󰒃", fg = "{Swatch.subtext1}" }},
{{ name = "go.sum", text = "", fg = "{Swatch.sapphire}" }},
{{ name = ".prettierrc.json", text = "", fg = "{Swatch.blue}" }},
{{ name = "config", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "FreeCAD.conf", text = "", fg = "{Swatch.red}" }},
{{ name = "i3blocks.conf", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "commitlint.config.js", text = "󰜘", fg = "{Swatch.teal}" }},
{{ name = "i18n.config.js", text = "󰗊", fg = "{Swatch.overlay1}" }},
{{ name = ".pnpmfile.cjs", text = "", fg = "{Swatch.peach}" }},
{{ name = ".luacheckrc", text = "", fg = "{Swatch.blue}" }},
{{ name = "vitest.config.js", text = "", fg = "{Swatch.green}" }},
{{ name = "code_of_conduct.md", text = "", fg = "{Swatch.red}" }},
{{ name = "hyprland.conf", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "dune", text = "", fg = "{Swatch.surface1}" }},
{{ name = "_gvimrc", text = "", fg = "{Swatch.green}" }},
{{ name = "Directory.Build.props", text = "", fg = "{Swatch.blue}" }},
{{ name = "gradlew", text = "", fg = "{Swatch.surface2}" }},
{{ name = "gulpfile.coffee", text = "", fg = "{Swatch.red}" }},
{{ name = "gulpfile.babel.js", text = "", fg = "{Swatch.red}" }},
{{ name = "pnpm-workspace.yaml", text = "", fg = "{Swatch.peach}" }},
{{ name = "eslint.config.js", text = "", fg = "{Swatch.surface2}" }},
{{ name = "dockerfile", text = "󰡨", fg = "{Swatch.blue}" }},
{{ name = "groovy", text = "", fg = "{Swatch.surface2}" }},
{{ name = ".gitignore", text = "", fg = "{Swatch.peach}" }},
{{ name = ".bashrc", text = "", fg = "{Swatch.green}" }},
{{ name = "gulpfile.js", text = "", fg = "{Swatch.red}" }},
{{ name = "gruntfile.coffee", text = "", fg = "{Swatch.peach}" }},
{{ name = "go.work", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "next.config.cjs", text = "", fg = "{Swatch.rosewater}" }},
{{ name = ".eslintrc", text = "", fg = "{Swatch.surface2}" }},
{{ name = "commitlint.config.ts", text = "󰜘", fg = "{Swatch.teal}" }},
{{ name = "compose.yml", text = "󰡨", fg = "{Swatch.blue}" }},
{{ name = "eslint.config.mjs", text = "", fg = "{Swatch.surface2}" }},
{{ name = "gradle.properties", text = "", fg = "{Swatch.surface2}" }},
{{ name = ".clang-format", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "docker-compose.yml", text = "󰡨", fg = "{Swatch.blue}" }},
{{ name = "copying.lesser", text = "", fg = "{Swatch.yellow}" }},
{{ name = "copying", text = "", fg = "{Swatch.yellow}" }},
{{ name = "fp-lib-table", text = "", fg = "{Swatch.rosewater}" }},
{{ name = ".nuxtrc", text = "󱄆", fg = "{Swatch.green}" }},
{{ name = "gnumakefile", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "i18n.config.ts", text = "󰗊", fg = "{Swatch.overlay1}" }},
{{ name = ".pylintrc", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "build.zig.zon", text = "", fg = "{Swatch.peach}" }},
{{ name = ".prettierrc.mjs", text = "", fg = "{Swatch.blue}" }},
{{ name = "hyprpaper.conf", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "QtProject.conf", text = "", fg = "{Swatch.green}" }},
{{ name = ".ds_store", text = "", fg = "{Swatch.surface1}" }},
{{ name = "Jenkinsfile", text = "", fg = "{Swatch.red}" }},
{{ name = "Gemfile", text = "", fg = "{Swatch.surface0}" }},
{{ name = "workspace", text = "", fg = "{Swatch.green}" }},
{{ name = "vite.config.js", text = "", fg = "{Swatch.peach}" }},
{{ name = ".nanorc", text = "", fg = "{Swatch.surface0}" }},
{{ name = ".prettierrc.yaml", text = "", fg = "{Swatch.blue}" }},
{{ name = "bitbucket-pipelines.yml", text = "󰂨", fg = "{Swatch.blue}" }},
{{ name = "playwright.config.cts", text = "", fg = "{Swatch.green}" }},
{{ name = "nuxt.config.cjs", text = "󱄆", fg = "{Swatch.green}" }},
{{ name = ".eslintignore", text = "", fg = "{Swatch.surface2}" }},
]
exts = [
{{ name = "txt", text = "󰈙", fg = "{Swatch.green}" }},
{{ name = "kicad_dru", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "cbl", text = "", fg = "{Swatch.surface2}" }},
{{ name = "mpp", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "cljc", text = "", fg = "{Swatch.green}" }},
{{ name = "jsonl", text = "", fg = "{Swatch.yellow}" }},
{{ name = "exs", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "liquid", text = "", fg = "{Swatch.green}" }},
{{ name = "vue", text = "", fg = "{Swatch.green}" }},
{{ name = "hrl", text = "", fg = "{Swatch.red}" }},
{{ name = "app", text = "", fg = "{Swatch.surface1}" }},
{{ name = "stories.vue", text = "", fg = "{Swatch.red}" }},
{{ name = "avi", text = "", fg = "{Swatch.peach}" }},
{{ name = "makefile", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "hpp", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "ino", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "drl", text = "", fg = "{Swatch.maroon}" }},
{{ name = "epp", text = "", fg = "{Swatch.peach}" }},
{{ name = "gv", text = "󱁉", fg = "{Swatch.surface2}" }},
{{ name = "cpp", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "stories.jsx", text = "", fg = "{Swatch.red}" }},
{{ name = "git", text = "", fg = "{Swatch.peach}" }},
{{ name = "tgz", text = "", fg = "{Swatch.peach}" }},
{{ name = "ical", text = "", fg = "{Swatch.surface0}" }},
{{ name = "R", text = "󰟔", fg = "{Swatch.overlay0}" }},
{{ name = "ogv", text = "", fg = "{Swatch.peach}" }},
{{ name = "strings", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "bmp", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "styl", text = "", fg = "{Swatch.green}" }},
{{ name = "ex", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "d", text = "", fg = "{Swatch.red}" }},
{{ name = "c", text = "", fg = "{Swatch.blue}" }},
{{ name = "huff", text = "󰡘", fg = "{Swatch.surface2}" }},
{{ name = "pyw", text = "", fg = "{Swatch.blue}" }},
{{ name = "a", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "bicep", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "download", text = "", fg = "{Swatch.teal}" }},
{{ name = "pyo", text = "", fg = "{Swatch.yellow}" }},
{{ name = "cu", text = "", fg = "{Swatch.green}" }},
{{ name = "h", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "blend", text = "󰂫", fg = "{Swatch.peach}" }},
{{ name = "zip", text = "", fg = "{Swatch.peach}" }},
{{ name = "unity", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "zig", text = "", fg = "{Swatch.peach}" }},
{{ name = "yml", text = "", fg = "{Swatch.peach}" }},
{{ name = "m", text = "", fg = "{Swatch.blue}" }},
{{ name = "xz", text = "", fg = "{Swatch.peach}" }},
{{ name = "ifc", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "xul", text = "", fg = "{Swatch.peach}" }},
{{ name = "ebuild", text = "", fg = "{Swatch.surface1}" }},
{{ name = "f#", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "fish", text = "", fg = "{Swatch.surface2}" }},
{{ name = "scm", text = "󰘧", fg = "{Swatch.rosewater}" }},
{{ name = "tbc", text = "󰛓", fg = "{Swatch.surface2}" }},
{{ name = "slim", text = "", fg = "{Swatch.peach}" }},
{{ name = "pyi", text = "", fg = "{Swatch.yellow}" }},
{{ name = "xpi", text = "", fg = "{Swatch.peach}" }},
{{ name = "astro", text = "", fg = "{Swatch.red}" }},
{{ name = "lrc", text = "󰨖", fg = "{Swatch.yellow}" }},
{{ name = "vala", text = "", fg = "{Swatch.surface2}" }},
{{ name = "tmpl", text = "", fg = "{Swatch.yellow}" }},
{{ name = "xm", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "f90", text = "󱈚", fg = "{Swatch.surface2}" }},
{{ name = "fods", text = "", fg = "{Swatch.green}" }},
{{ name = "elf", text = "", fg = "{Swatch.surface1}" }},
{{ name = "pcm", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "kdenlivetitle", text = "", fg = "{Swatch.blue}" }},
{{ name = "xcstrings", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "ccm", text = "", fg = "{Swatch.red}" }},
{{ name = "aac", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "kicad_prl", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "xcplayground", text = "", fg = "{Swatch.peach}" }},
{{ name = "xcf", text = "", fg = "{Swatch.surface2}" }},
{{ name = "cfc", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "less", text = "", fg = "{Swatch.surface1}" }},
{{ name = "hh", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "xaml", text = "󰙳", fg = "{Swatch.surface2}" }},
{{ name = "hx", text = "", fg = "{Swatch.peach}" }},
{{ name = "wvc", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "pck", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "eot", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "docx", text = "󰈬", fg = "{Swatch.surface2}" }},
{{ name = "sqlite3", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "wv", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "cxxm", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "dot", text = "󱁉", fg = "{Swatch.surface2}" }},
{{ name = "tsconfig", text = "", fg = "{Swatch.peach}" }},
{{ name = "wrz", text = "󰆧", fg = "{Swatch.overlay1}" }},
{{ name = "stl", text = "󰆧", fg = "{Swatch.overlay1}" }},
{{ name = "wrl", text = "󰆧", fg = "{Swatch.overlay1}" }},
{{ name = "gz", text = "", fg = "{Swatch.peach}" }},
{{ name = "woff2", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "stories.mjs", text = "", fg = "{Swatch.red}" }},
{{ name = "fctb", text = "", fg = "{Swatch.red}" }},
{{ name = "asm", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "ogx", text = "", fg = "{Swatch.peach}" }},
{{ name = "wmv", text = "", fg = "{Swatch.peach}" }},
{{ name = "terminal", text = "", fg = "{Swatch.green}" }},
{{ name = "webpack", text = "󰜫", fg = "{Swatch.sapphire}" }},
{{ name = "v", text = "󰍛", fg = "{Swatch.green}" }},
{{ name = "webmanifest", text = "", fg = "{Swatch.yellow}" }},
{{ name = "webm", text = "", fg = "{Swatch.peach}" }},
{{ name = "wav", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "wasm", text = "", fg = "{Swatch.surface2}" }},
{{ name = "ape", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "pot", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "skp", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "license", text = "", fg = "{Swatch.yellow}" }},
{{ name = "vsix", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "vsh", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "vim", text = "", fg = "{Swatch.green}" }},
{{ name = "ai", text = "", fg = "{Swatch.yellow}" }},
{{ name = "fctl", text = "", fg = "{Swatch.red}" }},
{{ name = "markdown", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "cts", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "config.ru", text = "", fg = "{Swatch.surface0}" }},
{{ name = "stp", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "feature", text = "", fg = "{Swatch.green}" }},
{{ name = "cfg", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "mov", text = "", fg = "{Swatch.peach}" }},
{{ name = "ads", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "vh", text = "󰍛", fg = "{Swatch.green}" }},
{{ name = "blp", text = "󰺾", fg = "{Swatch.blue}" }},
{{ name = "bz", text = "", fg = "{Swatch.peach}" }},
{{ name = "lff", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "torrent", text = "", fg = "{Swatch.teal}" }},
{{ name = "rmd", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "mkv", text = "", fg = "{Swatch.peach}" }},
{{ name = "webp", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "bin", text = "", fg = "{Swatch.surface1}" }},
{{ name = "svg", text = "󰜡", fg = "{Swatch.peach}" }},
{{ name = "hxx", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "ui", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "oga", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "apk", text = "", fg = "{Swatch.green}" }},
{{ name = "🔥", text = "", fg = "{Swatch.peach}" }},
{{ name = "cxx", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "gradle", text = "", fg = "{Swatch.surface2}" }},
{{ name = "ods", text = "", fg = "{Swatch.green}" }},
{{ name = "eex", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "typ", text = "", fg = "{Swatch.sky}" }},
{{ name = "avif", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "out", text = "", fg = "{Swatch.surface1}" }},
{{ name = "ogg", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "import", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "bazel", text = "", fg = "{Swatch.green}" }},
{{ name = "dwg", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "pxi", text = "", fg = "{Swatch.blue}" }},
{{ name = "ttf", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "tsx", text = "", fg = "{Swatch.surface2}" }},
{{ name = "tscn", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "kdbx", text = "", fg = "{Swatch.green}" }},
{{ name = "heex", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "sldprt", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "hex", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "erb", text = "", fg = "{Swatch.surface0}" }},
{{ name = "vi", text = "", fg = "{Swatch.yellow}" }},
{{ name = "ksh", text = "", fg = "{Swatch.surface2}" }},
{{ name = "sqlite", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "toml", text = "", fg = "{Swatch.surface2}" }},
{{ name = "spec.jsx", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "sh", text = "", fg = "{Swatch.surface2}" }},
{{ name = "tfvars", text = "", fg = "{Swatch.surface2}" }},
{{ name = "3gp", text = "", fg = "{Swatch.peach}" }},
{{ name = "tf", text = "", fg = "{Swatch.surface2}" }},
{{ name = "csh", text = "", fg = "{Swatch.surface2}" }},
{{ name = "tex", text = "", fg = "{Swatch.surface1}" }},
{{ name = "android", text = "", fg = "{Swatch.green}" }},
{{ name = "aiff", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "diff", text = "", fg = "{Swatch.surface1}" }},
{{ name = "7z", text = "", fg = "{Swatch.peach}" }},
{{ name = "norg", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "test.tsx", text = "", fg = "{Swatch.surface2}" }},
{{ name = "apl", text = "", fg = "{Swatch.green}" }},
{{ name = "sldasm", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "cjs", text = "", fg = "{Swatch.yellow}" }},
{{ name = "test.ts", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "ejs", text = "", fg = "{Swatch.yellow}" }},
{{ name = "test.jsx", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "test.js", text = "", fg = "{Swatch.yellow}" }},
{{ name = "wma", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "templ", text = "", fg = "{Swatch.yellow}" }},
{{ name = "msf", text = "", fg = "{Swatch.blue}" }},
{{ name = "query", text = "", fg = "{Swatch.green}" }},
{{ name = "tcl", text = "󰛓", fg = "{Swatch.surface2}" }},
{{ name = "desktop", text = "", fg = "{Swatch.surface1}" }},
{{ name = "svx", text = "", fg = "{Swatch.red}" }},
{{ name = "cobol", text = "", fg = "{Swatch.surface2}" }},
{{ name = "t", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "swift", text = "", fg = "{Swatch.peach}" }},
{{ name = "svh", text = "󰍛", fg = "{Swatch.green}" }},
{{ name = "m3u8", text = "󰲹", fg = "{Swatch.red}" }},
{{ name = "scad", text = "", fg = "{Swatch.yellow}" }},
{{ name = "svelte", text = "", fg = "{Swatch.peach}" }},
{{ name = "bak", text = "󰁯", fg = "{Swatch.overlay1}" }},
{{ name = "sv", text = "󰍛", fg = "{Swatch.green}" }},
{{ name = "nu", text = "", fg = "{Swatch.green}" }},
{{ name = "java", text = "", fg = "{Swatch.red}" }},
{{ name = "sublime", text = "", fg = "{Swatch.peach}" }},
{{ name = "sub", text = "󰨖", fg = "{Swatch.yellow}" }},
{{ name = "jar", text = "", fg = "{Swatch.peach}" }},
{{ name = "mjs", text = "", fg = "{Swatch.yellow}" }},
{{ name = "magnet", text = "", fg = "{Swatch.surface1}" }},
{{ name = "el", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "jwmrc", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "cache", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "odf", text = "", fg = "{Swatch.red}" }},
{{ name = "pdf", text = "", fg = "{Swatch.surface2}" }},
{{ name = "fodp", text = "", fg = "{Swatch.peach}" }},
{{ name = "vhdl", text = "󰍛", fg = "{Swatch.green}" }},
{{ name = "stories.tsx", text = "", fg = "{Swatch.red}" }},
{{ name = "jsx", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "gql", text = "", fg = "{Swatch.red}" }},
{{ name = "cs", text = "󰌛", fg = "{Swatch.surface2}" }},
{{ name = "pyd", text = "", fg = "{Swatch.yellow}" }},
{{ name = "asc", text = "󰦝", fg = "{Swatch.overlay0}" }},
{{ name = "bz3", text = "", fg = "{Swatch.peach}" }},
{{ name = "woff", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "otf", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "stories.js", text = "", fg = "{Swatch.red}" }},
{{ name = "pptx", text = "󰈧", fg = "{Swatch.red}" }},
{{ name = "elm", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "glb", text = "", fg = "{Swatch.peach}" }},
{{ name = "fsx", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "py", text = "", fg = "{Swatch.yellow}" }},
{{ name = "ste", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "sln", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "gleam", text = "", fg = "{Swatch.pink}" }},
{{ name = "fcscript", text = "", fg = "{Swatch.red}" }},
{{ name = "spec.tsx", text = "", fg = "{Swatch.surface2}" }},
{{ name = "eln", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "sql", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "rkt", text = "󰘧", fg = "{Swatch.surface1}" }},
{{ name = "md5", text = "󰕥", fg = "{Swatch.overlay1}" }},
{{ name = "clj", text = "", fg = "{Swatch.green}" }},
{{ name = "sha224", text = "󰕥", fg = "{Swatch.overlay1}" }},
{{ name = "spec.js", text = "", fg = "{Swatch.yellow}" }},
{{ name = "sha384", text = "󰕥", fg = "{Swatch.overlay1}" }},
{{ name = "sol", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "so", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "sml", text = "󰘧", fg = "{Swatch.peach}" }},
{{ name = "mdx", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "slvs", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "slnx", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "ssa", text = "󰨖", fg = "{Swatch.yellow}" }},
{{ name = "kra", text = "", fg = "{Swatch.mauve}" }},
{{ name = "sig", text = "󰘧", fg = "{Swatch.peach}" }},
{{ name = "jpeg", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "cshtml", text = "󱦗", fg = "{Swatch.surface2}" }},
{{ name = "fsi", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "coffee", text = "", fg = "{Swatch.yellow}" }},
{{ name = "bzl", text = "", fg = "{Swatch.green}" }},
{{ name = "sha512", text = "󰕥", fg = "{Swatch.overlay1}" }},
{{ name = "flac", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "sha256", text = "󰕥", fg = "{Swatch.overlay1}" }},
{{ name = "org", text = "", fg = "{Swatch.teal}" }},
{{ name = "spec.ts", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "brep", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "pub", text = "󰷖", fg = "{Swatch.yellow}" }},
{{ name = "jsonc", text = "", fg = "{Swatch.yellow}" }},
{{ name = "sha1", text = "󰕥", fg = "{Swatch.overlay1}" }},
{{ name = "tmux", text = "", fg = "{Swatch.green}" }},
{{ name = "vert", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "cpy", text = "", fg = "{Swatch.surface2}" }},
{{ name = "xml", text = "󰗀", fg = "{Swatch.peach}" }},
{{ name = "sc", text = "", fg = "{Swatch.red}" }},
{{ name = "cljs", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "kicad_sym", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "bat", text = "", fg = "{Swatch.green}" }},
{{ name = "fodg", text = "", fg = "{Swatch.yellow}" }},
{{ name = "sass", text = "", fg = "{Swatch.red}" }},
{{ name = "cuh", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "rasi", text = "", fg = "{Swatch.yellow}" }},
{{ name = "dll", text = "", fg = "{Swatch.crust}" }},
{{ name = "ics", text = "", fg = "{Swatch.surface0}" }},
{{ name = "razor", text = "󱦘", fg = "{Swatch.surface2}" }},
{{ name = "gpr", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "kbx", text = "󰯄", fg = "{Swatch.overlay0}" }},
{{ name = "mustache", text = "", fg = "{Swatch.peach}" }},
{{ name = "resi", text = "", fg = "{Swatch.red}" }},
{{ name = "res", text = "", fg = "{Swatch.red}" }},
{{ name = "mp3", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "hurl", text = "", fg = "{Swatch.red}" }},
{{ name = "gnumakefile", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "rproj", text = "󰗆", fg = "{Swatch.green}" }},
{{ name = "rar", text = "", fg = "{Swatch.peach}" }},
{{ name = "rake", text = "", fg = "{Swatch.surface0}" }},
{{ name = "igs", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "elc", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "dump", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "qrc", text = "", fg = "{Swatch.green}" }},
{{ name = "qml", text = "", fg = "{Swatch.green}" }},
{{ name = "ifb", text = "", fg = "{Swatch.surface0}" }},
{{ name = "qm", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "mm", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "pyx", text = "", fg = "{Swatch.blue}" }},
{{ name = "typoscript", text = "", fg = "{Swatch.peach}" }},
{{ name = "pm", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "pyc", text = "", fg = "{Swatch.yellow}" }},
{{ name = "mo", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "zsh", text = "", fg = "{Swatch.green}" }},
{{ name = "frag", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "fbx", text = "󰆧", fg = "{Swatch.overlay1}" }},
{{ name = "stories.svelte", text = "", fg = "{Swatch.red}" }},
{{ name = "step", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "go", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "mp4", text = "", fg = "{Swatch.peach}" }},
{{ name = "bicepparam", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "c++", text = "", fg = "{Swatch.red}" }},
{{ name = "ada", text = "", fg = "{Swatch.blue}" }},
{{ name = "twig", text = "", fg = "{Swatch.green}" }},
{{ name = "pxd", text = "", fg = "{Swatch.blue}" }},
{{ name = "odt", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "psd1", text = "󰨊", fg = "{Swatch.overlay1}" }},
{{ name = "po", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "psd", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "cob", text = "", fg = "{Swatch.surface2}" }},
{{ name = "rb", text = "", fg = "{Swatch.surface0}" }},
{{ name = "ps1", text = "󰨊", fg = "{Swatch.overlay0}" }},
{{ name = "fcmat", text = "", fg = "{Swatch.red}" }},
{{ name = "tres", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "prisma", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "prefab", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "ppt", text = "󰈧", fg = "{Swatch.red}" }},
{{ name = "applescript", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "pp", text = "", fg = "{Swatch.peach}" }},
{{ name = "cp", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "png", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "ply", text = "󰆧", fg = "{Swatch.overlay1}" }},
{{ name = "pls", text = "󰲹", fg = "{Swatch.red}" }},
{{ name = "pl", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "php", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "dxf", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "patch", text = "", fg = "{Swatch.surface1}" }},
{{ name = "part", text = "", fg = "{Swatch.teal}" }},
{{ name = "opus", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "gcode", text = "󰐫", fg = "{Swatch.overlay0}" }},
{{ name = "psm1", text = "󰨊", fg = "{Swatch.overlay1}" }},
{{ name = "cppm", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "m4v", text = "", fg = "{Swatch.peach}" }},
{{ name = "fcmacro", text = "", fg = "{Swatch.red}" }},
{{ name = "doc", text = "󰈬", fg = "{Swatch.surface2}" }},
{{ name = "odg", text = "", fg = "{Swatch.yellow}" }},
{{ name = "ko", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "o", text = "", fg = "{Swatch.surface1}" }},
{{ name = "suo", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "fcstd1", text = "", fg = "{Swatch.red}" }},
{{ name = "http", text = "", fg = "{Swatch.blue}" }},
{{ name = "nswag", text = "", fg = "{Swatch.green}" }},
{{ name = "nix", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "kdenlive", text = "", fg = "{Swatch.blue}" }},
{{ name = "geom", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "nim", text = "", fg = "{Swatch.yellow}" }},
{{ name = "env", text = "", fg = "{Swatch.yellow}" }},
{{ name = "nfo", text = "", fg = "{Swatch.yellow}" }},
{{ name = "mts", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "azcli", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "bash", text = "", fg = "{Swatch.green}" }},
{{ name = "lock", text = "", fg = "{Swatch.subtext1}" }},
{{ name = "fcstd", text = "", fg = "{Swatch.red}" }},
{{ name = "vhd", text = "󰍛", fg = "{Swatch.green}" }},
{{ name = "mojo", text = "", fg = "{Swatch.peach}" }},
{{ name = "luau", text = "", fg = "{Swatch.blue}" }},
{{ name = "mli", text = "", fg = "{Swatch.peach}" }},
{{ name = "ml", text = "", fg = "{Swatch.peach}" }},
{{ name = "bz2", text = "", fg = "{Swatch.peach}" }},
{{ name = "mk", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "csv", text = "", fg = "{Swatch.green}" }},
{{ name = "mint", text = "󰌪", fg = "{Swatch.green}" }},
{{ name = "crdownload", text = "", fg = "{Swatch.teal}" }},
{{ name = "spx", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "yaml", text = "", fg = "{Swatch.peach}" }},
{{ name = "pro", text = "", fg = "{Swatch.yellow}" }},
{{ name = "material", text = "", fg = "{Swatch.red}" }},
{{ name = "m3u", text = "󰲹", fg = "{Swatch.red}" }},
{{ name = "odp", text = "", fg = "{Swatch.peach}" }},
{{ name = "Dockerfile", text = "󰡨", fg = "{Swatch.blue}" }},
{{ name = "fcbak", text = "", fg = "{Swatch.red}" }},
{{ name = "dconf", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "bqn", text = "", fg = "{Swatch.green}" }},
{{ name = "svgz", text = "󰜡", fg = "{Swatch.peach}" }},
{{ name = "md", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "aif", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "bib", text = "󱉟", fg = "{Swatch.yellow}" }},
{{ name = "mobi", text = "", fg = "{Swatch.peach}" }},
{{ name = "luac", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "ebook", text = "", fg = "{Swatch.peach}" }},
{{ name = "krz", text = "", fg = "{Swatch.mauve}" }},
{{ name = "conf", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "iges", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "exe", text = "", fg = "{Swatch.surface1}" }},
{{ name = "lua", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "scala", text = "", fg = "{Swatch.red}" }},
{{ name = "signature", text = "󰘧", fg = "{Swatch.peach}" }},
{{ name = "lib", text = "", fg = "{Swatch.crust}" }},
{{ name = "image", text = "", fg = "{Swatch.flamingo}" }},
{{ name = "lhs", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "scss", text = "", fg = "{Swatch.red}" }},
{{ name = "leex", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "lck", text = "", fg = "{Swatch.subtext1}" }},
{{ name = "kicad_sch", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "iso", text = "", fg = "{Swatch.flamingo}" }},
{{ name = "kts", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "kt", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "log", text = "󰌱", fg = "{Swatch.rosewater}" }},
{{ name = "kpp", text = "", fg = "{Swatch.mauve}" }},
{{ name = "obj", text = "󰆧", fg = "{Swatch.overlay1}" }},
{{ name = "db", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "kicad_wks", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "kicad_pro", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "cow", text = "󰆚", fg = "{Swatch.peach}" }},
{{ name = "dart", text = "", fg = "{Swatch.surface2}" }},
{{ name = "json", text = "", fg = "{Swatch.yellow}" }},
{{ name = "ico", text = "", fg = "{Swatch.yellow}" }},
{{ name = "kicad_mod", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "kdb", text = "", fg = "{Swatch.green}" }},
{{ name = "rlib", text = "", fg = "{Swatch.peach}" }},
{{ name = "jxl", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "fcparam", text = "", fg = "{Swatch.red}" }},
{{ name = "kicad_pcb", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "haml", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "js", text = "", fg = "{Swatch.yellow}" }},
{{ name = "jpg", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "jl", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "ixx", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "ipynb", text = "", fg = "{Swatch.peach}" }},
{{ name = "cfm", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "3mf", text = "󰆧", fg = "{Swatch.overlay1}" }},
{{ name = "s", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "hs", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "fodt", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "odin", text = "󰟢", fg = "{Swatch.blue}" }},
{{ name = "cc", text = "", fg = "{Swatch.red}" }},
{{ name = "r", text = "󰟔", fg = "{Swatch.overlay0}" }},
{{ name = "srt", text = "󰨖", fg = "{Swatch.yellow}" }},
{{ name = "rs", text = "", fg = "{Swatch.peach}" }},
{{ name = "html", text = "", fg = "{Swatch.peach}" }},
{{ name = "icalendar", text = "", fg = "{Swatch.surface0}" }},
{{ name = "cson", text = "", fg = "{Swatch.yellow}" }},
{{ name = "x", text = "", fg = "{Swatch.blue}" }},
{{ name = "xslt", text = "󰗀", fg = "{Swatch.sapphire}" }},
{{ name = "ts", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "cast", text = "", fg = "{Swatch.peach}" }},
{{ name = "csproj", text = "󰪮", fg = "{Swatch.surface2}" }},
{{ name = "hbs", text = "", fg = "{Swatch.peach}" }},
{{ name = "gemspec", text = "", fg = "{Swatch.surface0}" }},
{{ name = "sbt", text = "", fg = "{Swatch.red}" }},
{{ name = "cr", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "psb", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "erl", text = "", fg = "{Swatch.red}" }},
{{ name = "ige", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "gif", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "gresource", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "f3d", text = "󰻫", fg = "{Swatch.green}" }},
{{ name = "fsscript", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "cljd", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "dropbox", text = "", fg = "{Swatch.overlay0}" }},
{{ name = "txz", text = "", fg = "{Swatch.peach}" }},
{{ name = "info", text = "", fg = "{Swatch.yellow}" }},
{{ name = "fnl", text = "", fg = "{Swatch.yellow}" }},
{{ name = "d.ts", text = "", fg = "{Swatch.peach}" }},
{{ name = "awk", text = "", fg = "{Swatch.surface2}" }},
{{ name = "flc", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "fdmdownload", text = "", fg = "{Swatch.teal}" }},
{{ name = "json5", text = "", fg = "{Swatch.yellow}" }},
{{ name = "img", text = "", fg = "{Swatch.flamingo}" }},
{{ name = "xlsx", text = "󰈛", fg = "{Swatch.surface2}" }},
{{ name = "gd", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "htm", text = "", fg = "{Swatch.peach}" }},
{{ name = "glsl", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "epub", text = "", fg = "{Swatch.peach}" }},
{{ name = "xls", text = "󰈛", fg = "{Swatch.surface2}" }},
{{ name = "qss", text = "", fg = "{Swatch.green}" }},
{{ name = "rss", text = "", fg = "{Swatch.peach}" }},
{{ name = "zst", text = "", fg = "{Swatch.peach}" }},
{{ name = "dockerignore", text = "󰡨", fg = "{Swatch.blue}" }},
{{ name = "edn", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "m4a", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "adb", text = "", fg = "{Swatch.blue}" }},
{{ name = "flf", text = "", fg = "{Swatch.rosewater}" }},
{{ name = "ini", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "cue", text = "󰲹", fg = "{Swatch.red}" }},
{{ name = "conda", text = "", fg = "{Swatch.green}" }},
{{ name = "css", text = "", fg = "{Swatch.surface1}" }},
{{ name = "blade.php", text = "", fg = "{Swatch.red}" }},
{{ name = "stories.ts", text = "", fg = "{Swatch.red}" }},
{{ name = "godot", text = "", fg = "{Swatch.overlay1}" }},
{{ name = "fs", text = "", fg = "{Swatch.sapphire}" }},
{{ name = "ass", text = "󰨖", fg = "{Swatch.yellow}" }},
{{ name = "graphql", text = "", fg = "{Swatch.red}" }},
{{ name = "cmake", text = "", fg = "{Swatch.text}" }},
]
""",
        "place": PLACE,
        "file": "flavor.toml",
        "files": [{"path": Path("tmtheme.xml"), "content": bat_["content"]}],
        "doc": """
to activate this yazi theme add these lines to your yazi <theme.toml>:
[flavor]
dark = "franky"
""",
    }
