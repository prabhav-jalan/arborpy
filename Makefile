.PHONY: test lint format typecheck clean build check

test:
	uv run pytest

lint:
	uv run ruff check src/ tests/

format:
	uv run ruff format src/ tests/

typecheck:
	uv run mypy src/

check: lint typecheck test

clean:
	rm -rf dist/ build/ *.egg-info .pytest_cache .mypy_cache htmlcov/

build: clean
	uv build
