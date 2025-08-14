# VerseVaani Makefile for development commands
# Requires uv (https://github.com/astral-sh/uv)

.PHONY: help install install-dev sync format lint test clean run

help: ## Show this help message
	@echo "VerseVaani Development Commands"
	@echo "==============================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install production dependencies
	uv pip install -r requirements.txt

install-dev: ## Install development dependencies
	uv pip install -e ".[dev]"

sync: ## Sync all dependencies (production + development)
	uv pip sync requirements.txt
	uv pip install -e ".[dev]"

format: ## Format code with ruff
	uv run ruff format .
	uv run ruff check --fix .

lint: ## Lint code with ruff and mypy
	uv run ruff check .
	uv run mypy .

test: ## Run tests with pytest
	uv run pytest test_versevaani.py -v

test-cov: ## Run tests with coverage
	uv run pytest test_versevaani.py -v --cov=. --cov-report=html --cov-report=term

clean: ## Clean cache and temporary files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete

run: ## Run the Streamlit application
	uv run streamlit run streamlit_app.py

dev: ## Setup development environment
	@echo "Setting up VerseVaani development environment..."
	uv venv
	uv pip install -e ".[dev]"
	@echo "Development environment ready!"
	@echo "Activate with: source .venv/bin/activate (Unix) or .venv\\Scripts\\activate (Windows)"

check: ## Run all checks (format, lint, test)
	$(MAKE) format
	$(MAKE) lint
	$(MAKE) test

ci: ## Run CI pipeline (lint, test without auto-fix)
	uv run ruff check .
	uv run mypy .
	uv run pytest test_versevaani.py -v --cov=. --cov-report=term

# Windows-specific commands
install-windows: ## Install dependencies on Windows
	uv.exe pip install -r requirements.txt

install-dev-windows: ## Install development dependencies on Windows
	uv.exe pip install -e ".[dev]"

format-windows: ## Format code on Windows
	uv.exe run ruff format .
	uv.exe run ruff check --fix .

test-windows: ## Run tests on Windows
	uv.exe run pytest test_versevaani.py -v

run-windows: ## Run application on Windows
	uv.exe run streamlit run streamlit_app.py
