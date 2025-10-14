from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

folder_path = "./text"
documents = []
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        loader = TextLoader(os.path.join(folder_path, filename))
        docs = loader.load()
        for d in docs:
            d.metadata["source"] = filename
        documents.extend(docs)

# # 2. Split into chunks (optional)
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = splitter.split_documents(documents)

# print(len(texts))

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(texts, embedding_model)
vectorstore.save_local("faiss_index")

query = "Which file talks about AI?"
results = vectorstore.similarity_search_with_score(query, k=10)

for doc, score in results:
    print(f"Filename -> {doc.metadata['source']}")
    print(f"Score -> {score}")
    print(f"Snippet -> {doc.page_content[:200]}")
    print("-----")
