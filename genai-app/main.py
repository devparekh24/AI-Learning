from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import os
import faiss
import numpy as np
from dotenv import load_dotenv
import google.generativeai as genai
from rag_pdf import process_pdf, get_embedding

load_dotenv()

app = FastAPI()
genai.configure(api_key=os.getenv("AI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

UPLOAD_FOLDER = "uploads"


class Query(BaseModel):
    question: str


# 📤 Upload PDF
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    chunks_count = process_pdf(file_path)

    return {"message": "PDF processed", "chunks": chunks_count}


# ❓ Ask questions
@app.post("/ask")
def ask(query: Query):
    index = faiss.read_index("index.faiss")
    chunks = np.load("chunks.npy", allow_pickle=True)

    query_vector = np.array([get_embedding(query.question)]).astype("float32")

    k = 3
    distances, indices = index.search(query_vector, k)

    context = "\n".join([chunks[i] for i in indices[0]])

    response = model.generate_content(
        f"Answer based on the PDF content.\n\nContext:\n{context}\n\nQuestion: {query.question}"
    )

    return {"answer": response.text, "context": context}
