#!/bin/bash
# Step 1: Create a virtual environment in your project folder
python3.13 -m venv venv

# Step 2: Activate the virtual environment
source venv/bin/activate

# Step 3: Install needed packages inside the venv
pip install docker requests docker-py
