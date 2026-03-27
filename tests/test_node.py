"""Tests for the Node class."""

from arborpy import Node


class TestNodeCreation:
    """Tests for node creation and basic properties."""

    def test_create_node_with_value(self) -> None:
        """Node stores its value correctly."""
        node = Node(42)
        assert node.val == 42

    def test_create_node_children_default_none(self) -> None:
        """New nodes have no children by default."""
        node = Node(10)
        assert node.left is None
        assert node.right is None

    def test_create_node_with_children(self) -> None:
        """Nodes can be created with explicit children."""
        left = Node(1)
        right = Node(3)
        parent = Node(2, left=left, right=right)
        assert parent.left is left
        assert parent.right is right

    def test_create_node_with_string_value(self) -> None:
        """Nodes can hold any type of value."""
        node = Node("hello")
        assert node.val == "hello"


class TestNodeMethods:
    """Tests for node methods."""

    def test_is_leaf_true(self) -> None:
        """Leaf nodes have no children."""
        assert Node(5).is_leaf() is True

    def test_is_leaf_false_with_left(self) -> None:
        """Node with left child is not a leaf."""
        node = Node(5, left=Node(3))
        assert node.is_leaf() is False

    def test_is_leaf_false_with_right(self) -> None:
        """Node with right child is not a leaf."""
        node = Node(5, right=Node(7))
        assert node.is_leaf() is False

    def test_is_leaf_false_with_both(self) -> None:
        """Node with both children is not a leaf."""
        node = Node(5, left=Node(3), right=Node(7))
        assert node.is_leaf() is False

    def test_repr(self) -> None:
        """Repr shows the node value."""
        assert repr(Node(42)) == "Node(42)"
        assert repr(Node("hi")) == "Node('hi')"

    def test_equality_same_value(self) -> None:
        """Nodes with the same value are equal."""
        assert Node(5) == Node(5)

    def test_equality_different_value(self) -> None:
        """Nodes with different values are not equal."""
        assert Node(5) != Node(10)

    def test_equality_non_node(self) -> None:
        """Comparing node to non-node returns NotImplemented."""
        assert Node(5) != "not a node"

    def test_hash_consistent(self) -> None:
        """Equal nodes produce the same hash."""
        assert hash(Node(5)) == hash(Node(5))
