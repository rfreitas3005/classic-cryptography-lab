"""Playfair cipher implementation."""

from .base import BaseCipher


class PlayfairCipher(BaseCipher):
    """Playfair cipher using 5x5 matrix."""

    def _build_matrix(self, key: str) -> list:
        """Build the 5x5 Playfair matrix."""
        key = "".join(dict.fromkeys(key.upper().replace("J", "I").replace(" ", "")))
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix_str = key + "".join([c for c in alphabet if c not in key])
        return [matrix_str[i : i + 5] for i in range(0, 25, 5)]

    def _find_position(self, char: str, matrix: list) -> tuple:
        """Find position of character in matrix."""
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == char:
                    return row, col
        return 0, 0

    def encrypt(self, text: str, key: str) -> str:
        """Encrypt using Playfair cipher."""
        matrix = self._build_matrix(key)
        text = text.upper().replace("J", "I").replace(" ", "")

        # Create digraphs
        digraphs = []
        i = 0
        while i < len(text):
            c1 = text[i]
            if i + 1 < len(text):
                c2 = text[i + 1]
                if c1 == c2:
                    digraphs.append(c1 + "X")
                    i += 1
                else:
                    digraphs.append(c1 + c2)
                    i += 2
            else:
                digraphs.append(c1 + "X")
                i += 1

        # Encrypt digraphs
        result = ""
        for digraph in digraphs:
            r1, c1 = self._find_position(digraph[0], matrix)
            r2, c2 = self._find_position(digraph[1], matrix)

            if r1 == r2:  # Same row
                result += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
            elif c1 == c2:  # Same column
                result += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
            else:  # Rectangle
                result += matrix[r1][c2] + matrix[r2][c1]

        return result

    def get_analysis(self, text: str, key: str) -> str:
        """Get step-by-step analysis of Playfair encryption."""
        matrix = self._build_matrix(key)
        text = text.upper().replace("J", "I").replace(" ", "")

        analysis = "5x5 Matrix:\n"
        analysis += "-----------\n"
        for row in matrix:
            analysis += "  " + "   ".join(row) + "\n"

        # Create digraphs
        digraphs = []
        i = 0
        while i < len(text):
            c1 = text[i]
            if i + 1 < len(text):
                c2 = text[i + 1]
                if c1 == c2:
                    digraphs.append(c1 + "X")
                    i += 1
                else:
                    digraphs.append(c1 + c2)
                    i += 2
            else:
                digraphs.append(c1 + "X")
                i += 1

        # Encrypt and show process
        result = ""
        for digraph in digraphs:
            r1, c1 = self._find_position(digraph[0], matrix)
            r2, c2 = self._find_position(digraph[1], matrix)

            if r1 == r2:
                result += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
            elif c1 == c2:
                result += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
            else:
                result += matrix[r1][c2] + matrix[r2][c1]

        analysis += f"\nOriginal Pairs: {' '.join(digraphs)}\n"
        analysis += f"Final Result  : > {result}"
        return analysis
