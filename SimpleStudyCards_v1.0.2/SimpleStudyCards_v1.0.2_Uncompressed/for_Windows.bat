@echo off
cd /d "%~dp0"

py --version >nul 2>&1
if %errorlevel% equ 0 (
    py pythonscript/SimpleStudyCards_app.py
) else (
    python pythonscript/SimpleStudyCards_app.py
)

pause