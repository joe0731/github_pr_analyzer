#!/bin/bash
# Quick start script for GitHub PR Analyzer

set -e

echo "=========================================="
echo "GitHub PR Analyzer - Quick Start"
echo "=========================================="
echo ""

# 1. Check Prerequisites
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

if ! command -v git &> /dev/null; then
    echo "Error: Git is not installed"
    exit 1
fi

if ! command -v gh &> /dev/null; then
    echo "Error: GitHub CLI (gh) is not installed"
    exit 1
fi

# 2. Check gh auth (CRITICAL STEP)
echo "Checking GitHub authentication..."
if ! gh auth status &> /dev/null; then
    echo ""
    echo "⚠️  GitHub CLI is not authenticated."
    echo "Please run: gh auth login"
    exit 1
fi

# 3. Install
echo "Installing github-pr-analyzer..."
pip install github-pr-analyzer --upgrade

echo ""
echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo ""
echo "⚠️  Note: If you want to use AI features, set CURSOR_AGENT_PATH:"
echo "   export CURSOR_AGENT_PATH=/path/to/cursor-agent"
echo ""
echo "Try running:"
echo "  ghpa interactive"
echo ""
echo "Legacy command (still supported):"
echo "  gh-pr-analyzer interactive"
echo ""
