"""Node classes for tree data structures."""

from __future__ import annotations

from typing import Any


class Node:
    """A node in a binary tree.

    Each node holds a value and optional references to left and right children.

    Attributes:
        val: The value stored in this node.
        left: Reference to the left child node.
        right: Reference to the right child node.

    Example:
        >>> node = Node(10)
        >>> node.left = Node(5)
        >>> node.right = Node(15)
        >>> node.val
        10
        >>> node.left.val
        5
    """

    __slots__ = ("left", "right", "val")

    def __init__(
        self,
        val: Any,
        left: Node | None = None,
        right: Node | None = None,
    ) -> None:
        """Initialize a Node.

        Args:
            val: The value to store in this node.
            left: Optional left child.
            right: Optional right child.
        """
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """Return a string representation of the node."""
        return f"Node({self.val!r})"

    def __eq__(self, other: object) -> bool:
        """Check equality based on value."""
        if not isinstance(other, Node):
            return NotImplemented
        return bool(self.val == other.val)

    def __hash__(self) -> int:
        """Return hash based on value."""
        return hash(self.val)

    def is_leaf(self) -> bool:
        """Check if this node has no children.

        Returns:
            True if the node has no left or right child.

        Example:
            >>> Node(5).is_leaf()
            True
            >>> Node(5, left=Node(3)).is_leaf()
            False
        """
        return self.left is None and self.right is None
