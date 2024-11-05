import os, ell, ollama, datetime, asyncio
from typing import List, Literal
from pydantic import BaseModel, Field

API_KEY = "ollama"
BASE_URL = "http://10.1.1.208:11434"
MODEL_NAME = "nomic-embed-text"
embedding_client: ollama.Client = ollama.Client(host=BASE_URL)

class NomicModel():
    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_embedding(embedding_string: str):
        if not embedding_client is None:
            return embedding_client.embed(MODEL_NAME, input=embedding_string, truncate=False)['embeddings'][0]
        else: return [0.]