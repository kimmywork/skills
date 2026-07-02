#!/bin/bash

# Check if CLOUDCONVERT_API_KEY environment variable is set
if [ -n "$CLOUDCONVERT_API_KEY" ]; then
    echo "✓ CLOUDCONVERT_API_KEY is set"
    # Don't print the actual key for security reasons
    echo "API key length: ${#CLOUDCONVERT_API_KEY} characters"
else
    echo "✗ CLOUDCONVERT_API_KEY is not set"
    echo ""
    echo "To set the API key:"
    echo "1. Get your API key from: https://cloudconvert.com/dashboard/api/v2/keys"
    echo "2. Set it as an environment variable:"
    echo "   export CLOUDCONVERT_API_KEY=your_key_here"
    echo ""
    echo "Or add it to your shell profile (~/.bashrc, ~/.zshrc, etc.)"
    exit 1
fi