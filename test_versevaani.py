"""Basic tests for VerseVaani components."""

import os
from unittest.mock import MagicMock, patch

import pytest

from api_client import OpenRouterClient

# Import modules to test
from config import Config
from utils import InputValidator


class TestConfig:
    """Test configuration management."""

    def test_config_without_api_key(self):
        """Test configuration when no API key is set."""
        with patch.dict(os.environ, {}, clear=True):
            config = Config()
            assert not config.is_configured()

    def test_config_with_api_key(self):
        """Test configuration when API key is set."""
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}):
            config = Config()
            assert config.is_configured()
            assert config.api_key == "test-key"

    def test_headers_generation(self):
        """Test API headers generation."""
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}):
            config = Config()
            headers = config.get_headers()
            assert "Authorization" in headers
            assert headers["Authorization"] == "Bearer test-key"
            assert headers["Content-Type"] == "application/json"


class TestInputValidator:
    """Test input validation functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.validator = InputValidator()

    def test_empty_input(self):
        """Test validation of empty input."""
        is_valid, error, cleaned = self.validator.validate_input("")
        assert not is_valid
        assert "Please enter some text" in error

    def test_short_input(self):
        """Test validation of very short input."""
        is_valid, error, cleaned = self.validator.validate_input("hi")
        assert not is_valid
        assert "longer text" in error

    def test_long_input(self):
        """Test validation of very long input."""
        long_text = "a" * 1001
        is_valid, error, cleaned = self.validator.validate_input(long_text)
        assert not is_valid
        assert "too long" in error

    def test_valid_sanskrit_input(self):
        """Test validation of valid Sanskrit input."""
        sanskrit_text = "योगः कर्मसु कौशलम्"
        is_valid, error, cleaned = self.validator.validate_input(sanskrit_text)
        assert is_valid
        assert error is None
        assert cleaned == sanskrit_text

    def test_sanskrit_detection_devanagari(self):
        """Test Sanskrit detection for Devanagari text."""
        sanskrit_text = "योगः कर्मसु कौशलम्"
        assert self.validator.contains_sanskrit(sanskrit_text)

    def test_sanskrit_detection_romanized(self):
        """Test Sanskrit detection for romanized text."""
        assert self.validator.contains_sanskrit("yoga karma")
        assert self.validator.contains_sanskrit("dharma moksha")

    def test_input_type_detection(self):
        """Test input type detection."""
        assert self.validator.get_input_type("योगः कर्मसु कौशलम्") == "sanskrit_verse"
        assert self.validator.get_input_type("What is yoga?") == "question"
        assert (
            self.validator.get_input_type("Random english text without sanskrit")
            == "general"
        )

    def test_text_cleaning(self):
        """Test text cleaning functionality."""
        dirty_text = "  योगः   कर्मसु  कौशलम्  "
        cleaned = self.validator.clean_text(dirty_text)
        assert cleaned == "योगः कर्मसु कौशलम्"

    def test_harmful_content_detection(self):
        """Test detection of potentially harmful content."""
        harmful_text = "<script>alert('test')</script>"
        is_valid, error, cleaned = self.validator.validate_input(harmful_text)
        assert not is_valid
        assert "Invalid input detected" in error


class TestOpenRouterClient:
    """Test OpenRouter API client."""

    def setup_method(self):
        """Set up test fixtures."""
        self.client = OpenRouterClient()

    @patch("api_client.config")
    def test_unconfigured_client(self, mock_config):
        """Test client behavior when not configured."""
        mock_config.is_configured.return_value = False

        success, response = self.client.send_message(
            [{"role": "user", "content": "test"}]
        )
        assert not success
        assert "API key not configured" in response

    @patch("api_client.requests.post")
    @patch("api_client.config")
    def test_successful_request(self, mock_config, mock_post):
        """Test successful API request."""
        # Mock configuration
        mock_config.is_configured.return_value = True
        mock_config.get_headers.return_value = {"Authorization": "Bearer test"}
        mock_config.api_url = "https://test.com"
        mock_config.model = "test-model"
        mock_config.temperature = 0.7
        mock_config.max_tokens = 1500

        # Mock successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "Test response"}}]
        }
        mock_post.return_value = mock_response

        # Create a new client instance to avoid configuration issues
        client = OpenRouterClient()
        client.config = mock_config

        success, response = client.send_message([{"role": "user", "content": "test"}])
        assert success
        assert response == "Test response"

    @patch("api_client.requests.post")
    @patch("api_client.config")
    def test_api_error_handling(self, mock_config, mock_post):
        """Test API error handling."""
        # Mock configuration
        mock_config.is_configured.return_value = True
        mock_config.get_headers.return_value = {"Authorization": "Bearer test"}
        mock_config.api_url = "https://test.com"
        mock_config.model = "test-model"
        mock_config.temperature = 0.7
        mock_config.max_tokens = 1500

        # Mock error response
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"
        mock_post.return_value = mock_response

        # Create a new client instance to avoid configuration issues
        client = OpenRouterClient()
        client.config = mock_config

        success, response = client.send_message([{"role": "user", "content": "test"}])
        assert not success
        assert "Invalid API key" in response


if __name__ == "__main__":
    # Run tests if script is executed directly
    pytest.main([__file__])
