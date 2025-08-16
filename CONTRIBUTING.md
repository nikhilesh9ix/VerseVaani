# 🤝 Contributing to VerseVaani

First and foremost, thank you for considering contributing to VerseVaani! Your contributions help us bring ancient Sanskrit wisdom to the modern world.

## 🌟 How Can I Contribute?

There are many ways to contribute to VerseVaani, whether you are a developer, a Sanskrit student, or a user who has a great idea.

### 🐛 Report Bugs

- If you find a bug, please check the [Issues](https://code.swecha.org/nikhilesh9ix/versevaani/-/issues) to see if it has already been reported.
- If not, open a new issue with a clear title and description. Include as much detail as possible to help us reproduce the bug.

### ✨ Suggest Features

- We love new ideas! Check our [Issues](https://code.swecha.org/nikhilesh9ix/versevaani/-/issues) or existing discussions to see if your idea is already planned.
- If not, feel free to open a new issue describing the new feature and why you think it would be valuable.

### 🧑‍💻 Code Contributions

- **Fixes:** Pick an existing bug from the issue tracker and submit a fix.
- **Features:** Help us implement features from our roadmap, such as:
  - Adding dropdown for Hindi and Telugu output.
  - Integrating Text-to-Speech (TTS) for audio output.
  - Implementing RAG (Retrieval-Augmented Generation) for Bhagavad Gita lookup.
- **Prompt Tuning:** The system prompt is key to the assistant's personality. We welcome suggestions and pull requests to improve the prompt's tone and effectiveness.

## 🚀 Getting Started

To get a local copy of the project running, follow these simple steps.

1. **Fork and Clone:** Fork the repository on GitLab and clone your fork to your local machine.

   ```bash
   git clone https://code.swecha.org/YOUR_USERNAME/versevaani.git
   cd versevaani
   ```

2. **Install uv:** We use `uv` for fast Python package management. Install it first:

   ```bash
   # On macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # On Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Or with pip
   pip install uv
   ```

3. **Set up Development Environment:** Use our development scripts:

   ```bash
   # Unix/Linux/macOS
   make setup
   
   # Windows PowerShell
   .\dev.ps1 setup
   ```

4. **Set up Environment Variables:** You will need an OpenRouter API key.

   ```env
   OPENROUTER_API_KEY=your-api-key-here
   ```

5. **Run Tests:** Ensure everything works:

   ```bash
   # Unix/Linux/macOS
   make test
   
   # Windows PowerShell
   .\dev.ps1 test
   ```

6. **Run the App:** Start the Streamlit application:

   ```bash
   # Unix/Linux/macOS
   make run
   
   # Windows PowerShell
   .\dev.ps1 run
   ```

## 📋 Development Workflow

1. Create a new branch for your changes: `git checkout -b feature/my-cool-feature`.
2. Make your changes following our code standards (see below).
3. Test your changes: `./dev.ps1 test` or `make test`.
4. Format and lint your code: `./dev.ps1 format` or `make format`.
5. Commit your changes with a descriptive message.
6. Push to your fork and create a Merge Request on GitLab.

## 🎯 Code Standards

We maintain high code quality standards. Please ensure your contributions follow these guidelines:

### Code Quality Tools

- **Formatting:** We use `ruff format` for consistent code formatting
- **Linting:** We use `ruff check` for code quality checks
- **Type Checking:** We use `mypy` for static type analysis
- **Testing:** We use `pytest` for comprehensive test coverage

### Quick Quality Check

Before submitting your PR, run:

```bash
# Windows
.\dev.ps1 lint

# Unix/Linux/macOS  
make lint
```

This will run all quality checks (formatting, linting, type checking).

### Code Style Guidelines

- **Type Hints:** Add type hints to all public functions and methods
- **Documentation:** Add docstrings to all public functions and classes
- **Error Handling:** Include comprehensive error handling with meaningful messages
- **Testing:** Write tests for new functionality
- **Comments:** Use clear, concise comments to explain complex logic

## 🧪 Testing

We maintain comprehensive test coverage. When adding new features:

1. **Write Tests First:** Consider using Test-Driven Development (TDD)
2. **Test Coverage:** Aim for high test coverage on new code
3. **Test Types:** Include unit tests for individual functions and integration tests for workflows

Run tests with:

```bash
# Basic test run
uv run pytest

# Test with coverage report
uv run pytest --cov=. --cov-report=term-missing
```

## 📝 Documentation

Good documentation helps everyone! When contributing:

- **Update README:** If you add new features, update the README.md
- **Add Examples:** Include usage examples for new features
- **Update CHANGELOG:** Add your changes to CHANGELOG.md
- **Code Comments:** Comment complex logic or algorithms

## 🤝 Community Guidelines

- **Be Respectful:** Treat all community members with respect and kindness
- **Be Patient:** Remember that we're all learning and growing
- **Be Constructive:** Provide helpful, actionable feedback
- **Be Inclusive:** Welcome contributors from all backgrounds and experience levels

## 🐛 Reporting Issues

When reporting bugs, please include:

- **Environment Information:** OS, Python version, browser (if applicable)
- **Steps to Reproduce:** Clear, step-by-step instructions
- **Expected vs Actual Behavior:** What you expected to happen vs what actually happened
- **Screenshots:** If applicable, include screenshots or error messages
- **Additional Context:** Any other relevant information

## 💡 Feature Requests

When suggesting new features:

- **Use Case:** Describe the problem this feature would solve
- **Proposed Solution:** Suggest how the feature might work
- **Alternatives:** Consider alternative approaches
- **Additional Context:** Any other relevant information or examples

## 📄 License

By contributing, you agree that your contributions will be licensed under the same GNU Affero General Public License v3.0 that covers the project.