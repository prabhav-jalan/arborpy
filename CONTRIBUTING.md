# Contributing to ArborPy

Thanks for your interest in contributing! Here's how to get started.

## Development Setup

1. Fork and clone the repo:
   ```bash
   git clone git@github.com:your-username/arborpy.git
   cd arborpy
   ```

2. Install [uv](https://docs.astral.sh/uv/):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Running Tests

```bash
uv run pytest                       # all tests
uv run pytest tests/test_node.py    # single file
uv run pytest -x                    # stop on first failure
uv run pytest -v                    # verbose output
```

## Code Quality

```bash
uv run ruff check src/ tests/       # lint
uv run ruff format src/ tests/      # format
uv run mypy src/                    # type check
```

Or run everything at once:

```bash
make check
```

## Branch Naming

| Prefix | Use for |
|--------|---------|
| `feat/` | New features |
| `fix/` | Bug fixes |
| `docs/` | Documentation |
| `refactor/` | Code refactoring |
| `test/` | Adding or fixing tests |

## Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add AVL tree with self-balancing insert
fix: correct BST delete when node has two children
docs: update README with AVL usage examples
test: add edge case tests for empty tree operations
```

## Pull Request Process

1. Create a feature branch from `develop`
2. Write tests for your changes
3. Ensure all checks pass (`make check`)
4. Submit PR against `develop`
5. Fill in the PR template

## Code Style

- Type hints on all public functions and methods
- Google-style docstrings on all public classes and methods
- Line length limit: 88 characters
- Ruff handles formatting and linting automatically
