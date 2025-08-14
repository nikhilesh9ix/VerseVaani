# 🤝 Contributing to VerseVaani

First and foremost, thank you for considering contributing to VerseVaani! Your contributions help us bring ancient Sanskrit wisdom to the modern world.

## 🌟 How Can I Contribute?

There are many ways to contribute to VerseVaani, whether you are a developer, a Sanskrit student, or a user who has a great idea.

### 🐛 Report Bugs
- If you find a bug, please check the [Issues](https://code.swecha.org/nikhilesh9ix/versevaani/-/issues) to see if it has already been reported.
- If not, open a new issue with a clear title and description. Include as much detail as possible to help us reproduce the bug.

### ✨ Suggest Features
- We love new ideas! Check our [Roadmap](https://code.swecha.org/nikhilesh9ix/versevaani/-/issues?label_name%5B%5D=roadmap) or existing issues to see if your idea is already planned.
- If not, feel free to open a new issue describing the new feature and why you think it would be valuable.

### 🧑‍💻 Code Contributions
- **Fixes:** Pick an existing bug from the issue tracker and submit a fix.
- **Features:** Help us implement features from our roadmap, such as:
  - Adding dropdown for Hindi and Telugu output.
  - Integrating Text-to-Speech (TTS) for audio output.
  - Implementing RAG (Retrieval-Augmented Generation) for Bhagavad Gita lookup.
- **Prompt Tuning:** As described in our report, the system prompt is key to the assistant's personality. We welcome suggestions and pull requests to improve the prompt's tone and effectiveness.

## 🚀 Getting Started

To get a local copy of the project running, follow these simple steps.

1.  **Fork and Clone:** Fork the repository on GitLab and clone your fork to your local machine.
    ```bash
    git clone https://code.swecha.org/nikhilesh9ix/versevaani.git
    cd versevaani
    ```

2.  **Install uv:** We use `uv` for fast Python package management. Install it first:
    ```bash
    # On macOS and Linux
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    # On Windows
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    
    # Or with pip
    pip install uv
    ```

3.  **Set up Development Environment:** Use our development scripts:
    ```bash
    # Unix/Linux/macOS
    make dev
    
    # Windows PowerShell
    .\dev.ps1 dev
    ```

4.  **Set up Environment Variables:** You will need an OpenRouter API key.
    - Go to [OpenRouter.ai](https://openrouter.ai) to get your API key.
    - Create a `.env` file in the root of the project and add your key:
    ```env
    OPENROUTER_API_KEY=sk-or-...
    ```

5.  **Run Tests:** Ensure everything works:
    ```bash
    # Unix/Linux/macOS
    make test
    
    # Windows PowerShell
    .\dev.ps1 test
    ```

6.  **Run the App:** Start the Streamlit application:
    ```bash
    # Unix/Linux/macOS
    make run
    
    # Windows PowerShell
    .\dev.ps1 run
    ```

## 📜 Contribution Workflow

### Development Workflow

1.  Create a new branch for your changes: `git checkout -b feature/my-cool-feature`.
2.  Make your changes following our code standards (see below).
3.  Format and lint your code:
    ```bash
    # Unix/Linux/macOS
    make format
    make lint
    
    # Windows PowerShell
    .\dev.ps1 format
    .\dev.ps1 lint
    ```
4.  Run tests to ensure everything works:
    ```bash
    # Unix/Linux/macOS
    make test
    
    # Windows PowerShell
    .\dev.ps1 test
    ```
5.  Commit your changes with a descriptive message: `git commit -m "feat: add my cool feature"`.
6.  Push your branch to your forked repository: `git push origin feature/my-cool-feature`.
7.  Open a new Merge Request on the main repository and describe your changes.

### Code Standards

We use **Ruff** for code formatting and linting. Please ensure your code follows these standards:

- **Formatting**: Run `make format` or `.\dev.ps1 format` before committing
- **Linting**: Run `make lint` or `.\dev.ps1 lint` to check for issues
- **Type Hints**: Add type hints to all function parameters and return values
- **Docstrings**: Document all classes and methods with Google-style docstrings
- **Testing**: Add tests for new functionality

### Available Commands

We provide convenient commands for development:

```bash
# Unix/Linux/macOS (using Makefile)
make help           # Show all available commands
make install        # Install production dependencies
make install-dev    # Install development dependencies
make format         # Format code with Ruff
make lint           # Lint code with Ruff and MyPy
make test           # Run tests
make test-cov       # Run tests with coverage
make clean          # Clean cache files
make run            # Run the application
make check          # Run format + lint + test
make ci             # Run CI pipeline

# Windows (using PowerShell script)
.\dev.ps1 help      # Show all available commands
.\dev.ps1 install   # Install production dependencies
.\dev.ps1 install-dev # Install development dependencies
.\dev.ps1 format    # Format code with Ruff
.\dev.ps1 lint      # Lint code with Ruff and MyPy
.\dev.ps1 test      # Run tests
.\dev.ps1 run       # Run the application
```

## 🪪 License

By contributing, you agree that your contributions will be licensed under the same GNU Affero General Public License v3.0 that covers the project.