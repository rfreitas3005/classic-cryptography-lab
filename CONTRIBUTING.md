# Contributing to Lab Cripto

Thank you for your interest in contributing to Lab Cripto! Here's how you can help.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature: `git checkout -b feature/amazing-feature`
4. Make your changes
5. Test your changes: `py main.py` or `run.bat`
6. Commit: `git commit -m 'Add amazing feature'`
7. Push to your branch: `git push origin feature/amazing-feature`
8. Create a Pull Request

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to all functions and classes
- Include type hints where applicable

## Adding New Ciphers

1. Create a new file in `src/ciphers/` named `your_cipher.py`
2. Implement your cipher by extending `BaseCipher`
3. Implement both `encrypt()` and `get_analysis()` methods
4. Add tests if possible
5. Update `src/ciphers/__init__.py` to export your cipher
6. Update the UI in `src/ui/main_window.py` to add your cipher to the list

## Reporting Issues

- Use clear, descriptive titles
- Describe the expected behavior
- Describe the actual behavior
- Include steps to reproduce

## Questions?

Feel free to open an issue for any questions.

Thank you for contributing!
