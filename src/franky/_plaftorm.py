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
from __future__ import annotations

from typing import Literal

from deluxe.availability import hints


PLATFORM: Literal["posix", "darwin", "windows"] = (
    "darwin" if "darwin" in hints() else "windows" if "windows" in hints() else "posix"
)

__all__ = ["PLATFORM"]
