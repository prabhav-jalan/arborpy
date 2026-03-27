"""Custom exceptions for the ArborPy library."""


class ArborPyError(Exception):
    """Base exception for all ArborPy errors."""


class EmptyTreeError(ArborPyError):
    """Raised when an operation is performed on an empty tree."""

    def __init__(self, message: str = "Tree is empty") -> None:
        """Initialize EmptyTreeError.

        Args:
            message: Error description.
        """
        super().__init__(message)


class NodeNotFoundError(ArborPyError):
    """Raised when a node with the given key is not found in the tree."""

    def __init__(self, key: object) -> None:
        """Initialize NodeNotFoundError.

        Args:
            key: The key that was not found.
        """
        super().__init__(f"Node with key {key!r} not found")
        self.key = key


class DuplicateKeyError(ArborPyError):
    """Raised when attempting to insert a key that already exists."""

    def __init__(self, key: object) -> None:
        """Initialize DuplicateKeyError.

        Args:
            key: The duplicate key.
        """
        super().__init__(f"Key {key!r} already exists in the tree")
        self.key = key
