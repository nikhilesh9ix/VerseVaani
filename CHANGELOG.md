# Changelog

## [0.2.1] - 2025-08-16

### Added
- **VS Code Integration**: Added Ruff extension to recommended extensions
- **Development Environment**: Enhanced VS Code configuration with proper settings, launch, and tasks
- **GitLab Integration**: Updated all documentation to reference GitLab repository as primary

### Enhanced
- **Documentation**: Completely rewritten CONTRIBUTING.md with comprehensive development guidelines
- **Development Workflow**: Improved documentation for cross-platform development setup
- **Code Quality**: Enhanced VS Code settings for automatic formatting and linting

## [0.2.0] - 2025-08-14

### Added
- **Modular Architecture**: Separated code into `config.py`, `api_client.py`, and `utils.py` for better maintainability
- **Enhanced Error Handling**: Comprehensive error management for API failures, network issues, and invalid responses
- **Input Validation**: Smart validation system that detects Sanskrit text and validates input quality
- **Rate Limiting**: Built-in rate limiting to prevent spam and ensure smooth operation
- **Advanced UI Features**: 
  - Beautiful CSS styling with gradient backgrounds
  - Sidebar with features, examples, and status information
  - Welcome message for new users
  - Input suggestions and tips
  - Session analytics and message counting
- **Configuration Management**: Secure API key handling through environment variables and Streamlit secrets
- **Test Suite**: Comprehensive test coverage with pytest for all major components
- **Documentation**: Enhanced README with detailed setup instructions and feature descriptions
- **Environment Setup**: Added `.env.example` and improved `.gitignore`
- **Sanskrit Text Detection**: Automatic detection of Devanagari script and IAST transliteration
- **Input Type Classification**: Distinguishes between Sanskrit verses, questions, and general input
- **Text Cleaning**: Automatic cleaning and normalization of user input
- **Responsive Design**: Mobile-friendly interface improvements

### Enhanced
- **System Prompt**: Improved AI assistant personality with more detailed instructions
- **API Communication**: Better request handling with timeout management and proper headers
- **User Experience**: More informative error messages and helpful suggestions
- **Security**: Input sanitization and harmful content detection
- **Performance**: Optimized API calls and reduced unnecessary requests

### Technical Improvements
- **Type Hints**: Added comprehensive type hints throughout the codebase
- **Logging**: Structured logging for better debugging and monitoring
- **Error Recovery**: Graceful handling of various failure scenarios
- **Code Organization**: Clean separation of concerns and modular design
- **Testing Infrastructure**: Unit tests for all major functionality

### Documentation
- **Setup Guide**: Detailed installation and configuration instructions
- **API Documentation**: Clear explanation of all components and their usage
- **Contributing Guidelines**: Enhanced contribution workflow and standards
- **Project Structure**: Clear overview of codebase organization

## [0.1.0] - 2025-08-05

### Added
- Initial deployment of core VerseVaani functionality
- Poetic English translation for Sanskrit shlokas
- Word-by-word meaning breakdown
- Explanation of spiritual and cultural context
- API integration with `mistralai/mistral-7b-instruct-v0.3` via OpenRouter
- Streamlit-based chat interface hosted on Hugging Face Spaces
- Basic system prompt for the `ShlokaSevak` assistant persona
- Initial project files including `README.md`, `streamlit_app.py`, and `requirements.txt`