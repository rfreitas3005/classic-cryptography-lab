"""Monoalphabetic substitution cipher implementation."""

from .base import BaseCipher


class MonoalphabeticCipher(BaseCipher):
    """Monoalphabetic substitution cipher."""

    def encrypt(self, text: str, key: str) -> str:
        """Encrypt using monoalphabetic substitution."""
        key = key.upper().replace(" ", "")
        text = text.upper().replace(" ", "")

        if len(key) != 26 or not key.isalpha():
            raise ValueError("Key must contain exactly 26 letters")

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        translation_table = str.maketrans(alphabet, key)
        return text.translate(translation_table)

    def get_analysis(self, text: str, key: str) -> str:
        """Get step-by-step analysis of monoalphabetic encryption."""
        key = key.upper().replace(" ", "")
        text = text.upper().replace(" ", "")

        if len(key) != 26 or not key.isalpha():
            raise ValueError("Key must contain exactly 26 letters")

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        analysis = "Alphabet Mapping:\n"
        analysis += "------------------------\n"
        analysis += "Original: " + " ".join(list(alphabet)) + "\n"
        analysis += "Key:      " + " ".join(list(key)) + "\n\n"

        translation_table = str.maketrans(alphabet, key)
        result = text.translate(translation_table)

        analysis += f"Final Result:\n> {result}"
        return analysis
