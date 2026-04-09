"""Serialization and deserialization utilities for tree structures."""

from __future__ import annotations

import json
from typing import Any

from arborpy.node import AVLNode, Node


def to_dict(root: Node | None) -> dict[str, Any] | None:
    """Convert a binary tree to a nested dictionary.

    Args:
        root: The root node of the tree.

    Returns:
        A nested dictionary representation, or None if root is None.

    Example:
        >>> from arborpy.node import Node
        >>> root = Node(5, Node(3), Node(7))
        >>> result = to_dict(root)
        >>> result["val"]
        5
    """
    if root is None:
        return None

    result: dict[str, Any] = {
        "val": root.val,
        "left": to_dict(root.left),
        "right": to_dict(root.right),
    }

    if isinstance(root, AVLNode):
        result["type"] = "AVLNode"
        result["height"] = root.height

    return result


def from_dict(data: dict[str, Any] | None) -> Node | None:
    """Reconstruct a binary tree from a nested dictionary.

    Args:
        data: A dictionary with 'val', 'left', and 'right' keys.

    Returns:
        The root node of the reconstructed tree, or None.

    Example:
        >>> d = {"val": 5, "left": None, "right": None}
        >>> node = from_dict(d)
        >>> node.val
        5
    """
    if data is None:
        return None

    if data.get("type") == "AVLNode":
        node: Node = AVLNode(data["val"])
        assert isinstance(node, AVLNode)
        node.height = data.get("height", 0)
    else:
        node = Node(data["val"])

    node.left = from_dict(data.get("left"))
    node.right = from_dict(data.get("right"))

    return node


def to_json(root: Node | None, indent: int = 2) -> str:
    """Serialize a binary tree to a JSON string.

    Args:
        root: The root node of the tree.
        indent: Number of spaces for JSON indentation.

    Returns:
        A JSON string representation of the tree.

    Example:
        >>> from arborpy.node import Node
        >>> root = Node(5)
        >>> print(to_json(root))
        {
          "val": 5,
          "left": null,
          "right": null
        }
    """
    return json.dumps(to_dict(root), indent=indent)


def from_json(json_str: str) -> Node | None:
    """Deserialize a binary tree from a JSON string.

    Args:
        json_str: A JSON string representing the tree.

    Returns:
        The root node of the reconstructed tree, or None.

    Example:
        >>> node = from_json('{"val": 5, "left": null, "right": null}')
        >>> node.val
        5
    """
    data = json.loads(json_str)
    return from_dict(data)
