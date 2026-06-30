from dotenv import load_dotenv
import os

load_dotenv()

VLLM_URL = os.getenv("VLLM_URL")
CHROMA_PATH = os.getenv("CHROMA_PATH", "data/vectordb")
COLLECTION = "recipes"