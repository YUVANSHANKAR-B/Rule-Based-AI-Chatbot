@echo off
cd /d "%~dp0"
set PYTHON_EXE="%~dp0.venv\Scripts\python.exe"
if exist %PYTHON_EXE% (
    %PYTHON_EXE% rule_based_chatbot.py
) else (
    echo Virtual environment Python not found.
    echo Run "python -m venv .venv" and install dependencies first.
)
