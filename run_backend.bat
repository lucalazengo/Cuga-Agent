@echo off
echo ========================================
echo Starting Cuga Agent Backend
echo ========================================
cd src\backend
echo Creating virtual environment...
python -m venv venv
echo Activating virtual environment...
call venv\Scripts\activate
echo Installing dependencies...
pip install -r requirements.txt
echo Starting FastAPI server...
python main.py
pause

