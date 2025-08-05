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
    git clone [https://code.swecha.org/nikhilesh9ix/versevaani.git](https://code.swecha.org/nikhilesh9ix/versevaani.git)
    cd versevaani
    ```

2.  **Install Dependencies:** We use `uv` for dependency management. Install the required packages with:
    ```bash
    uv pip install -r requirements.txt
    ```

3.  **Set up Environment:** You will need an OpenRouter API key.
    - Go to [OpenRouter.ai](https://openrouter.ai) to get your API key.
    - Create a `.env` file in the root of the project and add your key:
    ```
    OPENROUTER_API_KEY=sk-or-...
    ```

4.  **Run the App:** Start the Streamlit application from your terminal:
    ```bash
    streamlit run streamlit_app.py
    ```

## 📜 Contribution Workflow

1.  Create a new branch for your changes: `git checkout -b feature/my-cool-feature`.
2.  Make your changes and commit them with a descriptive message: `git commit -m "feat: add my cool feature"`.
3.  Push your branch to your forked repository: `git push origin feature/my-cool-feature`.
4.  Open a new Merge Request on the main repository and describe your changes.

## 🪪 License

By contributing, you agree that your contributions will be licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, which is the same license used by this project.