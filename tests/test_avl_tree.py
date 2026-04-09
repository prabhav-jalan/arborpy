"""Tests for the AVLTree class."""

from __future__ import annotations

import pytest

from arborpy import AVLTree
from arborpy.exceptions import DuplicateKeyError, EmptyTreeError, NodeNotFoundError
from arborpy.node import AVLNode


class TestAVLTreeInsert:
    """Tests for AVLTree insertion and balancing."""

    def test_insert_single(self) -> None:
        """Inserting into empty tree creates root."""
        tree = AVLTree()
        tree.insert(10)
        assert tree.root is not None
        assert tree.root.val == 10
        assert len(tree) == 1

    def test_insert_multiple(self) -> None:
        """Inserting multiple values builds correct tree."""
        tree = AVLTree()
        for v in [10, 5, 15, 3, 7]:
            tree.insert(v)
        assert len(tree) == 5
        assert tree.search(7) is True

    def test_insert_duplicate_raises(self) -> None:
        """Inserting duplicate raises DuplicateKeyError."""
        tree = AVLTree()
        tree.insert(10)
        with pytest.raises(DuplicateKeyError):
            tree.insert(10)

    def test_right_rotation(self) -> None:
        """Inserting 30, 20, 10 triggers a right rotation."""
        tree = AVLTree()
        tree.insert(30)
        tree.insert(20)
        tree.insert(10)
        assert tree.root is not None
        assert tree.root.val == 20
        assert tree.root.left is not None
        assert tree.root.left.val == 10
        assert tree.root.right is not None
        assert tree.root.right.val == 30

    def test_left_rotation(self) -> None:
        """Inserting 10, 20, 30 triggers a left rotation."""
        tree = AVLTree()
        tree.insert(10)
        tree.insert(20)
        tree.insert(30)
        assert tree.root is not None
        assert tree.root.val == 20

    def test_left_right_rotation(self) -> None:
        """Inserting 30, 10, 20 triggers a left-right rotation."""
        tree = AVLTree()
        tree.insert(30)
        tree.insert(10)
        tree.insert(20)
        assert tree.root is not None
        assert tree.root.val == 20

    def test_right_left_rotation(self) -> None:
        """Inserting 10, 30, 20 triggers a right-left rotation."""
        tree = AVLTree()
        tree.insert(10)
        tree.insert(30)
        tree.insert(20)
        assert tree.root is not None
        assert tree.root.val == 20

    def test_height_after_inserts(self) -> None:
        """Fifteen sequential inserts produce height 3."""
        tree = AVLTree()
        for v in range(1, 16):
            tree.insert(v)
        assert tree.height() == 3

    def test_nodes_are_avlnodes(self) -> None:
        """Inserted nodes are AVLNode instances."""
        tree = AVLTree()
        tree.insert(10)
        assert isinstance(tree.root, AVLNode)


class TestAVLTreeDelete:
    """Tests for AVLTree deletion and rebalancing."""

    def test_delete_leaf(self) -> None:
        """Deleting a leaf removes it."""
        tree = AVLTree()
        for v in [10, 5, 15]:
            tree.insert(v)
        tree.delete(5)
        assert len(tree) == 2
        assert tree.search(5) is False

    def test_delete_node_with_one_child(self) -> None:
        """Deleting a node with one child promotes the child."""
        tree = AVLTree()
        for v in [10, 5, 15, 3]:
            tree.insert(v)
        tree.delete(5)
        assert len(tree) == 3
        assert tree.search(3) is True

    def test_delete_node_with_two_children(self) -> None:
        """Deleting a node with two children uses inorder successor."""
        tree = AVLTree()
        for v in [10, 5, 15, 3, 7]:
            tree.insert(v)
        tree.delete(5)
        assert len(tree) == 4
        assert tree.search(3) is True
        assert tree.search(7) is True

    def test_delete_root(self) -> None:
        """Deleting the root replaces it correctly."""
        tree = AVLTree()
        for v in [10, 5, 15]:
            tree.insert(v)
        tree.delete(10)
        assert len(tree) == 2
        assert tree.root is not None
        assert tree.root.val in {5, 15}

    def test_delete_triggers_rebalance(self) -> None:
        """Deletion that unbalances the tree triggers rotation."""
        tree = AVLTree()
        for v in [20, 10, 30, 25, 35]:
            tree.insert(v)
        tree.delete(10)
        assert tree.root is not None
        assert tree.root.val == 30

    def test_delete_nonexistent_raises(self) -> None:
        """Deleting a missing value raises NodeNotFoundError."""
        tree = AVLTree()
        tree.insert(10)
        with pytest.raises(NodeNotFoundError):
            tree.delete(99)

    def test_delete_from_empty_raises(self) -> None:
        """Deleting from empty tree raises NodeNotFoundError."""
        tree = AVLTree()
        with pytest.raises(NodeNotFoundError):
            tree.delete(10)

    def test_delete_all(self) -> None:
        """Deleting all values empties the tree."""
        tree = AVLTree()
        values = [10, 5, 15, 3, 7, 12, 20]
        for v in values:
            tree.insert(v)
        for v in values:
            tree.delete(v)
        assert len(tree) == 0
        assert tree.root is None


class TestAVLTreeTraversals:
    """Tests for AVLTree traversal methods."""

    @pytest.fixture()
    def avl(self) -> AVLTree:
        """Build a sample AVL tree for traversal tests."""
        tree = AVLTree()
        for v in [10, 5, 15, 3, 7, 12, 20]:
            tree.insert(v)
        return tree

    def test_inorder(self, avl: AVLTree) -> None:
        """Inorder returns sorted values."""
        assert avl.inorder() == [3, 5, 7, 10, 12, 15, 20]

    def test_preorder(self, avl: AVLTree) -> None:
        """Preorder starts with root."""
        result = avl.preorder()
        assert avl.root is not None
        assert result[0] == avl.root.val
        assert sorted(result) == [3, 5, 7, 10, 12, 15, 20]

    def test_postorder(self, avl: AVLTree) -> None:
        """Postorder ends with root."""
        result = avl.postorder()
        assert avl.root is not None
        assert result[-1] == avl.root.val
        assert sorted(result) == [3, 5, 7, 10, 12, 15, 20]

    def test_level_order(self, avl: AVLTree) -> None:
        """Level order first level is root."""
        result = avl.level_order()
        assert avl.root is not None
        assert result[0] == [avl.root.val]
        assert len(result) == avl.height() + 1


class TestAVLTreeMinMax:
    """Tests for min/max on AVLTree."""

    def test_min(self) -> None:
        """Find min returns smallest value."""
        tree = AVLTree()
        for v in [10, 5, 15, 3, 7]:
            tree.insert(v)
        assert tree.find_min() == 3

    def test_max(self) -> None:
        """Find max returns largest value."""
        tree = AVLTree()
        for v in [10, 5, 15, 3, 7]:
            tree.insert(v)
        assert tree.find_max() == 15

    def test_min_empty_raises(self) -> None:
        """Find min on empty tree raises EmptyTreeError."""
        with pytest.raises(EmptyTreeError):
            AVLTree().find_min()

    def test_max_empty_raises(self) -> None:
        """Find max on empty tree raises EmptyTreeError."""
        with pytest.raises(EmptyTreeError):
            AVLTree().find_max()


class TestAVLTreeDunder:
    """Tests for dunder methods on AVLTree."""

    def test_len(self) -> None:
        """Len tracks insertions."""
        tree = AVLTree()
        assert len(tree) == 0
        tree.insert(10)
        assert len(tree) == 1

    def test_contains(self) -> None:
        """In operator uses search."""
        tree = AVLTree()
        tree.insert(10)
        assert 10 in tree
        assert 99 not in tree

    def test_bool(self) -> None:
        """Bool reflects emptiness."""
        tree = AVLTree()
        assert not tree
        tree.insert(10)
        assert tree

    def test_repr(self) -> None:
        """Repr includes class name."""
        tree = AVLTree()
        assert "AVLTree" in repr(tree)

    def test_str(self) -> None:
        """Str includes node values."""
        tree = AVLTree()
        tree.insert(10)
        assert "10" in str(tree)

    def test_iter(self) -> None:
        """Iter yields sorted values."""
        tree = AVLTree()
        for v in [10, 5, 15]:
            tree.insert(v)
        assert list(tree) == [5, 10, 15]
