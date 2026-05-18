"""Example usage of Lab Cripto ciphers as standalone modules."""

from src.ciphers import (
    CaesarCipher,
    MonoalphabeticCipher,
    PlayfairCipher,
    VigenereCipher,
    VernamCipher,
    TranspositionCipher,
)


def main():
    """Demonstrate cipher usage."""

    # Example 1: Caesar Cipher
    print("=" * 60)
    print("CAESAR CIPHER")
    print("=" * 60)
    caesar = CaesarCipher()
    message = "HELLO WORLD"
    key = "3"
    print(caesar.get_analysis(message, key))

    # Example 2: Vigenère Cipher
    print("\n" + "=" * 60)
    print("VIGENERE CIPHER")
    print("=" * 60)
    vigenere = VigenereCipher()
    message = "HELLO WORLD"
    key = "UTAD"
    print(vigenere.get_analysis(message, key))

    # Example 3: Playfair Cipher
    print("\n" + "=" * 60)
    print("PLAYFAIR CIPHER")
    print("=" * 60)
    playfair = PlayfairCipher()
    message = "HELLO WORLD"
    key = "KEYWORD"
    print(playfair.get_analysis(message, key))

    # Example 4: Monoalphabetic Cipher
    print("\n" + "=" * 60)
    print("MONOALPHABETIC CIPHER")
    print("=" * 60)
    mono = MonoalphabeticCipher()
    message = "HELLO WORLD"
    key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"  # Reversed alphabet
    print(mono.get_analysis(message, key))

    # Example 5: Vernam Cipher
    print("\n" + "=" * 60)
    print("VERNAM CIPHER (OTP)")
    print("=" * 60)
    vernam = VernamCipher()
    message = "HELLO"
    key = "WORLD"  # Must be same length
    print(vernam.get_analysis(message, key))

    # Example 6: Transposition Cipher
    print("\n" + "=" * 60)
    print("COLUMNAR TRANSPOSITION CIPHER")
    print("=" * 60)
    transposition = TranspositionCipher()
    message = "HELLO WORLD"
    key = "ZEBRAS"
    print(transposition.get_analysis(message, key))


if __name__ == "__main__":
    main()
