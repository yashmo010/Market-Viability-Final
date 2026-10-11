#!/usr/bin/env bash
# Exit on error
set -o errexit

# Upgrade pip and install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Build the React frontend
cd src/app/frontend
npm install
npm run build
cd ../../..
