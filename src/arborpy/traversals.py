"""Traversal algorithms for binary trees."""

from __future__ import annotations

from collections import deque
from typing import Any

from arborpy.node import Node


def inorder(root: Node | None) -> list[Any]:
    """Return values from an inorder traversal (left, root, right).

    This produces sorted output for a binary search tree.

    Args:
        root: The root node of the tree.

    Returns:
        List of values in inorder sequence.

    Example:
        >>> from arborpy.node import Node
        >>> root = Node(2, Node(1), Node(3))
        >>> inorder(root)
        [1, 2, 3]
    """
    if root is None:
        return []
    return [*inorder(root.left), root.val, *inorder(root.right)]


def preorder(root: Node | None) -> list[Any]:
    """Return values from a preorder traversal (root, left, right).

    Args:
        root: The root node of the tree.

    Returns:
        List of values in preorder sequence.

    Example:
        >>> from arborpy.node import Node
        >>> root = Node(2, Node(1), Node(3))
        >>> preorder(root)
        [2, 1, 3]
    """
    if root is None:
        return []
    return [root.val, *preorder(root.left), *preorder(root.right)]


def postorder(root: Node | None) -> list[Any]:
    """Return values from a postorder traversal (left, right, root).

    Args:
        root: The root node of the tree.

    Returns:
        List of values in postorder sequence.

    Example:
        >>> from arborpy.node import Node
        >>> root = Node(2, Node(1), Node(3))
        >>> postorder(root)
        [1, 3, 2]
    """
    if root is None:
        return []
    return [*postorder(root.left), *postorder(root.right), root.val]


def level_order(root: Node | None) -> list[list[Any]]:
    """Return values from a level-order (breadth-first) traversal.

    Each inner list represents one level of the tree.

    Args:
        root: The root node of the tree.

    Returns:
        List of lists, where each inner list contains values at that level.

    Example:
        >>> from arborpy.node import Node
        >>> root = Node(1, Node(2), Node(3))
        >>> level_order(root)
        [[1], [2, 3]]
    """
    if root is None:
        return []

    result: list[list[Any]] = []
    queue: deque[Node] = deque([root])

    while queue:
        level_size = len(queue)
        current_level: list[Any] = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        result.append(current_level)

    return result
