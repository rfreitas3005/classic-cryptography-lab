@echo off
REM Build Lab Cripto Executable with PyInstaller

setlocal enabledelayedexpansion

echo Building Lab Cripto executable...
py -m PyInstaller lab_cripto_new.spec

if errorlevel 1 (
    echo.
    echo Error: Build failed
    echo Make sure PyInstaller is installed: py -m pip install pyinstaller
    pause
    exit /b 1
)

echo.
echo Build complete! Executable is in the 'dist' folder.
pause

