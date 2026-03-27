"""Tests for traversal functions."""

from arborpy import Node, inorder, level_order, postorder, preorder


class TestInorder:
    """Tests for inorder traversal."""

    def test_none(self) -> None:
        """Inorder of None returns empty list."""
        assert inorder(None) == []

    def test_single_node(self) -> None:
        """Inorder of single node returns its value."""
        assert inorder(Node(5)) == [5]

    def test_full_tree(self) -> None:
        """Inorder returns left-root-right ordering."""
        root = Node(2, Node(1), Node(3))
        assert inorder(root) == [1, 2, 3]

    def test_left_skewed(self) -> None:
        """Inorder handles left-only trees."""
        root = Node(3, Node(2, Node(1)))
        assert inorder(root) == [1, 2, 3]

    def test_right_skewed(self) -> None:
        """Inorder handles right-only trees."""
        root = Node(1, right=Node(2, right=Node(3)))
        assert inorder(root) == [1, 2, 3]


class TestPreorder:
    """Tests for preorder traversal."""

    def test_none(self) -> None:
        """Preorder of None returns empty list."""
        assert preorder(None) == []

    def test_single_node(self) -> None:
        """Preorder of single node returns its value."""
        assert preorder(Node(5)) == [5]

    def test_full_tree(self) -> None:
        """Preorder returns root-left-right ordering."""
        root = Node(2, Node(1), Node(3))
        assert preorder(root) == [2, 1, 3]


class TestPostorder:
    """Tests for postorder traversal."""

    def test_none(self) -> None:
        """Postorder of None returns empty list."""
        assert postorder(None) == []

    def test_single_node(self) -> None:
        """Postorder of single node returns its value."""
        assert postorder(Node(5)) == [5]

    def test_full_tree(self) -> None:
        """Postorder returns left-right-root ordering."""
        root = Node(2, Node(1), Node(3))
        assert postorder(root) == [1, 3, 2]


class TestLevelOrder:
    """Tests for level-order traversal."""

    def test_none(self) -> None:
        """Level-order of None returns empty list."""
        assert level_order(None) == []

    def test_single_node(self) -> None:
        """Level-order of single node returns one level."""
        assert level_order(Node(5)) == [[5]]

    def test_full_tree(self) -> None:
        """Level-order returns values grouped by level."""
        root = Node(1, Node(2), Node(3))
        assert level_order(root) == [[1], [2, 3]]

    def test_three_levels(self) -> None:
        """Level-order handles deeper trees."""
        root = Node(1, Node(2, Node(4), Node(5)), Node(3))
        assert level_order(root) == [[1], [2, 3], [4, 5]]
