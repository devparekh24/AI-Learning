import os
import numpy as np
import faiss
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("AI_API_KEY"))

# Step 1: Load data
with open("data.txt", "r") as f:
    documents = f.readlines()


# Step 2: Create embeddings
def get_embedding(text):
    response = genai.embed_content(model="models/text-embedding-004", content=text)
    return response["embedding"]


embeddings = [get_embedding(doc) for doc in documents]

# Step 3: Convert to numpy
embedding_matrix = np.array(embeddings).astype("float32")

# Step 4: Create FAISS index
dimension = int(embedding_matrix.shape[1])
index = faiss.IndexFlatL2(dimension)  # pylint: disable=no-value-for-parameter
index.add(embedding_matrix)

# Save for reuse
faiss.write_index(index, "index.faiss")
np.save("docs.npy", documents)

print("✅ Index created!")
