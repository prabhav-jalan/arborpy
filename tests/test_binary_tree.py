"""Tests for the BinarySearchTree class."""

import pytest

from arborpy import BinarySearchTree
from arborpy.exceptions import DuplicateKeyError, EmptyTreeError, NodeNotFoundError


class TestBSTCreation:
    """Tests for BST initialization."""

    def test_empty_tree(self, empty_bst: BinarySearchTree) -> None:
        """New BST is empty."""
        assert len(empty_bst) == 0
        assert empty_bst.root is None

    def test_bool_empty(self, empty_bst: BinarySearchTree) -> None:
        """Empty BST is falsy."""
        assert not empty_bst

    def test_bool_nonempty(self, sample_bst: BinarySearchTree) -> None:
        """Non-empty BST is truthy."""
        assert sample_bst

    def test_repr(self, sample_bst: BinarySearchTree) -> None:
        """Repr shows size."""
        assert repr(sample_bst) == "BinarySearchTree(size=7)"


class TestBSTInsert:
    """Tests for BST insert operation."""

    def test_insert_single(self, empty_bst: BinarySearchTree) -> None:
        """Inserting into empty tree creates root."""
        empty_bst.insert(10)
        assert empty_bst.root is not None
        assert empty_bst.root.val == 10
        assert len(empty_bst) == 1

    def test_insert_left(self, empty_bst: BinarySearchTree) -> None:
        """Smaller values go left."""
        empty_bst.insert(10)
        empty_bst.insert(5)
        assert empty_bst.root is not None
        assert empty_bst.root.left is not None
        assert empty_bst.root.left.val == 5

    def test_insert_right(self, empty_bst: BinarySearchTree) -> None:
        """Larger values go right."""
        empty_bst.insert(10)
        empty_bst.insert(15)
        assert empty_bst.root is not None
        assert empty_bst.root.right is not None
        assert empty_bst.root.right.val == 15

    def test_insert_duplicate_raises(self, empty_bst: BinarySearchTree) -> None:
        """Inserting duplicate value raises error."""
        empty_bst.insert(10)
        with pytest.raises(DuplicateKeyError):
            empty_bst.insert(10)

    def test_insert_duplicate_preserves_size(self, empty_bst: BinarySearchTree) -> None:
        """Failed duplicate insert doesn't change size."""
        empty_bst.insert(10)
        with pytest.raises(DuplicateKeyError):
            empty_bst.insert(10)
        assert len(empty_bst) == 1

    def test_insert_multiple(self, sample_bst: BinarySearchTree) -> None:
        """Inserting multiple values maintains correct size."""
        assert len(sample_bst) == 7


class TestBSTSearch:
    """Tests for BST search operation."""

    def test_search_existing(self, sample_bst: BinarySearchTree) -> None:
        """Search finds existing values."""
        assert sample_bst.search(5) is True
        assert sample_bst.search(1) is True
        assert sample_bst.search(8) is True

    def test_search_missing(self, sample_bst: BinarySearchTree) -> None:
        """Search returns False for missing values."""
        assert sample_bst.search(99) is False
        assert sample_bst.search(0) is False

    def test_search_empty_tree(self, empty_bst: BinarySearchTree) -> None:
        """Search on empty tree returns False."""
        assert empty_bst.search(5) is False

    def test_contains_operator(self, sample_bst: BinarySearchTree) -> None:
        """The 'in' operator works."""
        assert 5 in sample_bst
        assert 99 not in sample_bst


class TestBSTDelete:
    """Tests for BST delete operation."""

    def test_delete_leaf(self, sample_bst: BinarySearchTree) -> None:
        """Deleting a leaf node works correctly."""
        sample_bst.delete(1)
        assert sample_bst.search(1) is False
        assert len(sample_bst) == 6

    def test_delete_node_with_one_child(self) -> None:
        """Deleting a node with one child promotes the child."""
        bst = BinarySearchTree()
        for val in [5, 3, 1]:
            bst.insert(val)
        bst.delete(3)
        assert bst.search(3) is False
        assert bst.search(1) is True
        assert len(bst) == 2

    def test_delete_node_with_two_children(self, sample_bst: BinarySearchTree) -> None:
        """Deleting a node with two children uses inorder successor."""
        sample_bst.delete(3)
        assert sample_bst.search(3) is False
        assert sample_bst.search(1) is True
        assert sample_bst.search(4) is True
        assert len(sample_bst) == 6

    def test_delete_root(self, sample_bst: BinarySearchTree) -> None:
        """Deleting the root works correctly."""
        sample_bst.delete(5)
        assert sample_bst.search(5) is False
        assert len(sample_bst) == 6
        # All other values should still be present
        for val in [3, 7, 1, 4, 6, 8]:
            assert val in sample_bst

    def test_delete_missing_raises(self, sample_bst: BinarySearchTree) -> None:
        """Deleting non-existent value raises error."""
        with pytest.raises(NodeNotFoundError):
            sample_bst.delete(99)

    def test_delete_all_nodes(self) -> None:
        """Deleting all nodes results in empty tree."""
        bst = BinarySearchTree()
        for val in [5, 3, 7]:
            bst.insert(val)
        for val in [3, 7, 5]:
            bst.delete(val)
        assert len(bst) == 0
        assert bst.root is None


class TestBSTMinMax:
    """Tests for find_min and find_max."""

    def test_find_min(self, sample_bst: BinarySearchTree) -> None:
        """Find min returns smallest value."""
        assert sample_bst.find_min() == 1

    def test_find_max(self, sample_bst: BinarySearchTree) -> None:
        """Find max returns largest value."""
        assert sample_bst.find_max() == 8

    def test_find_min_empty_raises(self, empty_bst: BinarySearchTree) -> None:
        """Find min on empty tree raises error."""
        with pytest.raises(EmptyTreeError):
            empty_bst.find_min()

    def test_find_max_empty_raises(self, empty_bst: BinarySearchTree) -> None:
        """Find max on empty tree raises error."""
        with pytest.raises(EmptyTreeError):
            empty_bst.find_max()

    def test_find_min_single_node(self, empty_bst: BinarySearchTree) -> None:
        """Single-node tree: min is that node."""
        empty_bst.insert(42)
        assert empty_bst.find_min() == 42

    def test_find_max_single_node(self, empty_bst: BinarySearchTree) -> None:
        """Single-node tree: max is that node."""
        empty_bst.insert(42)
        assert empty_bst.find_max() == 42


class TestBSTHeight:
    """Tests for tree height calculation."""

    def test_height_empty(self, empty_bst: BinarySearchTree) -> None:
        """Empty tree has height -1."""
        assert empty_bst.height() == -1

    def test_height_single(self, empty_bst: BinarySearchTree) -> None:
        """Single node has height 0."""
        empty_bst.insert(5)
        assert empty_bst.height() == 0

    def test_height_balanced(self, sample_bst: BinarySearchTree) -> None:
        """Balanced sample tree has height 2."""
        assert sample_bst.height() == 2

    def test_height_skewed(self) -> None:
        """Completely skewed tree has height n-1."""
        bst = BinarySearchTree()
        for val in [1, 2, 3, 4, 5]:
            bst.insert(val)
        assert bst.height() == 4


class TestBSTTraversals:
    """Tests for traversal methods on BST."""

    def test_inorder(self, sample_bst: BinarySearchTree) -> None:
        """Inorder traversal returns sorted values."""
        assert sample_bst.inorder() == [1, 3, 4, 5, 6, 7, 8]

    def test_preorder(self, sample_bst: BinarySearchTree) -> None:
        """Preorder traversal returns root-first ordering."""
        assert sample_bst.preorder() == [5, 3, 1, 4, 7, 6, 8]

    def test_postorder(self, sample_bst: BinarySearchTree) -> None:
        """Postorder traversal returns leaves-first ordering."""
        assert sample_bst.postorder() == [1, 4, 3, 6, 8, 7, 5]

    def test_level_order(self, sample_bst: BinarySearchTree) -> None:
        """Level-order traversal returns values by level."""
        assert sample_bst.level_order() == [[5], [3, 7], [1, 4, 6, 8]]

    def test_traversals_empty(self, empty_bst: BinarySearchTree) -> None:
        """All traversals return empty list for empty tree."""
        assert empty_bst.inorder() == []
        assert empty_bst.preorder() == []
        assert empty_bst.postorder() == []
        assert empty_bst.level_order() == []
