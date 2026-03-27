"""Tests for tree visualization."""

from arborpy.node import Node
from arborpy.visualize import pretty_str


class TestPrettyStr:
    """Tests for ASCII tree visualization."""

    def test_none(self) -> None:
        """Empty tree shows placeholder text."""
        assert pretty_str(None) == "(empty tree)"

    def test_single_node(self) -> None:
        """Single node displays just its value."""
        assert pretty_str(Node(5)) == "5"

    def test_output_is_string(self) -> None:
        """pretty_str always returns a string."""
        assert isinstance(pretty_str(Node(5)), str)

    def test_contains_all_values(self) -> None:
        """Output contains all node values."""
        root = Node(5, Node(3), Node(7))
        result = pretty_str(root)
        assert "5" in result
        assert "3" in result
        assert "7" in result

    def test_multiline(self) -> None:
        """Tree with children produces multi-line output."""
        root = Node(5, Node(3), Node(7))
        result = pretty_str(root)
        assert "\n" in result
