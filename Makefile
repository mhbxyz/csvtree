.PHONY: help lint typecheck test security

help:
	@echo
	@echo "Usage: make <target>"
	@echo
	@echo "Available targets:"
	@echo "  lint       Run code linting (ruff + isort) on src/"
	@echo "  typecheck  Run static type checks with mypy on src/"
	@echo "  test       Run tests under coverage (pytest)"
	@echo "  security   Run security analysis with bandit"
	@echo

lint:
	uv run ruff check src/
	uv run isort src/

typecheck:
	uv run mypy src/

test:
	uv run coverage run -m pytest

security:
	uv run bandit -c config/bandit.yaml -r src/

ci:
	act push -P ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-latest
