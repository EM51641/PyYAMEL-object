import pytest
from pyyaml_object.utils import Node


class TestsNode:
    @pytest.fixture(autouse=True)
    def _setup(self):
        self._node = Node()

    def test_node_repr(self):
        assert str(self._node) == f"Node(id={id(self._node)})"

    def test_node_str(self):
        assert repr(self._node) == f"Node(id={id(self._node)})"
