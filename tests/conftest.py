from __future__ import annotations

import ast

import pytest
from flake8_qt_tr.checker import TrChecker


class PluginWrapper:
    def __init__(self, code: str) -> None:
        self.tree = ast.parse(code)
        self.plugin = TrChecker(self.tree)

    def run(self) -> set[str]:
        return {f"{line}:{col} {msg}" for line, col, msg, _ in self.plugin.run()}


@pytest.fixture()
def plugin_wrapper() -> type[PluginWrapper]:
    return PluginWrapper
