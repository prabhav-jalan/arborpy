"""AVL Tree implementation."""

from __future__ import annotations

from typing import Any

from arborpy.base import BaseTree
from arborpy.node import AVLNode, Node


class AVLTree(BaseTree):
    """A self-balancing AVL tree.

    An AVL tree maintains the invariant that the heights of the left
    and right subtrees of every node differ by at most one. Rotations
    are performed after insertions and deletions to restore balance.

    Example:
        >>> avl = AVLTree()
        >>> for v in [10, 20, 30]:
        ...     avl.insert(v)
        >>> avl.root.val  # 20, not 10 — tree rebalanced
        20
        >>> avl.height()
        1
    """

    def _get_height(self, node: AVLNode | None) -> int:
        """Return the height of a node, or -1 if None.

        Args:
            node: The node to query.

        Returns:
            The stored height, or -1 for a null node.
        """
        if node is None:
            return -1
        return node.height

    def _update_height(self, node: AVLNode) -> None:
        """Recalculate and store the height of a node.

        Args:
            node: The node whose height to update.
        """
        node.height = 1 + max(
            self._get_height(node.left),  # type: ignore[arg-type]
            self._get_height(node.right),  # type: ignore[arg-type]
        )

    def _balance_factor(self, node: AVLNode) -> int:
        """Calculate the balance factor of a node.

        The balance factor is defined as height(left) - height(right).

        Args:
            node: The node to query.

        Returns:
            The balance factor (negative means right-heavy).
        """
        return self._get_height(node.left) - self._get_height(  # type: ignore[arg-type]
            node.right,  # type: ignore[arg-type]
        )

    def _rotate_right(self, z: AVLNode) -> AVLNode:
        """Perform a right rotation around node z.

        Args:
            z: The unbalanced node.

        Returns:
            The new root of the rotated subtree.
        """
        y = z.left
        assert isinstance(y, AVLNode)
        t3 = y.right

        y.right = z
        z.left = t3

        self._update_height(z)
        self._update_height(y)

        return y

    def _rotate_left(self, z: AVLNode) -> AVLNode:
        """Perform a left rotation around node z.

        Args:
            z: The unbalanced node.

        Returns:
            The new root of the rotated subtree.
        """
        y = z.right
        assert isinstance(y, AVLNode)
        t2 = y.left

        y.left = z
        z.right = t2

        self._update_height(z)
        self._update_height(y)

        return y

    def _rebalance(self, node: AVLNode) -> AVLNode:
        """Rebalance a node if its balance factor exceeds ±1.

        Applies the appropriate single or double rotation based on the
        balance factor and the child's balance factor.

        Args:
            node: The node to rebalance.

        Returns:
            The new root of the rebalanced subtree.
        """
        self._update_height(node)
        bf = self._balance_factor(node)

        # Left-heavy
        if bf > 1:
            assert isinstance(node.left, AVLNode)
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right-heavy
        if bf < -1:
            assert isinstance(node.right, AVLNode)
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _insert(self, node: Node | None, val: Any) -> Node:
        """Insert a value into the subtree rooted at node.

        Args:
            node: Current node in the recursion.
            val: The value to insert.

        Returns:
            The root of the subtree after insertion and rebalancing.

        Raises:
            DuplicateKeyError: If the value already exists.
        """
        from arborpy.exceptions import DuplicateKeyError

        if node is None:
            return AVLNode(val)

        if val == node.val:
            raise DuplicateKeyError(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)

        assert isinstance(node, AVLNode)
        return self._rebalance(node)

    def _delete(self, node: Node | None, val: Any) -> Node | None:
        """Delete a value from the subtree rooted at node.

        Args:
            node: Current node in the recursion.
            val: The value to delete.

        Returns:
            The root of the subtree after deletion and rebalancing.
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

        assert isinstance(node, AVLNode)
        return self._rebalance(node)
