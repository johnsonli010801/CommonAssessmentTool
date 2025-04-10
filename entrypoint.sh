#!/bin/bash

# Wait for the database to be ready (adjust as needed for your DB setup)
echo "Waiting for the database to be ready..."
sleep 10  # This is a simple sleep; in a production scenario, use a loop with checks.

# Run data initialization script
echo "Initializing data..."
python initialize_data.py

# Start the main application
echo "Starting the application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
