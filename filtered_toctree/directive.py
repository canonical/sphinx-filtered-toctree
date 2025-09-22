# This file is part of filtered-toctree.
#
# Copyright 2025 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License version 3, as published by the Free Software
# Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranties of MERCHANTABILITY, SATISFACTORY
# QUALITY, or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with this
# program.  If not, see <http://www.gnu.org/licenses/>.

"""The core logic of the filtered-toctree extension."""

import re

from docutils.nodes import Node
from docutils.statemachine import StringList
from sphinx.directives.other import TocTree

FILTER_PATTERN = re.compile(r"^\s*:(.+?):.+$|^.*<:(.+?):.+>$")


class FilteredTocTree(TocTree):
    """Define the directive's behavior."""

    def filter_entries(self, entries: StringList) -> StringList:
        """Filter out ToC entries based on `toc_filter_exclude`.

        If they should be included, remove the filter (e.g., ':something:').
        """
        excl = self.state.document.settings.env.config.toc_filter_exclude
        filtered: list[str] = []
        for e in entries:
            m = FILTER_PATTERN.match(e)

            filt: str = ""
            if m is not None:
                # The filter is in different matches depending on whether
                # we override the title and where we put the filter
                if e.startswith(":"):
                    filt = m.groups()[0]
                elif e.endswith(">"):
                    filt = m.groups()[1]

                # Keep the entries that are not supposed to be excluded
                if filt and filt not in excl:
                    filtered.append(e.replace(":" + filt + ":", ""))
            else:
                filtered.append(e)
        return StringList(filtered)

    def run(self) -> list[Node]:
        """Remove all ToC entries excluded by `toc_filter_exclude`."""
        self.content = self.filter_entries(self.content)
        return super().run()
