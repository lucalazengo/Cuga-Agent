#!/bin/bash

echo "========================================"
echo "Starting Cuga Agent Backend"
echo "========================================"

cd src/backend

echo "Creating virtual environment..."
python -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting FastAPI server..."
python main.py

