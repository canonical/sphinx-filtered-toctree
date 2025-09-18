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

from pathlib import Path

import pytest
from docutils.frontend import get_default_settings
from docutils.parsers.rst import Parser
from docutils.parsers.rst.states import RSTState, RSTStateMachine
from docutils.statemachine import StringList
from docutils.utils import new_document
from filtered_toctree import FilteredTocTree
from sphinx.environment import BuildEnvironment
from sphinx.testing.util import SphinxTestApp
from typing_extensions import override


class FakeTocTree(FilteredTocTree):
    @override
    def __init__(self, content: StringList, env_root: Path):
        self.content = content
        self.options = {}
        self.state, self.state_machine = mock_state(env_root)
        self.lineno = 1

    @override
    def get_source_info(self) -> tuple[str, int]:
        return "src", 1


@pytest.fixture
def fake_toctree(request: pytest.FixtureRequest, tmp_path) -> FakeTocTree:
    """This fixture can be parametrized to override the default values."""
    # Get any optional overrides from the fixtures
    overrides = request.param if hasattr(request, "param") else {}

    return FakeTocTree(content=overrides.get("content", []), env_root=tmp_path)


def mock_state(tmp_path) -> tuple[RSTState, RSTStateMachine]:
    state_machine = RSTStateMachine([], "")
    state = RSTState(state_machine)
    document = new_document("docname", settings=get_default_settings(Parser))

    src_dir = tmp_path / "src"

    src_dir.mkdir(parents=True, exist_ok=True)
    (src_dir / "conf.py").write_text("project = 'mock'")
    (src_dir / "index.rst").write_text("index\n=====")

    test_app = SphinxTestApp(srcdir=src_dir)
    test_app.build()

    build_env = BuildEnvironment(test_app)
    build_env.temp_data["docname"] = "index"

    document.settings.env = build_env
    document.settings.env.config.toc_filter_exclude = ["exclude"]
    state.document = document

    return state, state_machine
