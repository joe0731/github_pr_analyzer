#!/bin/bash
# Quick start script for GitHub PR Analyzer

set -e

echo "=========================================="
echo "GitHub PR Analyzer - Quick Start"
echo "=========================================="
echo ""

# check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "✓ Python found: $(python3 --version)"

# check if Git is installed
if ! command -v git &> /dev/null; then
    echo "Error: Git is not installed"
    echo "Please install Git"
    exit 1
fi

echo "✓ Git found: $(git --version)"

# check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "Error: GitHub CLI (gh) is not installed"
    echo "Please install gh CLI:"
    echo "  Ubuntu/Debian: sudo apt install gh"
    echo "  macOS: brew install gh"
    echo "  Windows: choco install gh"
    exit 1
fi

echo "✓ GitHub CLI found: $(gh --version | head -n 1)"

# check gh authentication
if ! gh auth status &> /dev/null; then
    echo ""
    echo "GitHub CLI is not authenticated."
    echo "Please run: gh auth login"
    echo ""
    read -p "Do you want to authenticate now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        gh auth login
    else
        echo "Please authenticate before using the tool."
        exit 1
    fi
fi

echo "✓ GitHub CLI is authenticated"
echo ""

# create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet

# install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt --quiet

echo "✓ Dependencies installed"
echo ""

# create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✓ .env file created"
    echo "  You can edit .env to customize settings"
fi

echo ""
echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo ""
echo "Run installation test:"
echo "  python test_installation.py"
echo ""
echo "Get help:"
echo "  python main.py --help"
echo ""
echo "Try the interactive mode:"
echo "  python main.py interactive"
echo ""
echo "Search for PRs and commits:"
echo "  python main.py search \"your query\""
echo ""
echo "For more information, see:"
echo "  - README.md: Overview and features"
echo "  - USAGE.md: Detailed usage guide"
echo "  - INSTALL.md: Installation troubleshooting"
echo ""
