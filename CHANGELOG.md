# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

## [0.1.0] - 2026-03-27

### Added

- `Node` class with value, left/right children, and `is_leaf()` method
- `BinarySearchTree` with insert, delete, search, find_min, find_max, height
- Traversal functions: inorder, preorder, postorder, level_order
- Serialization: to_dict, from_dict, to_json, from_json
- ASCII pretty-print visualization via `print(bst)`
- Custom exceptions: EmptyTreeError, NodeNotFoundError, DuplicateKeyError
- Support for `len(bst)`, `in` operator, and `bool(bst)`
- Full test suite with 77 tests
- CI pipeline with GitHub Actions (Python 3.13, 3.14 on Ubuntu and macOS)
- Type hints throughout (PEP 561 compatible with py.typed marker)
