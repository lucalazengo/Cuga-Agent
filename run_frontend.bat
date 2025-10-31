@echo off
echo ========================================
echo Starting Cuga Agent Frontend
echo ========================================
cd src\frontend
echo Creating virtual environment...
python -m venv venv
echo Activating virtual environment...
call venv\Scripts\activate
echo Installing dependencies...
pip install -r requirements.txt
echo Starting Streamlit app...
streamlit run app.py
pause

