"""Abstract base class for tree data structures."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from arborpy.node import Node
from arborpy.traversals import inorder, level_order, postorder, preorder
from arborpy.visualize import pretty_str


class BaseTree(ABC):
    """Abstract base class for binary tree implementations.

    Provides a common interface and shared functionality for all binary
    tree variants (BST, AVL, Red-Black, etc.). Subclasses must implement
    the core ``_insert`` and ``_delete`` operations.

    Attributes:
        root: The root node of the tree.
        size: The number of nodes in the tree.
    """

    def __init__(self) -> None:
        """Initialize an empty tree."""
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
        """
        return self.search(val)

    def __repr__(self) -> str:
        """Return a string representation of the tree."""
        return f"{type(self).__name__}(size={self.size})"

    def __str__(self) -> str:
        """Return a pretty-printed visualization of the tree."""
        if self.root is None:
            return "(empty tree)"
        return pretty_str(self.root)

    @abstractmethod
    def _insert(self, node: Node | None, val: Any) -> Node:
        """Insert a value into the subtree rooted at node.

        Args:
            node: Current node in the recursion.
            val: The value to insert.

        Returns:
            The root of the subtree after insertion.
        """

    @abstractmethod
    def _delete(self, node: Node | None, val: Any) -> Node | None:
        """Delete a value from the subtree rooted at node.

        Args:
            node: Current node in the recursion.
            val: The value to delete.

        Returns:
            The root of the subtree after deletion.
        """

    def insert(self, val: Any) -> None:
        """Insert a value into the tree.

        Args:
            val: The value to insert.

        Raises:
            DuplicateKeyError: If the value already exists in the tree.
        """
        self.root = self._insert(self.root, val)
        self.size += 1

    def delete(self, val: Any) -> None:
        """Delete a value from the tree.

        Args:
            val: The value to delete.

        Raises:
            NodeNotFoundError: If the value is not found.
        """
        from arborpy.exceptions import NodeNotFoundError

        if not self.search(val):
            raise NodeNotFoundError(val)
        self.root = self._delete(self.root, val)
        self.size -= 1

    def search(self, val: Any) -> bool:
        """Search for a value in the tree.

        Args:
            val: The value to search for.

        Returns:
            True if the value exists, False otherwise.
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

    def _find_min_node(self, node: Node) -> Node:
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
        """
        from arborpy.exceptions import EmptyTreeError

        if self.root is None:
            raise EmptyTreeError()
        return self._find_min_node(self.root).val

    def find_max(self) -> Any:
        """Find the maximum value in the tree.

        Returns:
            The maximum value.

        Raises:
            EmptyTreeError: If the tree is empty.
        """
        from arborpy.exceptions import EmptyTreeError

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
