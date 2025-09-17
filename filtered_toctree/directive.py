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

            if m is not None:
                # The filter is in different matches depending on whether
                # we override the title and where we put the filter
                if e.startswith(":"):
                    filt = m.groups()[0]
                elif e.endswith(">"):
                    filt = m.groups()[1]
                else:
                    filt = m.groups()[0]

                # Keep the entries that are not supposed to be excluded
                if filt not in excl:
                    filtered.append(e.replace(":" + filt + ":", ""))
            else:
                filtered.append(e)
        return StringList(filtered)

    def run(self) -> list[Node]:
        """Remove all ToC entries excluded by `toc_filter_exclude`."""
        self.content = self.filter_entries(self.content)
        return super().run()
