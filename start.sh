#!/bin/bash

# Quick Start Script for Company Research Assistant
# This script helps you get started quickly

echo "=================================="
echo "Company Research Assistant Setup"
echo "=================================="
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found!"
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✅ Created .env file"
    echo ""
    echo "📝 Please edit .env and add your GEMINI_API_KEY"
    echo "   Get your key from: https://makersuite.google.com/app/apikey"
    echo ""
    read -p "Press Enter after you've added your API key..."
fi

# Check if API key is set
if grep -q "your_gemini_api_key_here" .env || grep -q "^GEMINI_API_KEY=$" .env; then
    echo "⚠️  GEMINI_API_KEY not set in .env file!"
    echo "📝 Please edit .env and add your actual API key"
    echo "   Get your key from: https://makersuite.google.com/app/apikey"
    echo ""
    exit 1
fi

echo "✅ .env file configured"
echo ""

# Check if dependencies are installed
echo "Checking Python dependencies..."
if python3 -c "import streamlit" 2>/dev/null; then
    echo "✅ Dependencies already installed"
else
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

echo ""
echo "=================================="
echo "🚀 Starting Company Research Assistant"
echo "=================================="
echo ""
echo "The app will open in your browser at http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run Streamlit
streamlit run main.py
