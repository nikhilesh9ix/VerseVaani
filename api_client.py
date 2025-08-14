"""API client for OpenRouter integration."""

import json
import logging

import requests

from config import config

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OpenRouterClient:
    """Client for interacting with OpenRouter API."""

    def __init__(self):
        self.config = config

    def _validate_config(self) -> bool:
        """Validate that the configuration is proper."""
        if not self.config.is_configured():
            logger.error("OpenRouter API key not configured")
            return False
        return True

    def _create_payload(self, messages: list[dict[str, str]]) -> dict:
        """Create payload for API request."""
        return {
            "model": self.config.model,
            "messages": messages,
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
            "stream": False,
        }

    def send_message(self, messages: list[dict[str, str]]) -> tuple[bool, str]:
        """Send messages to OpenRouter API.

        Args:
            messages: List of message dictionaries with 'role' and 'content'

        Returns:
            Tuple of (success: bool, response: str)
        """
        if not self._validate_config():
            return (
                False,
                "⚠️ API key not configured. Please set OPENROUTER_API_KEY in your environment variables or Streamlit secrets.",
            )

        try:
            payload = self._create_payload(messages)
            headers = self.config.get_headers()

            logger.info(f"Sending request to OpenRouter with {len(messages)} messages")

            response = requests.post(
                self.config.api_url,
                headers=headers,
                data=json.dumps(payload),
                timeout=30,
            )

            if response.status_code == 200:
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0:
                    reply = result["choices"][0]["message"]["content"]
                    logger.info("Successfully received response from OpenRouter")
                    return True, reply
                logger.error("Invalid response format from OpenRouter")
                return False, "❌ Received invalid response from the AI service."

            if response.status_code == 401:
                logger.error("Invalid API key")
                return (
                    False,
                    "❌ Invalid API key. Please check your OpenRouter API key.",
                )

            if response.status_code == 429:
                logger.error("Rate limit exceeded")
                return (
                    False,
                    "⏳ Rate limit exceeded. Please wait a moment before trying again.",
                )

            if response.status_code == 500:
                logger.error("Server error")
                return (
                    False,
                    "🔧 The AI service is temporarily unavailable. Please try again later.",
                )

            logger.error(f"HTTP {response.status_code}: {response.text}")
            return (
                False,
                f"❌ Error {response.status_code}: Unable to get response from AI service.",
            )

        except requests.exceptions.Timeout:
            logger.error("Request timeout")
            return False, "⏱️ Request timed out. Please try again."

        except requests.exceptions.ConnectionError:
            logger.error("Connection error")
            return (
                False,
                "🌐 Unable to connect to the AI service. Please check your internet connection.",
            )

        except requests.exceptions.RequestException as e:
            logger.error(f"Request exception: {e}")
            return False, f"❌ Network error: {e!s}"

        except json.JSONDecodeError:
            logger.error("JSON decode error")
            return False, "❌ Received invalid response format from the AI service."

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return False, f"❌ An unexpected error occurred: {e!s}"


# Global client instance
openrouter_client = OpenRouterClient()
