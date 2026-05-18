"""Vernam (One-Time Pad) cipher implementation."""

from .base import BaseCipher


class VernamCipher(BaseCipher):
    """Vernam cipher - One-Time Pad encryption."""

    def encrypt(self, text: str, key: str) -> str:
        """Encrypt using Vernam cipher."""
        text = text.upper().replace(" ", "")
        key = key.upper().replace(" ", "")

        if len(key) < len(text):
            raise ValueError("Key must be at least as long as the message")

        result = ""
        for i in range(len(text)):
            if text[i].isalpha():
                text_val = ord(text[i]) - 65
                key_val = ord(key[i]) - 65
                encrypted_val = (text_val + key_val) % 26
                result += chr(encrypted_val + 65)

        return result

    def get_analysis(self, text: str, key: str) -> str:
        """Get step-by-step analysis of Vernam encryption."""
        text = text.upper().replace(" ", "")
        key = key.upper().replace(" ", "")

        if len(key) < len(text):
            raise ValueError("Key must be at least as long as the message")

        result = ""
        analysis = "Step-by-Step Calculations (Letter + Letter):\n"
        analysis += "---------------------------------------\n"

        for i in range(len(text)):
            if text[i].isalpha():
                text_val = ord(text[i]) - 65
                key_val = ord(key[i]) - 65
                sum_val = text_val + key_val
                encrypted_val = sum_val % 26
                encrypted_char = chr(encrypted_val + 65)

                result += encrypted_char
                analysis += (
                    f"{text[i]}({text_val:02d}) + {key[i]}({key_val:02d}) = "
                    f"{sum_val:02d} mod 26 -> {encrypted_val:02d} ({encrypted_char})\n"
                )

        analysis += f"\nFinal Result:\n> {result}"
        return analysis
