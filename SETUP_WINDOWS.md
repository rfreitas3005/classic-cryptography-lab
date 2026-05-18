# Lab Cripto - Windows Setup Guide 🪟

If you're having issues running Lab Cripto on Windows, follow this guide.

## Problem: "Python was not found"

This usually means Python is not added to your Windows PATH. Here are the solutions:

### Option 1: Use the Provided Batch File (Easiest) ✅

Simply double-click or run:
```cmd
run.bat
```

### Option 2: Command Line

Open Command Prompt and run:
```cmd
py main.py
```

### Option 3: Manual Method (if needed)

1. Open Command Prompt
2. Navigate to the project folder
3. Run:
   ```cmd
   py main.py
   ```

## Running Examples

### Test the ciphers:
```cmd
py example_usage.py
```

## Building Executable

### Easy way (Recommended):
```cmd
build.bat
```

### Manual way:
```cmd
py -m PyInstaller lab_cripto_new.spec
```

Then your executable will be in `dist/lab_cripto.exe`

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `python: The term 'python' is not recognized` | Use `run.bat` instead or add Python to PATH |
| `pyinstaller: The term 'pyinstaller' is not recognized` | Use `build.bat` or run `python -m PyInstaller` |
| `ModuleNotFoundError: No module named 'tkinter'` | Tkinter is included with Python - reinstall if missing |
| Build takes very long | This is normal - PyInstaller packages everything. Can take 2-5 minutes |

## Quick Reference
Try `py main.py` or use `run.bat` |
| `py: The term 'py' is no
|------|-----------------|
| Run app | `run.bat` or `py main.py` |
| Build exe | `build.bat` |
| Test ciphers | `py example_usage.py` |

## Still Having Issues?

1. Check if Python is installed: Open Command Prompt and type `py --version`
2. If not found, download from https://www.python.org/downloads/
3. During installation, **CHECK** the box "Add Python to PATH"
4. Restart Command Prompt and try again

---

For more help, check the main [README.md](README.md)
