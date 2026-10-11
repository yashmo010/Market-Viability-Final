"""Application Launcher for Launch-Blind Product Viability System.

Usage:
    python run_app.py

Launches the unified FastAPI backend serving the interactive React dashboard
at http://127.0.0.1:8000.
"""

import sys
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

if __name__ == "__main__":
    print("=" * 70)
    print("Launching Autonomous Product Viability System Dashboard...")
    print("Serving UI & Backend at: http://127.0.0.1:8000")
    print("Press Ctrl+C to terminate the application.")
    print("=" * 70)
    try:
        import uvicorn
        sys.path.insert(0, str(ROOT_DIR))
        uvicorn.run("src.app.api:app", host="127.0.0.1", port=8000, reload=False)
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
