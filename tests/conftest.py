"""Shared test fixtures for ArborPy tests."""

import pytest

from arborpy import BinarySearchTree


@pytest.fixture()
def empty_bst() -> BinarySearchTree:
    """Return an empty BST."""
    return BinarySearchTree()


@pytest.fixture()
def sample_bst() -> BinarySearchTree:
    r"""Return a BST with values [5, 3, 7, 1, 4, 6, 8].

       5
      / \\
      3   7
    / \\ / \\
    1  4 6  8
    """
    bst = BinarySearchTree()
    for val in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(val)
    return bst
