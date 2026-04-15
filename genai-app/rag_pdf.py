import os
import numpy as np
import faiss
from pypdf import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("AI_API_KEY"))


# 🔹 Extract text from PDF
def extract_text(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


# 🔹 Split into chunks
def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i : i + chunk_size])
    return chunks


# 🔹 Get embeddings
def get_embedding(text):
    res = genai.embed_content(model="models/text-embedding-004", content=text)
    return res["embedding"]


# 🔹 Process PDF → FAISS
def process_pdf(file_path):
    text = extract_text(file_path)
    chunks = chunk_text(text)

    embeddings = [get_embedding(chunk) for chunk in chunks]

    matrix = np.array(embeddings).astype("float32")

    dimension = int(matrix.shape[1])
    index = faiss.IndexFlatL2(dimension)  # pylint: disable=no-value-for-parameter
    index.add(matrix)

    # Save
    faiss.write_index(index, "index.faiss")
    np.save("chunks.npy", chunks)

    return len(chunks)
