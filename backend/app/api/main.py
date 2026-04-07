"""API entry point for Uvicorn."""
import sys
from pathlib import Path

# Add parent directories to path to import from root main.py
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from main import app  # noqa: E402

__all__ = ["app"]
