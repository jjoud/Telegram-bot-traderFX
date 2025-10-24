# config.py
# -------------------------------
# Configuration file for ArabicTraderFXbot
# Safely stores all API keys and credentials
# -------------------------------

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Optional: safety check
if not all([API_ID, API_HASH, BOT_TOKEN, OPENAI_API_KEY]):
    raise ValueError("⚠️ Missing one or more environment variables. Please check your .env file.")
