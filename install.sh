#!/bin/bash

# Verify the script is run from the correct directory
if [ ! -f "np.py" ] || [ ! -d "templates" ]; then
    echo "Error: Please run this script from the directory containing np.py and templates/"
    echo "Change to the np directory and run:"
    echo "cd /path/to/np"
    echo "sudo ./install.sh"
    exit 1
fi

# Get absolute path of current directory
NP_DIR="$(pwd)"

# System-wide installation
if [ "$(id -u)" -ne 0 ]; then
    echo "Root privileges required. Please run with sudo:"
    echo "sudo ./install.sh"
    exit 1
fi

echo "Installing np system-wide..."

# 1. Make the script executable
chmod +x "$NP_DIR/np.py"

# 2. Create symlink in /usr/local/bin
ln -sf "$NP_DIR/np.py" /usr/local/bin/np

# 3. Verify installation
if ! command -v np &> /dev/null; then
    echo "Error: Installation failed!"
    echo "Please ensure /usr/local/bin is in your PATH"
    exit 1
fi

echo "Successfully installed!"
echo "You can now use the 'np' command from any directory"
echo "Original files remain in: $NP_DIR"
