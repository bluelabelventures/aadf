#!/bin/bash

# AADF Installation Script
# This script checks prerequisites and sets up the AADF framework

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

echo "======================================"
echo "AADF Framework Installation Script"
echo "======================================"
echo

# Check for Git
echo "Checking prerequisites..."
if command -v git &> /dev/null; then
    print_status "Git is installed ($(git --version))"
else
    print_error "Git is not installed. Please install Git first."
    echo "Visit: https://git-scm.com/downloads"
    exit 1
fi

# Check for Python 3
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    print_status "Python 3 is installed ($PYTHON_VERSION)"
    
    # Check Python version is 3.8 or higher
    PYTHON_VERSION_MAJOR=$(python3 -c 'import sys; print(sys.version_info[0])')
    PYTHON_VERSION_MINOR=$(python3 -c 'import sys; print(sys.version_info[1])')
    
    if [ "$PYTHON_VERSION_MAJOR" -eq 3 ] && [ "$PYTHON_VERSION_MINOR" -ge 8 ]; then
        print_status "Python version meets requirements (3.8+)"
    else
        print_warning "Python 3.8 or higher is recommended. You have Python $PYTHON_VERSION_MAJOR.$PYTHON_VERSION_MINOR"
    fi
else
    print_error "Python 3 is not installed. Please install Python 3.8 or higher."
    echo "Visit: https://www.python.org/downloads/"
    exit 1
fi

# Check for pip
if command -v pip3 &> /dev/null || command -v pip &> /dev/null; then
    print_status "pip is installed"
else
    print_error "pip is not installed. Please install pip."
    echo "Run: python3 -m ensurepip"
    exit 1
fi

echo
echo "Making scripts executable..."

# Make Python scripts executable
find . -name "*.py" -type f -exec chmod +x {} \; 2>/dev/null || true
print_status "Python scripts are now executable"

# Make shell scripts executable
find . -name "*.sh" -type f -exec chmod +x {} \; 2>/dev/null || true
print_status "Shell scripts are now executable"

# Check if main launcher exists
if [ -f "aadf.py" ]; then
    chmod +x aadf.py
    print_status "Main launcher (aadf.py) is ready"
else
    print_warning "aadf.py not found in current directory"
fi

echo
echo "======================================"
echo "Installation Complete!"
echo "======================================"
echo
echo "Quick Start Guide:"
echo "1. Create a virtual environment (recommended):"
echo "   python3 -m venv venv"
echo "   source venv/bin/activate  # On Windows: venv\\Scripts\\activate"
echo
echo "2. Install dependencies:"
echo "   pip install -r requirements.txt"
echo
echo "3. Configure your environment:"
echo "   cp .env.example .env"
echo "   # Edit .env with your API keys and settings"
echo
echo "4. Launch AADF:"
echo "   python aadf.py"
echo "   # Or if you made it executable: ./aadf.py"
echo
echo "For more information, see README.md"
echo "Report issues at: https://github.com/yourusername/aadf/issues"
echo

# Optional: Create alias for easier access
read -p "Would you like to create an alias 'aadf' for easy access? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    AADF_PATH=$(pwd)/aadf.py
    
    # Detect shell and add alias
    if [ -n "$ZSH_VERSION" ]; then
        # Zsh
        echo "alias aadf='python3 $AADF_PATH'" >> ~/.zshrc
        print_status "Added alias to ~/.zshrc"
        echo "Run 'source ~/.zshrc' to use the alias immediately"
    elif [ -n "$BASH_VERSION" ]; then
        # Bash
        if [ -f ~/.bash_profile ]; then
            echo "alias aadf='python3 $AADF_PATH'" >> ~/.bash_profile
            print_status "Added alias to ~/.bash_profile"
            echo "Run 'source ~/.bash_profile' to use the alias immediately"
        else
            echo "alias aadf='python3 $AADF_PATH'" >> ~/.bashrc
            print_status "Added alias to ~/.bashrc"
            echo "Run 'source ~/.bashrc' to use the alias immediately"
        fi
    else
        print_warning "Could not detect shell type. Please add the following alias manually:"
        echo "alias aadf='python3 $AADF_PATH'"
    fi
fi

echo
print_status "Setup complete! Happy coding with AADF!"