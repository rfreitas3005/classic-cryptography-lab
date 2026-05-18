"""Columnar transposition cipher implementation."""

import math
from .base import BaseCipher


class TranspositionCipher(BaseCipher):
    """Columnar transposition cipher."""

    def encrypt(self, text: str, key: str) -> str:
        """Encrypt using columnar transposition."""
        text = text.upper().replace(" ", "")
        key = key.upper().replace(" ", "")

        if not key:
            raise ValueError("Key cannot be empty")

        num_cols = len(key)
        num_rows = math.ceil(len(text) / num_cols)
        text += "X" * (num_rows * num_cols - len(text))

        # Create grid
        grid = [text[i : i + num_cols] for i in range(0, len(text), num_cols)]

        # Sort columns by key
        sorted_indices = sorted(
            list(enumerate(key)), key=lambda x: x[1]
        )

        result = ""
        for original_index, _ in sorted_indices:
            for row in range(num_rows):
                result += grid[row][original_index]

        return result

    def get_analysis(self, text: str, key: str) -> str:
        """Get step-by-step analysis of transposition encryption."""
        text = text.upper().replace(" ", "")
        key = key.upper().replace(" ", "")

        if not key:
            raise ValueError("Key cannot be empty")

        num_cols = len(key)
        num_rows = math.ceil(len(text) / num_cols)
        text += "X" * (num_rows * num_cols - len(text))

        # Create grid
        grid = [text[i : i + num_cols] for i in range(0, len(text), num_cols)]

        # Sort columns by key
        sorted_indices = sorted(
            list(enumerate(key)), key=lambda x: x[1]
        )

        # Create order mapping
        order = [0] * num_cols
        for i, (original_idx, _) in enumerate(sorted_indices):
            order[original_idx] = i + 1

        analysis = "Transposition Grid:\n\n"
        analysis += "Key   : " + "  ".join(list(key)) + "\n"
        analysis += "Order : " + "  ".join(map(str, order)) + "\n"
        analysis += "        " + "-" * (num_cols * 3) + "\n"
        for row in range(num_rows):
            analysis += "        " + "  ".join(list(grid[row])) + "\n"

        result = ""
        for original_index, _ in sorted_indices:
            for row in range(num_rows):
                result += grid[row][original_index]

        analysis += f"\nFinal Result:\n> {result}"
        return analysis
