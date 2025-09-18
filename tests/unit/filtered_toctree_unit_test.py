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

import pytest
from docutils.core import publish_doctree

TOCTREE_EXAMPLE = """\
.. toctree::

    entry1
"""


@pytest.mark.parametrize(
    "fake_toctree",
    [{"content": ["entry1"]}],
    indirect=True,
)
def test_filtered_toctree_exclude_none(fake_toctree):
    expected = publish_doctree(
        TOCTREE_EXAMPLE, settings=fake_toctree.state.document.settings
    ).children
    actual = fake_toctree.run()

    assert str(expected) == str(actual)


@pytest.mark.parametrize(
    "fake_toctree",
    [{"content": ["entry1", ":exclude:entry2"]}],
    indirect=True,
)
def test_filtered_toctree_exclude(fake_toctree):
    expected = publish_doctree(
        TOCTREE_EXAMPLE, settings=fake_toctree.state.document.settings
    ).children
    actual = fake_toctree.run()

    assert str(expected) == str(actual)


@pytest.mark.parametrize(
    "fake_toctree",
    [{"content": ["entry1", ":exclude:docname <entry2>"]}],
    indirect=True,
)
def test_filtered_toctree_exclude_name(fake_toctree):
    expected = publish_doctree(
        TOCTREE_EXAMPLE, settings=fake_toctree.state.document.settings
    ).children
    actual = fake_toctree.run()

    assert str(expected) == str(actual)


@pytest.mark.parametrize(
    "fake_toctree",
    [{"content": ["entry1", "docname <:exclude:entry2>"]}],
    indirect=True,
)
def test_filtered_toctree_exclude_target(fake_toctree):
    expected = publish_doctree(
        TOCTREE_EXAMPLE, settings=fake_toctree.state.document.settings
    ).children
    actual = fake_toctree.run()

    assert str(expected) == str(actual)


@pytest.mark.parametrize(
    "fake_toctree",
    [{"content": ["entry1", ":include:entry2"]}],
    indirect=True,
)
def test_filtered_toctree_include(fake_toctree):
    expected = publish_doctree(
        TOCTREE_EXAMPLE, settings=fake_toctree.state.document.settings
    ).children
    actual = fake_toctree.run()

    assert str(expected) == str(actual)


@pytest.mark.parametrize(
    "fake_toctree",
    [{"content": ["entry1", ":include:docname <entry2>"]}],
    indirect=True,
)
def test_filtered_toctree_include_name(fake_toctree):
    expected = publish_doctree(
        TOCTREE_EXAMPLE, settings=fake_toctree.state.document.settings
    ).children
    actual = fake_toctree.run()

    assert str(expected) == str(actual)


@pytest.mark.parametrize(
    "fake_toctree",
    [{"content": ["entry1", "docname <:include:entry2>"]}],
    indirect=True,
)
def test_filtered_toctree_include_target(fake_toctree):
    expected = publish_doctree(
        TOCTREE_EXAMPLE, settings=fake_toctree.state.document.settings
    ).children
    actual = fake_toctree.run()

    assert str(expected) == str(actual)
