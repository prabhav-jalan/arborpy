"""Binary tree and binary search tree implementations."""

from __future__ import annotations

from typing import Any

from arborpy.exceptions import DuplicateKeyError, EmptyTreeError, NodeNotFoundError
from arborpy.node import Node
from arborpy.traversals import inorder, level_order, postorder, preorder
from arborpy.visualize import pretty_str


class BinarySearchTree:
    """A binary search tree (BST) implementation.

    A BST maintains the invariant that for every node, all values in its left
    subtree are smaller and all values in its right subtree are larger.

    Attributes:
        root: The root node of the tree.
        size: The number of nodes in the tree.

    Example:
        >>> bst = BinarySearchTree()
        >>> for val in [5, 3, 7, 1, 4]:
        ...     bst.insert(val)
        >>> bst.search(4)
        True
        >>> bst.inorder()
        [1, 3, 4, 5, 7]
        >>> len(bst)
        5
    """

    def __init__(self) -> None:
        """Initialize an empty binary search tree."""
        self.root: Node | None = None
        self.size: int = 0

    def __len__(self) -> int:
        """Return the number of nodes in the tree."""
        return self.size

    def __bool__(self) -> bool:
        """Return True if the tree is non-empty."""
        return self.size > 0

    def __contains__(self, val: Any) -> bool:
        """Check if a value exists in the tree.

        Args:
            val: The value to search for.

        Returns:
            True if the value is found.

        Example:
            >>> bst = BinarySearchTree()
            >>> bst.insert(5)
            >>> 5 in bst
            True
            >>> 99 in bst
            False
        """
        return self.search(val)

    def __repr__(self) -> str:
        """Return a string representation of the tree."""
        return f"BinarySearchTree(size={self.size})"

    def __str__(self) -> str:
        """Return a pretty-printed visualization of the tree."""
        if self.root is None:
            return "(empty tree)"
        return pretty_str(self.root)

    def insert(self, val: Any) -> None:
        """Insert a value into the BST.

        Args:
            val: The value to insert.

        Raises:
            DuplicateKeyError: If the value already exists in the tree.

        Example:
            >>> bst = BinarySearchTree()
            >>> bst.insert(5)
            >>> bst.insert(3)
            >>> bst.inorder()
            [3, 5]
        """
        self.root = self._insert(self.root, val)
        self.size += 1

    def _insert(self, node: Node | None, val: Any) -> Node:
        """Recursively insert a value into the subtree.

        Args:
            node: Current node in the recursion.
            val: The value to insert.

        Returns:
            The node after insertion.

        Raises:
            DuplicateKeyError: If the value already exists.
        """
        if node is None:
            return Node(val)

        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        else:
            raise DuplicateKeyError(val)

        return node

    def search(self, val: Any) -> bool:
        """Search for a value in the BST.

        Args:
            val: The value to search for.

        Returns:
            True if the value exists, False otherwise.

        Example:
            >>> bst = BinarySearchTree()
            >>> bst.insert(5)
            >>> bst.search(5)
            True
            >>> bst.search(99)
            False
        """
        return self._search(self.root, val)

    def _search(self, node: Node | None, val: Any) -> bool:
        """Recursively search for a value.

        Args:
            node: Current node in the recursion.
            val: The value to search for.

        Returns:
            True if found, False otherwise.
        """
        if node is None:
            return False
        if val == node.val:
            return True
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

    def delete(self, val: Any) -> None:
        """Delete a value from the BST.

        Args:
            val: The value to delete.

        Raises:
            NodeNotFoundError: If the value is not found.

        Example:
            >>> bst = BinarySearchTree()
            >>> for v in [5, 3, 7]:
            ...     bst.insert(v)
            >>> bst.delete(3)
            >>> bst.inorder()
            [5, 7]
        """
        if not self.search(val):
            raise NodeNotFoundError(val)
        self.root = self._delete(self.root, val)
        self.size -= 1

    def _delete(self, node: Node | None, val: Any) -> Node | None:
        """Recursively delete a value from the subtree.

        Args:
            node: Current node in the recursion.
            val: The value to delete.

        Returns:
            The node after deletion.
        """
        if node is None:
            return None

        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Node with two children: get inorder successor
            successor = self._find_min(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)

        return node

    def _find_min(self, node: Node) -> Node:
        """Find the node with the minimum value in a subtree.

        Args:
            node: Root of the subtree.

        Returns:
            The node with the smallest value.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_min(self) -> Any:
        """Find the minimum value in the tree.

        Returns:
            The minimum value.

        Raises:
            EmptyTreeError: If the tree is empty.

        Example:
            >>> bst = BinarySearchTree()
            >>> for v in [5, 3, 7, 1]:
            ...     bst.insert(v)
            >>> bst.find_min()
            1
        """
        if self.root is None:
            raise EmptyTreeError()
        return self._find_min(self.root).val

    def find_max(self) -> Any:
        """Find the maximum value in the tree.

        Returns:
            The maximum value.

        Raises:
            EmptyTreeError: If the tree is empty.

        Example:
            >>> bst = BinarySearchTree()
            >>> for v in [5, 3, 7, 1]:
            ...     bst.insert(v)
            >>> bst.find_max()
            7
        """
        if self.root is None:
            raise EmptyTreeError()
        current = self.root
        while current.right is not None:
            current = current.right
        return current.val

    def height(self) -> int:
        """Calculate the height of the tree.

        An empty tree has height -1, a single node has height 0.

        Returns:
            The height of the tree.

        Example:
            >>> bst = BinarySearchTree()
            >>> bst.height()
            -1
            >>> bst.insert(5)
            >>> bst.height()
            0
        """
        return self._height(self.root)

    def _height(self, node: Node | None) -> int:
        """Recursively calculate the height of a subtree.

        Args:
            node: Root of the subtree.

        Returns:
            The height of the subtree.
        """
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def inorder(self) -> list[Any]:
        """Return values in inorder sequence (sorted for BST).

        Returns:
            Sorted list of values.
        """
        return inorder(self.root)

    def preorder(self) -> list[Any]:
        """Return values in preorder sequence.

        Returns:
            List of values in preorder.
        """
        return preorder(self.root)

    def postorder(self) -> list[Any]:
        """Return values in postorder sequence.

        Returns:
            List of values in postorder.
        """
        return postorder(self.root)

    def level_order(self) -> list[list[Any]]:
        """Return values in level-order (breadth-first).

        Returns:
            List of lists, each containing values at that level.
        """
        return level_order(self.root)
