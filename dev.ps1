# VerseVaani Development Scripts for Windows
# PowerShell script to replace Makefile functionality

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("help", "install", "install-dev", "sync", "format", "lint", "test", "test-cov", "clean", "run", "dev", "check", "ci")]
    [string]$Command
)

function Show-Help {
    Write-Host "VerseVaani Development Commands" -ForegroundColor Cyan
    Write-Host "===============================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "install     " -ForegroundColor Green -NoNewline; Write-Host "Install production dependencies"
    Write-Host "install-dev " -ForegroundColor Green -NoNewline; Write-Host "Install development dependencies"
    Write-Host "sync        " -ForegroundColor Green -NoNewline; Write-Host "Sync all dependencies"
    Write-Host "format      " -ForegroundColor Green -NoNewline; Write-Host "Format code with ruff"
    Write-Host "lint        " -ForegroundColor Green -NoNewline; Write-Host "Lint code with ruff and mypy"
    Write-Host "test        " -ForegroundColor Green -NoNewline; Write-Host "Run tests with pytest"
    Write-Host "test-cov    " -ForegroundColor Green -NoNewline; Write-Host "Run tests with coverage"
    Write-Host "clean       " -ForegroundColor Green -NoNewline; Write-Host "Clean cache and temporary files"
    Write-Host "run         " -ForegroundColor Green -NoNewline; Write-Host "Run the Streamlit application"
    Write-Host "dev         " -ForegroundColor Green -NoNewline; Write-Host "Setup development environment"
    Write-Host "check       " -ForegroundColor Green -NoNewline; Write-Host "Run all checks (format, lint, test)"
    Write-Host "ci          " -ForegroundColor Green -NoNewline; Write-Host "Run CI pipeline"
}

function Install-Production {
    Write-Host "Installing production dependencies..." -ForegroundColor Yellow
    uv pip install -r requirements.txt
}

function Install-Dev {
    Write-Host "Installing development dependencies..." -ForegroundColor Yellow
    uv pip install -e ".[dev]"
}

function Sync-Dependencies {
    Write-Host "Syncing all dependencies..." -ForegroundColor Yellow
    uv pip sync requirements.txt
    uv pip install -e ".[dev]"
}

function Format-Code {
    Write-Host "Formatting code with ruff..." -ForegroundColor Yellow
    uv run ruff format .
    uv run ruff check --fix .
}

function Lint-Code {
    Write-Host "Linting code..." -ForegroundColor Yellow
    uv run ruff check .
    uv run mypy .
}

function Run-Tests {
    Write-Host "Running tests..." -ForegroundColor Yellow
    uv run pytest test_versevaani.py -v
}

function Run-TestsWithCoverage {
    Write-Host "Running tests with coverage..." -ForegroundColor Yellow
    uv run pytest test_versevaani.py -v --cov=. --cov-report=html --cov-report=term
}

function Clean-Files {
    Write-Host "Cleaning cache and temporary files..." -ForegroundColor Yellow
    Get-ChildItem -Path . -Recurse -Name "*.pyc" | Remove-Item -Force
    Get-ChildItem -Path . -Recurse -Directory -Name "__pycache__" | Remove-Item -Recurse -Force
    Get-ChildItem -Path . -Recurse -Directory -Name ".pytest_cache" | Remove-Item -Recurse -Force
    Get-ChildItem -Path . -Recurse -Directory -Name ".ruff_cache" | Remove-Item -Recurse -Force
    Get-ChildItem -Path . -Recurse -Directory -Name "htmlcov" | Remove-Item -Recurse -Force
    Get-ChildItem -Path . -Recurse -Name ".coverage" | Remove-Item -Force
}

function Run-App {
    Write-Host "Starting VerseVaani application..." -ForegroundColor Yellow
    uv run streamlit run streamlit_app.py
}

function Setup-Dev {
    Write-Host "Setting up VerseVaani development environment..." -ForegroundColor Yellow
    uv venv
    uv pip install -e ".[dev]"
    Write-Host "Development environment ready!" -ForegroundColor Green
    Write-Host "Activate with: .venv\Scripts\activate" -ForegroundColor Cyan
}

function Run-AllChecks {
    Write-Host "Running all checks..." -ForegroundColor Yellow
    Format-Code
    Lint-Code
    Run-Tests
}

function Run-CI {
    Write-Host "Running CI pipeline..." -ForegroundColor Yellow
    uv run ruff check .
    uv run mypy .
    uv run pytest test_versevaani.py -v --cov=. --cov-report=term
}

# Execute the requested command
switch ($Command) {
    "help" { Show-Help }
    "install" { Install-Production }
    "install-dev" { Install-Dev }
    "sync" { Sync-Dependencies }
    "format" { Format-Code }
    "lint" { Lint-Code }
    "test" { Run-Tests }
    "test-cov" { Run-TestsWithCoverage }
    "clean" { Clean-Files }
    "run" { Run-App }
    "dev" { Setup-Dev }
    "check" { Run-AllChecks }
    "ci" { Run-CI }
}
