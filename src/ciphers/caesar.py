"""Caesar cipher implementation."""

from .base import BaseCipher


class CaesarCipher(BaseCipher):
    """Caesar cipher with customizable displacement."""

    def encrypt(self, text: str, key: str) -> str:
        """Encrypt using Caesar cipher."""
        try:
            displacement = int(key)
        except ValueError:
            raise ValueError("Caesar cipher key must be a number")

        text = text.upper().replace(" ", "")
        result = ""

        for char in text:
            if char.isalpha():
                val = ord(char) - 65
                encrypted_val = (val + displacement) % 26
                result += chr(encrypted_val + 65)
            else:
                result += char

        return result

    def get_analysis(self, text: str, key: str) -> str:
        """Get step-by-step analysis of Caesar encryption."""
        try:
            displacement = int(key)
        except ValueError:
            raise ValueError("Caesar cipher key must be a number")

        text = text.upper().replace(" ", "")
        result = ""
        analysis = "Step-by-Step Calculations:\n"
        analysis += "------------------------\n"

        for char in text:
            if char.isalpha():
                val = ord(char) - 65
                sum_val = val + displacement
                encrypted_val = sum_val % 26
                encrypted_char = chr(encrypted_val + 65)
                result += encrypted_char
                analysis += (
                    f"{char} ({val:02d}) + k({displacement}) = {sum_val:02d} "
                    f"mod 26 -> {encrypted_val:02d} ({encrypted_char})\n"
                )

        analysis += f"\nFinal Result:\n> {result}"
        return analysis
