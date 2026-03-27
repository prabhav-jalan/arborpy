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

## Pull Request Process

1. Create a branch from `develop`:

```bash
git checkout develop
git pull origin develop
git checkout -b feat/your-feature
```

2. Write your code and tests.

3. Make sure all checks pass:

```bash
make check
```

4. Push and open a PR against `develop`:

```bash
git push -u origin feat/your-feature
```

5. Fill in the PR template.

## Branch Naming

| Prefix | Use for |
|--------|---------|
| `feat/` | New features |
| `fix/` | Bug fixes |
| `docs/` | Documentation |
| `refactor/` | Code refactoring |
| `test/` | Adding or fixing tests |

## Commit Messages

We use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat: add AVL tree implementation`
- `fix: correct BST delete for leaf nodes`
- `docs: update README with new examples`
- `test: add edge case tests for empty tree`
- `refactor: extract rotation logic`
- `chore: update CI configuration`

## Code Style

- Type hints on all public functions and methods
- Google-style docstrings on all public classes and methods
- Line length limit: 88 characters
- Ruff handles formatting and linting automatically via pre-commit
