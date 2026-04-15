@echo off
echo ======================================
echo Walmart ESG Dashboard - Quick Start
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo X Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo [OK] Python detected
python --version
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo [OK] Virtual environment created
) else (
    echo [OK] Virtual environment already exists
)

echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt --quiet
echo [OK] Dependencies installed

echo.

REM Run test script
echo Running installation tests...
python test_installation.py

if %errorlevel% equ 0 (
    echo.
    echo ======================================
    echo Starting Walmart ESG Dashboard...
    echo ======================================
    echo.
    echo Dashboard will open in your browser at:
    echo http://localhost:8501
    echo.
    echo Press Ctrl+C to stop the server
    echo.
    
    streamlit run app.py
) else (
    echo.
    echo X Installation tests failed. Please fix errors above.
    pause
    exit /b 1
)
