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

"""Adds the directive to Sphinx."""

from sphinx.util.typing import ExtensionMetadata
from sphinx.application import Sphinx
from filtered_toctree.directive import FilteredTocTree

try:
    from ._version import __version__
except ImportError:  # pragma: no cover
    from importlib.metadata import version, PackageNotFoundError

    try:
        __version__ = version("filtered_toctree")
    except PackageNotFoundError:
        __version__ = "dev"


def setup(app: Sphinx) -> ExtensionMetadata:
    """Add the extension to the Sphinx application instance."""
    app.add_config_value("toc_filter_exclude", [], "html")
    app.add_directive("filtered-toctree", FilteredTocTree)
    return {"version": "1.0.0", "parallel_read_safe": True, "parallel_write_safe": True}


__all__ = ["__version__", "setup"]
