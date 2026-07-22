#!/bin/bash

# 1. Activate the project virtual environment
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
else
    echo "Could not find virtual environment activation script."
    exit 1
fi

# 2. Execute the test suite
pytest tests/test_app.py

# 3. Return exit code 0 if all tests passed, or 1 if something went wrong
if [ $? -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
