# Lab Cripto

A comprehensive cryptography laboratory application built with Python and Tkinter. Learn and visualize classic cipher algorithms with step-by-step calculations.

## Features

- **Caesar Cipher**: Basic substitution cipher with customizable displacement
- **Monoalphabetic Substitution**: Full alphabet replacement cipher
- **Playfair Cipher**: Digraphic substitution cipher with 5x5 matrix
- **Vigenère Cipher**: Polyalphabetic substitution using keyword
- **Vernam Cipher (OTP)**: One-Time Pad encryption
- **Columnar Transposition**: Transposition cipher using keyword ordering

## Screenshots

All ciphers include:
- Real-time step-by-step calculation visualization
- Educational format showing intermediate values
- Clean and intuitive dark-themed UI
- Input validation and error handling

## Installation 

### Requirements
- Python 3.9+
- tkinter (usually bundled with Python)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/lab_cripto.git
cd lab_cripto
```

2. Install dependencies (if needed):
```bash
pip install -r requirements.txt
```

### Running the Application

#### Option 1: Double-click (Windows)
- Simply double-click `run.bat` to launch the application

#### Option 2: Command Line (Windows)
```cmd
py main.py
```

Or use the provided script:
```cmd
run.bat
```

#### Option 3: PowerShell
```powershell
py main.py
```

## Usage 

1. **Select a cipher** from the dropdown menu
2. **Enter your message** to encrypt
3. **Provide a key** (format depends on chosen cipher):
   - Caesar: numeric displacement (e.g., 3)
   - Monoalphabetic: 26-character shuffled alphabet
   - Playfair/Vigenère/Transposition: keyword
   - Vernam: same length as message
4. **Click "Encrypt Message"** to process
5. **View step-by-step calculations** in the results panel

## Project Structure 

```
lab_cripto/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .gitignore             # Git ignore rules
└── src/
    ├── ciphers/           # Cipher implementations
    │   ├── __init__.py
    │   ├── base.py       # Base cipher class
    │   ├── caesar.py     # Caesar cipher
    │   ├── monoalphabetic.py
    │   ├── playfair.py
    │   ├── vigenere.py
    │   ├── vernam.py
    │   └── transposition.py
    └── ui/                # User interface
        ├── __init__.py
        ├── main_window.py # Main UI window
        └── styles.py      # Theme and styles
```

## Technical Details 

### Architecture

The application follows a modular design:
- **Ciphers Module**: Independent cipher implementations with consistent interface
- **UI Module**: Tkinter-based interface with custom theming
- **Main Entry Point**: Simple launcher that initializes the GUI

### Color Scheme (Catppuccin Mocha)

- Background: `#1E1E2E`
- Foreground: `#CDD6F4`
- Accent: `#89B4FA`
- Terminal: `#11111B`
- Success: `#A6E3A1`

## Building Executable 

To create a standalone executable using PyInstaller:

### Windows (Easiest)
Simply double-click `build.bat` or run:
```cmd
build.bat
```

### Command Line
```bash
# Option 1 (if py command is available)
py -m PyInstaller lab_cripto_new.spec

# Option 2 (manual)
build.bat
```

The executable will be created in the `dist/` folder as `lab_cripto.exe`.

## Educational Purpose 

This project is designed for learning cryptography concepts. Classic ciphers have known vulnerabilities and should **NOT** be used for actual data protection.

## License 

MIT License - See LICENSE file for details

## Author 

Developed by Ricardo Freitas

## Contributing 

Contributions are welcome! Feel free to submit issues or pull requests.

---

**Disclaimer**: These cipher implementations are for educational purposes only. Do not use them for securing sensitive data.
