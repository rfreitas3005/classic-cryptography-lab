"""Vigenère cipher implementation."""

from .base import BaseCipher


class VigenereCipher(BaseCipher):
    """Vigenère polyalphabetic substitution cipher."""

    def encrypt(self, text: str, key: str) -> str:
        """Encrypt using Vigenère cipher."""
        key = key.upper().replace(" ", "")
        if not key:
            raise ValueError("Key cannot be empty")

        text_clean = text.upper().replace(" ", "")
        result = ""
        key_index = 0

        for char in text_clean:
            if char.isalpha():
                key_char = key[key_index % len(key)]
                char_val = ord(char) - 65
                key_val = ord(key_char) - 65
                encrypted_val = (char_val + key_val) % 26
                result += chr(encrypted_val + 65)
                key_index += 1
            else:
                result += char

        return result

    def get_analysis(self, text: str, key: str) -> str:
        """Get step-by-step analysis of Vigenère encryption."""
        key = key.upper().replace(" ", "")
        if not key:
            raise ValueError("Key cannot be empty")

        text_clean = text.upper().replace(" ", "")
        result = ""
        analysis = "Step-by-Step Calculations:\n"
        analysis += "Text + Key = Sum mod 26 -> Ciphertext\n"
        analysis += "------------------------------------------\n"

        key_index = 0
        for char in text_clean:
            if char.isalpha():
                key_char = key[key_index % len(key)]
                char_val = ord(char) - 65
                key_val = ord(key_char) - 65
                sum_val = char_val + key_val
                encrypted_val = sum_val % 26
                encrypted_char = chr(encrypted_val + 65)

                result += encrypted_char
                analysis += (
                    f"{char}({char_val:02d}) + {key_char}({key_val:02d}) = "
                    f"{sum_val:02d} mod 26 -> {encrypted_val:02d} ({encrypted_char})\n"
                )
                key_index += 1

        analysis += f"\nFinal Result:\n> {result}"
        return analysis
