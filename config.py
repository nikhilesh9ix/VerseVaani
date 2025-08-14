"""Configuration management for VerseVaani application."""

import os
from typing import Optional

import streamlit as st


class Config:
    """Configuration class for VerseVaani application."""

    def __init__(self):
        self.api_key = self._get_api_key()
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "mistralai/mistral-7b-instruct-v0.3"
        self.temperature = 0.7
        self.max_tokens = 1500

    def _get_api_key(self) -> Optional[str]:
        """Get API key from environment variables or Streamlit secrets."""
        # Try environment variable first
        api_key = os.getenv("OPENROUTER_API_KEY")

        # If not found, try Streamlit secrets
        if not api_key:
            try:
                api_key = st.secrets.get("OPENROUTER_API_KEY")
            except Exception:
                pass

        return api_key

    def is_configured(self) -> bool:
        """Check if the application is properly configured."""
        return self.api_key is not None and self.api_key.strip() != ""

    def get_headers(self) -> dict:
        """Get headers for API requests."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://versevaani.streamlit.app",
            "X-Title": "VerseVaani - Sanskrit Shloka Explainer",
        }


# Global configuration instance
config = Config()
