import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = "models/gemini-1.5-flash"
    EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
    TEMPERATURE = 0.3
    TOP_P = 1
    TOP_K = 32
    CHUNK_SIZE = 1024
    CHUNK_OVERLAP = 20
    INPUT_FILES = ["input.pdf"]
