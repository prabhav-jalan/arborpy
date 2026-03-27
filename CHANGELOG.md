# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

## [0.1.1] - 2026-03-27

### Fixed
- Removed broken documentation URL from PyPI links
- Broadened Python version support to >=3.10

## [0.1.0] - 2026-03-27

### Added
- `Node` class with value storage, left/right children, and leaf detection
- `BinarySearchTree` with insert, delete, search, find_min, find_max, height
- Traversals: inorder, preorder, postorder, level-order
- ASCII pretty-print tree visualization
- JSON and dict serialization/deserialization
- Custom exceptions: EmptyTreeError, NodeNotFoundError, DuplicateKeyError
- Full test suite with 77 tests
- CI pipeline with GitHub Actions (lint, type check, test)
- Type hints throughout (PEP 561 compatible)
