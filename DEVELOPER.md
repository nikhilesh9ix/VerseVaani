# VerseVaani Developer Documentation

## Architecture Overview

VerseVaani follows a modular architecture with clear separation of concerns:

```
├── streamlit_app.py    # Main UI application
├── config.py          # Configuration management
├── api_client.py      # OpenRouter API communication
├── utils.py           # Input validation and processing
└── test_versevaani.py # Comprehensive test suite
```

## Core Components

### 1. Configuration Management (`config.py`)

The `Config` class handles all application configuration:

- **API Key Management**: Securely retrieves API keys from environment variables or Streamlit secrets
- **Model Configuration**: Sets default model parameters (temperature, max_tokens, etc.)
- **Security Headers**: Generates proper HTTP headers for API requests

```python
from config import config

# Check if properly configured
if config.is_configured():
    headers = config.get_headers()
```

### 2. API Client (`api_client.py`)

The `OpenRouterClient` class manages all communication with the OpenRouter API:

- **Error Handling**: Comprehensive error handling for network issues, API errors, timeouts
- **Request Formatting**: Properly formats messages for the AI model
- **Response Processing**: Extracts and validates responses from the API

```python
from api_client import openrouter_client

success, response = openrouter_client.send_message(messages)
if success:
    print(response)
else:
    print(f"Error: {response}")
```

### 3. Input Validation (`utils.py`)

The `InputValidator` class provides intelligent input processing:

- **Sanskrit Detection**: Identifies Devanagari script and IAST transliteration
- **Input Validation**: Validates length, content, and format
- **Text Cleaning**: Normalizes and cleans user input
- **Type Classification**: Distinguishes between Sanskrit verses, questions, and general input

```python
from utils import input_validator

is_valid, error, cleaned = input_validator.validate_input(user_text)
if is_valid:
    input_type = input_validator.get_input_type(cleaned)
    suggestions = input_validator.suggest_improvements(cleaned)
```

### 4. Main Application (`streamlit_app.py`)

The main Streamlit application ties everything together:

- **UI Components**: Header, sidebar, chat interface, styling
- **Session Management**: Handles chat history and user sessions
- **Rate Limiting**: Prevents spam and manages API usage
- **Error Display**: User-friendly error messages and suggestions

## Key Features

### Enhanced Error Handling

The application includes comprehensive error handling:

- **API Errors**: 401 (unauthorized), 429 (rate limit), 500 (server error)
- **Network Issues**: Timeouts, connection errors, DNS issues
- **Input Validation**: Empty input, too long/short, harmful content
- **Configuration Issues**: Missing API keys, invalid configuration

### Smart Input Processing

Advanced input processing capabilities:

- **Sanskrit Text Detection**: Automatic detection of Sanskrit content
- **Text Normalization**: Cleaning and formatting of user input
- **Input Classification**: Automatic categorization of input types
- **Helpful Suggestions**: Tips for better results based on input analysis

### Modern UI/UX

Enhanced user interface features:

- **Responsive Design**: Works well on mobile and desktop
- **Beautiful Styling**: Custom CSS with gradients and modern design
- **Informative Sidebar**: Features, examples, and status information
- **Interactive Elements**: Rate limiting feedback, input suggestions

## Testing

Comprehensive test suite covering:

- **Configuration Management**: API key handling, header generation
- **Input Validation**: All validation rules and edge cases
- **API Client**: Success cases, error handling, network issues
- **Sanskrit Detection**: Devanagari, IAST, and romanized text

Run tests with:
```bash
pytest test_versevaani.py -v
```

## Development Workflow

### Setting up Development Environment

1. **Install uv** (fast Python package manager):
   ```bash
   # On macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # On Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Or with pip
   pip install uv
   ```

2. **Clone and Setup**:
   ```bash
   git clone <repository>
   cd versevaani
   ```

3. **Development Environment Setup**:
   ```bash
   # Unix/Linux/macOS
   make dev
   
   # Windows PowerShell
   .\dev.ps1 dev
   ```

4. **Environment Configuration**:
   ```bash
   cp .env.example .env
   # Edit .env with your API key
   ```

5. **Run Tests**:
   ```bash
   # Unix/Linux/macOS
   make test
   
   # Windows PowerShell
   .\dev.ps1 test
   ```

6. **Start Development Server**:
   ```bash
   # Unix/Linux/macOS
   make run
   
   # Windows PowerShell
   .\dev.ps1 run
   ```

### Code Style Guidelines

- **Formatting**: Use `ruff format` for code formatting (configured in pyproject.toml)
- **Linting**: Use `ruff check` for linting and code quality checks
- **Type Hints**: Use type hints for all function parameters and return values
- **Docstrings**: Document all classes and methods with Google-style docstrings
- **Error Handling**: Always handle potential errors gracefully
- **Logging**: Use structured logging for debugging and monitoring
- **Testing**: Write tests for all new functionality

### Development Commands

We provide convenient Make targets and PowerShell scripts for common tasks:

```bash
# Unix/Linux/macOS (using Makefile)
make help           # Show all available commands
make install        # Install production dependencies  
make install-dev    # Install development dependencies
make sync           # Sync all dependencies
make format         # Format code with Ruff
make lint           # Lint code with Ruff and MyPy
make test           # Run tests with pytest
make test-cov       # Run tests with coverage
make clean          # Clean cache and temporary files
make run            # Run the Streamlit application
make dev            # Setup development environment
make check          # Run format + lint + test
make ci             # Run CI pipeline

# Windows (using PowerShell script)
.\dev.ps1 help      # Show all available commands
.\dev.ps1 install   # Install production dependencies
.\dev.ps1 install-dev # Install development dependencies
.\dev.ps1 format    # Format code with Ruff
.\dev.ps1 lint      # Lint code with Ruff and MyPy
.\dev.ps1 test      # Run tests
.\dev.ps1 run       # Run application
.\dev.ps1 dev       # Setup development environment
.\dev.ps1 check     # Run all checks
.\dev.ps1 ci        # Run CI pipeline
```

### Adding New Features

1. **Plan the Feature**: Consider where it fits in the architecture
2. **Write Tests First**: Follow TDD principles where possible
3. **Implement**: Keep functions small and focused
4. **Document**: Update docstrings and this documentation
5. **Test**: Ensure all tests pass before committing

## Performance Considerations

### API Usage Optimization

- **Rate Limiting**: Built-in rate limiting prevents API abuse
- **Request Optimization**: Efficient message formatting and caching
- **Error Recovery**: Graceful handling reduces unnecessary retries

### Memory Management

- **Session State**: Efficient management of chat history
- **Input Processing**: Streaming processing for large inputs
- **Resource Cleanup**: Proper cleanup of resources and connections

## Security Considerations

### API Key Security

- **Environment Variables**: API keys never hardcoded
- **Secrets Management**: Support for Streamlit secrets
- **Header Security**: Proper HTTP headers for API requests

### Input Sanitization

- **XSS Prevention**: Input sanitization prevents script injection
- **Content Validation**: Checks for potentially harmful content
- **Rate Limiting**: Prevents abuse and spam

## Deployment

### Local Deployment

```bash
streamlit run streamlit_app.py
```

### Streamlit Cloud Deployment

1. Push code to GitHub
2. Connect to Streamlit Cloud
3. Add API key to secrets
4. Deploy

### Custom Deployment

The application can be deployed on any platform supporting Python and Streamlit:

- Docker containers
- Heroku
- AWS/GCP/Azure
- VPS servers

## Troubleshooting

### Common Issues

1. **API Key Not Working**:
   - Check if API key is correctly set
   - Verify API key has sufficient credits
   - Check network connectivity

2. **Import Errors**:
   - Ensure all dependencies are installed
   - Check Python version compatibility (3.9+)

3. **Tests Failing**:
   - Check if all dependencies are installed
   - Verify test data and mocks are correct

### Debug Mode

Enable debug logging by setting environment variable:
```bash
export LOG_LEVEL=DEBUG
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## API Reference

### Configuration Class

- `Config()`: Initialize configuration
- `is_configured()`: Check if API key is set
- `get_headers()`: Get HTTP headers for API requests

### OpenRouter Client

- `send_message(messages)`: Send messages to AI model
- Returns: `(success: bool, response: str)`

### Input Validator

- `validate_input(text)`: Validate user input
- `contains_sanskrit(text)`: Check for Sanskrit content
- `get_input_type(text)`: Classify input type
- `suggest_improvements(text)`: Get improvement suggestions

---

For questions or support, please check the [GitHub Issues](https://github.com/nikhilesh9ix/versevaani/issues).
