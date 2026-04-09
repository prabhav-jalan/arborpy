# ArborPy 🌳

[![CI](https://github.com/prabhav-jalan/arborpy/actions/workflows/ci.yml/badge.svg)](https://github.com/prabhav-jalan/arborpy/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/arborpy)](https://pypi.org/project/arborpy/)
[![Python versions](https://img.shields.io/pypi/pyversions/arborpy)](https://pypi.org/project/arborpy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive, typed, and well-tested Python library for tree data structures.

## Installation

```bash
pip install arborpy
```

Or with uv:

```bash
uv add arborpy
```

## Quick Start

```python
from arborpy import BinarySearchTree

bst = BinarySearchTree()
for val in [5, 3, 7, 1, 4]:
    bst.insert(val)

print(bst.inorder())    # [1, 3, 4, 5, 7]
print(bst.search(4))    # True
print(5 in bst)         # True
print(len(bst))         # 5
print(bst)              # Pretty-printed tree
```

## Features

### Binary Search Tree

```python
from arborpy import BinarySearchTree

bst = BinarySearchTree()

# Insert values
for val in [5, 3, 7, 1, 4, 6, 8]:
    bst.insert(val)

# Search
bst.search(4)       # True
bst.search(99)      # False

# Delete
bst.delete(3)

# Min and max
bst.find_min()      # 1
bst.find_max()      # 8

# Tree properties
bst.height()        # 2
len(bst)            # 7
```

### AVL Tree

```python
from arborpy import AVLTree

avl = AVLTree()
for val in [10, 20, 30, 25, 28]:
    avl.insert(val)

print(avl)           # Pretty-printed balanced tree
print(avl.inorder()) # [10, 20, 25, 28, 30]
print(avl.height())  # 2 — stays balanced!
```

### Traversals

```python
from arborpy import BinarySearchTree

bst = BinarySearchTree()
for val in [5, 3, 7, 1, 4, 6, 8]:
    bst.insert(val)

bst.inorder()       # [1, 3, 4, 5, 6, 7, 8]
bst.preorder()      # [5, 3, 1, 4, 7, 6, 8]
bst.postorder()     # [1, 4, 3, 6, 8, 7, 5]
bst.level_order()   # [[5], [3, 7], [1, 4, 6, 8]]
```

### Serialization

```python
from arborpy import BinarySearchTree, to_json, from_json, to_dict, from_dict

bst = BinarySearchTree()
for val in [5, 3, 7]:
    bst.insert(val)

# To/from dictionary
d = to_dict(bst.root)
node = from_dict(d)

# To/from JSON
json_str = to_json(bst.root)
node = from_json(json_str)
```

### Standalone Traversal Functions

```python
from arborpy import Node, inorder, preorder, postorder, level_order

# Build a tree manually
root = Node(1, Node(2, Node(4), Node(5)), Node(3))

inorder(root)       # [4, 2, 5, 1, 3]
preorder(root)      # [1, 2, 4, 5, 3]
postorder(root)     # [4, 5, 2, 3, 1]
level_order(root)   # [[1], [2, 3], [4, 5]]
```

## Roadmap

- [x] Binary Search Tree
- [x] Traversals (inorder, preorder, postorder, level-order)
- [x] Serialization (dict, JSON)
- [x] ASCII visualization
- [x] AVL Tree (self-balancing)
- [ ] Min/Max Heap
- [ ] Red-Black Tree
- [ ] Trie (prefix tree)
- [ ] Segment Tree
- [ ] Fenwick Tree (Binary Indexed Tree)
- [ ] N-ary Tree

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE) for details.
