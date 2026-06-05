# config.py
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

DATASET_PATH = "data/stem_dataset.csv"

CHROMA_DB_PATH = "chroma_db"
