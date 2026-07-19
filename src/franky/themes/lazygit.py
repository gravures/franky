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
"""Lazygit Franky theme."""

from __future__ import annotations

import os
from pathlib import Path

from franky import UI, Swatch, Theme
from franky.theme import Place


PLACE = Place(
    posix=Path.home() / ".config" / "lazygit",
    darwin=Path.home() / ".config" / "lazygit",
    windows=Path(os.getenv("APPDATA", Path.home() / "AppData" / "Roaming")) / "lazygit",
)

CONFDIR = PLACE.current().parent  # pyright: ignore[reportOptionalMemberAccess]


def main() -> Theme:
    return {
        "content": f"""
 gui:
  theme:
    activeBorderColor:
      - '{UI.popup_border.fg}'
      - bold
    inactiveBorderColor:
      - '{Swatch.surface2}'
    searchingActiveBorderColor:
      - '{UI.jump_label.fg}'
    optionsTextColor:
      - '{UI.status_line.fg}'
    selectedLineBgColor:
      - '{UI.cursor_line.bg}'
    inactiveViewSelectedLineBgColor:
      - '{UI.popup.bg}'
    cherryPickedCommitFgColor:
      - '{UI.hint.fg}'
    cherryPickedCommitBgColor:
      - '{UI.popup.bg}'
    markedBaseCommitFgColor:
      - '{UI.hint.fg}'
    markedBaseCommitBgColor:
      - '{Swatch.yellow}'
    unstagedChangesColor:
      - '{UI.error.fg}'
    defaultFgColor:
      - '{Swatch.text}'

  authorColors:
    '*': '{Swatch.lavender}'
""",
        "place": PLACE,
        "file": "franky.yml",
        "doc": f"""
to activate this theme add this line to your shell .rc file:
export LG_CONFIG_FILE='{CONFDIR}/config.yml,franky.yml'

This will merge you're actual lazygit config with this theme.
It's also recommended to install franky delta theme to get diff view themed.
""",
    }
