"""Input validation and Sanskrit text processing utilities."""

import re
from typing import Optional


class InputValidator:
    """Validates and processes user input for Sanskrit shlokas."""

    # Common Sanskrit characters and patterns
    DEVANAGARI_RANGE = r"[\u0900-\u097F]"
    IAST_PATTERN = r"[aāiīuūeēoōṛṝṃḥkgcjṭḍtdnpbyrlvśṣshm]"

    def __init__(self):
        # Common Sanskrit punctuation and symbols
        self.sanskrit_punctuation = ["।", "॥", "ॐ", "्"]

    def contains_sanskrit(self, text: str) -> bool:
        """Check if text contains Sanskrit characters (Devanagari or IAST)."""
        # Check for Devanagari script
        if re.search(self.DEVANAGARI_RANGE, text):
            return True

        # Check for IAST transliteration (more specific patterns)
        # Look for Sanskrit-specific diacritical marks
        iast_specific = r"[āīūēōṛṝṃḥṇṭḍśṣ]"
        if re.search(iast_specific, text, re.IGNORECASE):
            return True

        # Check for common Sanskrit words in romanized form
        sanskrit_words = [
            "yoga",
            "dharma",
            "karma",
            "moksha",
            "atman",
            "brahman",
            "samsara",
            "nirvana",
            "guru",
            "mantra",
            "yantra",
            "tantra",
            "vedas",
            "upanishads",
            "gita",
            "ramayana",
            "mahabharata",
        ]

        text_lower = text.lower()
        # Use word boundaries to avoid false positives
        return any(
            re.search(r"\b" + word + r"\b", text_lower) for word in sanskrit_words
        )

    def clean_text(self, text: str) -> str:
        """Clean and normalize input text."""
        # Remove excessive whitespace
        text = re.sub(r"\s+", " ", text.strip())

        # Remove common markdown or formatting artifacts
        text = re.sub(r"[*_`#]", "", text)

        return text

    def validate_input(self, text: str) -> tuple[bool, Optional[str], str]:
        """Validate user input for Sanskrit shloka processing.

        Args:
            text: User input text

        Returns:
            Tuple of (is_valid: bool, error_message: Optional[str], cleaned_text: str)
        """
        if not text or not text.strip():
            return False, "Please enter some text to analyze.", ""

        cleaned_text = self.clean_text(text)

        if len(cleaned_text) < 3:
            return (
                False,
                "Please enter a longer text for meaningful analysis.",
                cleaned_text,
            )

        if len(cleaned_text) > 1000:
            return (
                False,
                "Text is too long. Please enter a shorter shloka or verse (max 1000 characters).",
                cleaned_text,
            )

        # Check for potentially harmful content (very basic check)
        harmful_patterns = ["<script", "javascript:", "data:", "vbscript:"]
        text_lower = cleaned_text.lower()
        if any(pattern in text_lower for pattern in harmful_patterns):
            return (
                False,
                "Invalid input detected. Please enter clean Sanskrit text.",
                cleaned_text,
            )

        return True, None, cleaned_text

    def get_input_type(self, text: str) -> str:
        """Determine the type of input (Sanskrit verse, question, etc.)."""
        text_lower = text.lower().strip()

        # Check if it's a question
        question_indicators = [
            "what",
            "how",
            "why",
            "when",
            "where",
            "explain",
            "meaning",
            "?",
        ]
        if any(indicator in text_lower for indicator in question_indicators):
            return "question"

        # Check if it contains Sanskrit
        if self.contains_sanskrit(text):
            return "sanskrit_verse"

        # Default to general input
        return "general"

    def suggest_improvements(self, text: str) -> list[str]:
        """Suggest improvements for better processing."""
        suggestions = []

        if not self.contains_sanskrit(text):
            suggestions.append(
                "💡 For best results, try entering text in Devanagari script or include Sanskrit words."
            )

        if len(text.split()) < 4:
            suggestions.append(
                "💡 Consider entering a complete shloka or verse for more detailed analysis."
            )

        if "।" not in text and "॥" not in text and self.contains_sanskrit(text):
            suggestions.append(
                "💡 Sanskrit verses often end with '।' or '॥' - these help identify verse boundaries."
            )

        return suggestions


# Global validator instance
input_validator = InputValidator()
