#!/bin/bash

# Check if cloudconvert CLI is installed
if command -v cloudconvert &> /dev/null; then
    echo "✓ cloudconvert CLI is already installed"
    cloudconvert --version
else
    echo "✗ cloudconvert CLI is not installed"
    echo "Installing cloudconvert CLI..."
    
    # Check if npm is available
    if command -v npm &> /dev/null; then
        npm install -g cloudconvert-cli
        if [ $? -eq 0 ]; then
            echo "✓ cloudconvert CLI installed successfully"
            cloudconvert --version
        else
            echo "✗ Failed to install cloudconvert CLI"
            echo "Please install Node.js and npm first, then run: npm install -g cloudconvert-cli"
            exit 1
        fi
    else
        echo "✗ npm is not available"
        echo "Please install Node.js and npm first, then run: npm install -g cloudconvert-cli"
        exit 1
    fi
fi