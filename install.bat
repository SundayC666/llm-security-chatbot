@echo off
REM Security Chatbot - One-Click Installation Script for Windows
REM This script automates the installation process

echo ===============================================================
echo   Security Chatbot - Automated Installation
echo ===============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.11 or higher from https://www.python.org/
    pause
    exit /b 1
)

echo [1/6] Python found:
python --version
echo.

REM Check if virtual environment exists
if exist venv (
    echo [2/6] Virtual environment already exists. Skipping creation.
) else (
    echo [2/6] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully.
)
echo.

REM Activate virtual environment
echo [3/6] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)
echo.

REM Upgrade pip
echo [4/6] Upgrading pip...
python -m pip install --upgrade pip --quiet
echo pip upgraded.
echo.

REM Install packages
echo [5/6] Installing required packages...
echo This may take 5-10 minutes. Please be patient...
echo.

pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo [WARNING] Some packages may have failed to install.
    echo Trying individual installation...
    echo.
    
    pip install faiss-cpu
    pip install streamlit
    pip install langchain langchain-community langchain-openai
    pip install langchain-text-splitters langchain-core
    pip install sentence-transformers
    pip install openai
    pip install requests python-dotenv pandas numpy tiktoken
)
echo.

REM Verify installation
echo [6/6] Verifying installation...
python test_imports.py

if errorlevel 1 (
    echo.
    echo [WARNING] Some packages may not be installed correctly.
    echo Please check the output above and refer to INSTALLATION_FIX.md
) else (
    echo.
    echo ===============================================================
    echo   Installation Complete!
    echo ===============================================================
    echo.
    echo Next steps:
    echo   1. Configure .env file (copy from .env.example)
    echo   2. Run: streamlit run app.py
    echo.
)

pause
