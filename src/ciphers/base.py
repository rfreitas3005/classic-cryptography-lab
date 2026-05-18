"""Base cipher class."""


class BaseCipher:
    """Base class for all cipher implementations."""

    def encrypt(self, text: str, key: str) -> str:
        """
        Encrypt the text using the given key.
        
        Args:
            text: The plaintext to encrypt
            key: The encryption key
            
        Returns:
            The encrypted text
            
        Raises:
            NotImplementedError: Must be implemented by subclasses
        """
        raise NotImplementedError("Subclasses must implement encrypt()")

    def get_analysis(self, text: str, key: str) -> str:
        """
        Get detailed step-by-step analysis of the encryption process.
        
        Args:
            text: The plaintext to encrypt
            key: The encryption key
            
        Returns:
            A formatted string with detailed calculations
            
        Raises:
            NotImplementedError: Must be implemented by subclasses
        """
        raise NotImplementedError("Subclasses must implement get_analysis()")
