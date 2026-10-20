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
"""Neomutt Franky theme."""

from __future__ import annotations

from pathlib import Path

from franky import UI, Ansi, Markup, Swatch, Theme
from franky.theme import Place


PLACE = Place(
    posix=Path.home() / ".config" / "neomutt",
    darwin=Path.home() / ".config" / "neomutt",
    windows=None,
)


def main() -> Theme:
    return {
        "content": f"""
color attachment	color14 default     # Attachments
color normal		color7 default          # Text
color index		    color6 default ~N       # New Messages
color index		    color1 default ~F   # Flagged messages
color index		    color5 default ~T  # Tagged Messages
color index		    color1 default ~D        # Messages to delete
color signature	    color8 default      # Signatures
color search		color3 color8   # Highlighted results

color indicator		default color8      # currently highlighted message
color error		    color1 default          # error messages
color status		color7 default         # status line
color tree          color7 default         # thread tree arrows
color tilde         color7 default         # blank line padding

color hdrdefault    color8 color0         # default headers Pink
color header		color8 color0 "^From:"
color header	    color8 color0 "^Subject:"

color quoted     	color15 default         # Subtext 0
color quoted1		color7 default          # Subtext 1
color quoted2		color8 default          # Surface 2
color quoted3		color0 default          # Surface 1
color quoted4		color0 default
color quoted5		color0 default

# email Green
color body    color7 color0 (^.*)
color body	  color2 color0	[\\-\\.+_a-zA-Z0-9]+@[\\-\\.a-zA-Z0-9]+
# URLs
color body	  color12 color0	(https?|ftp)://[\\-\\.,/%~_:?&=\\#a-zA-Z0-9]+
# *bold* text Blue
color body	  color4 color0	(^|[[:space:]])\\\\*[^[:space:]]+\\\\*([[:space:]]|$)
# _underlined_ text Blue
color body	  color4 color0	(^|[[:space:]])_[^[:space:]]+_([[:space:]]|$)
# /italic/ text Blue
color body	  color4 color0	(^|[[:space:]])/[^[:space:]]+/([[:space:]]|$)

# sidebar
color sidebar_background color8 color0
color sidebar_divider   color8 default
color sidebar_unread    color11 default
color sidebar_highlight color3 default
color sidebar_flagged   color1 default  # Mailboxes with flagged mails
color sidebar_new       color6 default      # Mailboxes with new mail
""",
        "place": PLACE,
        "file": "franky",
        "doc": f"""
to activate this theme you could add this line to <{PLACE.current()}/neomuttrc>:
source {PLACE.current()}/franky
""",
    }
