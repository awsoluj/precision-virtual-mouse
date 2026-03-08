@echo off
title Precision Virtual Mouse
echo Checking system requirements...

:: Check if 'venv' exists
if not exist "venv" (
    echo ---------------------------------------------------
    echo First time setup detected!
    echo Creating virtual environment...
    echo ---------------------------------------------------
    python -m venv venv
    
    echo Activating virtual environment...
    call venv\Scripts\activate
    
    echo Installing dependencies...
    pip install -r requirements.txt
    
    echo ---------------------------------------------------
    echo Setup Complete!
    echo ---------------------------------------------------
) else (
    echo Virtual environment found. Activating...
    call venv\Scripts\activate
)

echo.
echo Launching Space Defense Game...
echo Press 'q' in the game window to quit.
echo.

python main.py

echo.
echo Game closed. 
pause