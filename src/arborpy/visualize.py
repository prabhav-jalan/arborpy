"""Pretty-print visualization for binary trees."""

from __future__ import annotations

from arborpy.node import Node


def pretty_str(root: Node | None) -> str:
    r"""Generate an ASCII art representation of a binary tree.

    Args:
        root: The root node of the tree.

    Returns:
        A multi-line string showing the tree structure.

    Example:
        >>> from arborpy.node import Node
        >>> root = Node(5, Node(3, Node(1), Node(4)), Node(7))
        >>> print(pretty_str(root))
            5
           / \\
          3   7
         / \\
        1   4
    """
    if root is None:
        return "(empty tree)"

    lines = _build_lines(root)
    return "\n".join(lines)


def _build_lines(node: Node | None) -> list[str]:
    """Recursively build display lines for a node and its subtrees.

    Args:
        node: The current node.

    Returns:
        List of strings representing the visual lines.
    """
    if node is None:
        return []

    val_str = str(node.val)

    # Base case: leaf node
    if node.left is None and node.right is None:
        return [val_str]

    # Only right child
    if node.left is None:
        right_lines = _build_lines(node.right)
        first_line = val_str + " \\"
        below = [" " * len(val_str) + "  " + line for line in right_lines]
        return [first_line, *below]

    # Only left child
    if node.right is None:
        left_lines = _build_lines(node.left)
        first_line = (
            " " * (len(left_lines[0]) - len(left_lines[0].lstrip()) + len(val_str))
            + val_str
        )
        connector = " " * len(val_str) + " /"
        padded = _build_lines(node.left)
        return [val_str, connector, *padded]

    # Both children present
    left_lines = _build_lines(node.left)
    right_lines = _build_lines(node.right)

    # Calculate widths
    left_width = max(len(line) for line in left_lines)
    right_width = max(len(line) for line in right_lines)

    # Pad left lines to uniform width
    left_padded = [line.ljust(left_width) for line in left_lines]
    right_padded = [line.ljust(right_width) for line in right_lines]

    # Build the root line centered above
    gap = 3
    root_pos = left_width + 1
    root_line = " " * root_pos + val_str

    # Build connector line
    connector = " " * (left_width) + " / \\"

    # Merge left and right subtree lines
    max_height = max(len(left_padded), len(right_padded))
    left_padded.extend([" " * left_width] * (max_height - len(left_padded)))
    right_padded.extend([" " * right_width] * (max_height - len(right_padded)))

    merged = []
    for left_l, right_l in zip(left_padded, right_padded, strict=False):
        merged.append(left_l + " " * gap + right_l)

    return [root_line, connector, *merged]
