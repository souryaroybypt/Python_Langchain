from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Virat Kohli is known for his aggressive batting style and remarkable consistency across all formats.",
    "Rohit Sharma holds the record for the highest individual score in ODI cricket with his explosive double centuries.",
    "M. S. Dhoni is celebrated for his calm leadership and ability to finish matches under pressure.",
    "Sachin Tendulkar, often called the 'God of Cricket', inspired generations with his extraordinary batting records.",
    "Jasprit Bumrah is renowned for his deadly yorkers and precision as one of the best fast bowlers in modern cricket."
]

query = "Tell me about Virat Kohli"
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

print(cosine_similarity([query_embedding],doc_embeddings))
scores = cosine_similarity([query_embedding],doc_embeddings)[0]
# print(list(enumerate(scores)))
index, score = sorted (list(enumerate(scores)), key = lambda x:x[1])[-1]
# print(index,score)
print(documents[index])
print(f"Similarity Score is {score}")
