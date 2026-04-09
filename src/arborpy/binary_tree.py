"""Binary Search Tree implementation."""

from __future__ import annotations

from typing import Any

from arborpy.base import BaseTree
from arborpy.node import Node


class BinarySearchTree(BaseTree):
    """A binary search tree.

    A BST where each node's left children hold smaller values and
    right children hold larger values. Duplicate keys are not allowed.

    Example:
        >>> bst = BinarySearchTree()
        >>> bst.insert(10)
        >>> bst.insert(5)
        >>> bst.insert(15)
        >>> bst.search(5)
        True
        >>> len(bst)
        3
    """

    def _insert(self, node: Node | None, val: Any) -> Node:
        """Insert a value into the subtree rooted at node.

        Args:
            node: Current node in the recursion.
            val: The value to insert.

        Returns:
            The root of the subtree after insertion.

        Raises:
            DuplicateKeyError: If the value already exists.
        """
        from arborpy.exceptions import DuplicateKeyError

        if node is None:
            return Node(val)

        if val == node.val:
            raise DuplicateKeyError(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)

        return node

    def _delete(self, node: Node | None, val: Any) -> Node | None:
        """Delete a value from the subtree rooted at node.

        Args:
            node: Current node in the recursion.
            val: The value to delete.

        Returns:
            The new root of the subtree after deletion.
        """
        if node is None:
            return None

        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self._find_min_node(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)

        return node
