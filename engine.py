import os
from openai import OpenAI
from llmlingua import PromptCompressor
import chromadb
from pypdf import PdfReader

class FiscalEngine:
    def __init__(self):
        self.ai = OpenAI()
        self.compressor = PromptCompressor()
        self.db_client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.db_client.get_or_create_collection("fiscal_data")

    def ingest_pdf(self, file):
        reader = PdfReader(file)
        text_blocks = [page.extract_text() for page in reader.pages if page.extract_text()]
        ids = [f"p_{i}" for i in range(len(text_blocks))]
        self.collection.add(documents=text_blocks, ids=ids)

    def run_query(self, query):
        # 1. Retrieve
        results = self.collection.query(query_texts=[query], n_results=3)
        raw_context = "\n".join(results['documents'][0])

        # 2. Compress (Logic for Intermediate level)
        compressed = self.compressor.compress_prompt(
            [raw_context],
            instruction=query,
            target_token=500,
            rank_method="longllmlingua"
        )
        
        # 3. Generate
        prompt = f"Using this compressed data: {compressed['compressed_prompt']}\n\nAnswer: {query}"
        res = self.ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        # 4. Dummy stats for visualization (In prod, these are extracted from LLM)
        stats = {
            "saved": len(raw_context.split()) - len(compressed['compressed_prompt'].split()),
            "ratio": round(len(raw_context.split()) / len(compressed['compressed_prompt'].split()), 1),
            "growth": 8, "risk": 3, "stability": 7
        }
        
        return res.choices[0].message.content, stats