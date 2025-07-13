#!/bin/bash

# Quick launch script for your Student Performance Predictor
echo "🚀 Launching Student Performance Predictor Web App"
echo "📊 Your Exceptional ML Model (R² = 0.9250)"
echo "="*50

cd /Users/drahmetacik/Projects/ml_practice_project

# Set environment variable to skip email prompt
export STREAMLIT_SERVER_HEADLESS=true

# Activate virtual environment and run
source .venv/bin/activate
.venv/bin/streamlit run app/student_predictor_app.py --server.headless true

echo "🎯 Web app should open at: http://localhost:8501"
