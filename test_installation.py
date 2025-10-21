#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Installation test script for GitHub PR Analyzer.

MIT License

Copyright (c) 2025 GitHub PR Analyzer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
from pathlib import Path


def test_python_version():
    """test if Python version is compatible."""
    print("Checking Python version...")
    version = sys.version_info
    if version >= (3, 8):
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(
            f"✗ Python {version.major}.{version.minor}.{version.micro} is too old (need >= 3.8)"
        )
        return False


def test_imports():
    """test if all required packages can be imported."""
    print("\nChecking Python packages...")

    packages = {
        "click": "click",
        "rich": "rich",
        "dotenv": "python-dotenv",
        "git": "GitPython",
        "requests": "requests",
        "dateutil": "python-dateutil",
        "fuzzywuzzy": "fuzzywuzzy",
    }

    all_ok = True
    for module, package in packages.items():
        try:
            __import__(module)
            print(f"✓ {package} is installed")
        except ImportError:
            print(f"✗ {package} is not installed")
            all_ok = False

    return all_ok


def test_project_structure():
    """test if project files are in place."""
    print("\nChecking project structure...")

    required_files = [
        "main.py",
        "requirements.txt",
        "setup.py",
        ".env.example",
        "README.md",
        "src/__init__.py",
        "src/config.py",
        "src/utils.py",
        "src/pr_collector.py",
        "src/commit_collector.py",
        "src/diff_viewer.py",
        "src/matcher.py",
        "src/ai_analyzer.py",
        "src/cli.py",
    ]

    all_ok = True
    for file_path in required_files:
        path = Path(file_path)
        if path.exists():
            print(f"✓ {file_path} exists")
        else:
            print(f"✗ {file_path} is missing")
            all_ok = False

    return all_ok


def test_external_tools():
    """test if external tools are available."""
    print("\nChecking external tools...")
    import subprocess

    tools = {
        "git": ["git", "--version"],
        "gh": ["gh", "--version"],
    }

    all_ok = True
    for tool_name, command in tools.items():
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print(f"✓ {tool_name} is installed")
            else:
                print(f"✗ {tool_name} is not working properly")
                all_ok = False
        except FileNotFoundError:
            print(f"✗ {tool_name} is not installed")
            all_ok = False
        except Exception as e:
            print(f"✗ Error checking {tool_name}: {str(e)}")
            all_ok = False

    return all_ok


def test_gh_auth():
    """test if GitHub CLI is authenticated."""
    print("\nChecking GitHub CLI authentication...")
    import subprocess

    try:
        result = subprocess.run(
            ["gh", "auth", "status"], capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            print("✓ GitHub CLI is authenticated")
            return True
        else:
            print("✗ GitHub CLI is not authenticated")
            print("  Run: gh auth login")
            return False
    except Exception as e:
        print(f"✗ Error checking authentication: {str(e)}")
        return False


def test_config():
    """test if configuration is set up."""
    print("\nChecking configuration...")

    env_file = Path(".env")
    if env_file.exists():
        print("✓ .env file exists")
        return True
    else:
        print("⚠ .env file not found (optional)")
        print("  Copy .env.example to .env to customize settings")
        return True


def main():
    """run all tests."""
    print("=" * 60)
    print("GitHub PR Analyzer - Installation Test")
    print("=" * 60)

    tests = [
        ("Python Version", test_python_version),
        ("Python Packages", test_imports),
        ("Project Structure", test_project_structure),
        ("External Tools", test_external_tools),
        ("GitHub Authentication", test_gh_auth),
        ("Configuration", test_config),
    ]

    results = {}
    for test_name, test_func in tests:
        results[test_name] = test_func()

    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)

    for test_name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test_name}: {status}")

    all_passed = all(results.values())

    print("\n" + "=" * 60)
    if all_passed:
        print("✓ All tests passed! Installation is complete.")
        print("\nYou can now use the tool:")
        print("  python main.py --help")
        return 0
    else:
        print("✗ Some tests failed. Please fix the issues above.")
        print("\nRefer to INSTALL.md for troubleshooting.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
