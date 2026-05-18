@echo off
REM Run Lab Cripto Application

setlocal enabledelayedexpansion

echo Launching Lab Cripto...
py main.py

if errorlevel 1 (
    echo.
    echo Error: Could not run application
    echo Make sure Python is installed and 'py' command is available
    pause
)

