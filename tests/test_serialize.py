"""Tests for serialization and deserialization."""

from arborpy import Node, from_dict, from_json, to_dict, to_json


class TestToDict:
    """Tests for tree-to-dict conversion."""

    def test_none(self) -> None:
        """None tree returns None."""
        assert to_dict(None) is None

    def test_single_node(self) -> None:
        """Single node converts correctly."""
        result = to_dict(Node(5))
        assert result == {"val": 5, "left": None, "right": None}

    def test_with_children(self) -> None:
        """Tree with children nests correctly."""
        root = Node(5, Node(3), Node(7))
        result = to_dict(root)
        assert result is not None
        assert result["val"] == 5
        assert result["left"] == {"val": 3, "left": None, "right": None}
        assert result["right"] == {"val": 7, "left": None, "right": None}


class TestFromDict:
    """Tests for dict-to-tree conversion."""

    def test_none(self) -> None:
        """None input returns None."""
        assert from_dict(None) is None

    def test_single_node(self) -> None:
        """Dict reconstructs single node."""
        node = from_dict({"val": 5, "left": None, "right": None})
        assert node is not None
        assert node.val == 5
        assert node.left is None
        assert node.right is None

    def test_roundtrip(self) -> None:
        """Converting to dict and back preserves structure."""
        original = Node(5, Node(3, Node(1)), Node(7))
        reconstructed = from_dict(to_dict(original))
        assert reconstructed is not None
        assert reconstructed.val == 5
        assert reconstructed.left is not None
        assert reconstructed.left.val == 3
        assert reconstructed.left.left is not None
        assert reconstructed.left.left.val == 1
        assert reconstructed.right is not None
        assert reconstructed.right.val == 7


class TestJson:
    """Tests for JSON serialization."""

    def test_to_json_single(self) -> None:
        """JSON output contains the node value."""
        result = to_json(Node(5))
        assert '"val": 5' in result

    def test_from_json_single(self) -> None:
        """JSON string reconstructs a node."""
        node = from_json('{"val": 5, "left": null, "right": null}')
        assert node is not None
        assert node.val == 5

    def test_json_roundtrip(self) -> None:
        """JSON serialize and deserialize preserves structure."""
        original = Node(10, Node(5), Node(15))
        json_str = to_json(original)
        reconstructed = from_json(json_str)
        assert reconstructed is not None
        assert reconstructed.val == 10
        assert reconstructed.left is not None
        assert reconstructed.left.val == 5
        assert reconstructed.right is not None
        assert reconstructed.right.val == 15
