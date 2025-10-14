from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import HuggingFaceChat
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not HF_TOKEN:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN is not set in .env")

# 1. Load PDF
loader = PyPDFLoader("./sampletext.pdf")
documents = loader.load()
print(f"Loaded {len(documents)} pages from PDF.")

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = splitter.split_documents(documents)
print(f"Split into {len(texts)} chunks.")
print("First chunk preview:", texts[0].page_content[:300])

# 3. Create embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 4. Store in FAISS
vectorstore = FAISS.from_documents(texts, embedding_model)
vectorstore.save_local("faiss_index")

# 5. Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 6. Load LLM
llm = HuggingFaceChat(
    model_name="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.2
)

# 7. Build RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
)

# 8. Ask a query
query = "How to reduce carbon footprint?"
answer = qa_chain.run(query)
print("Answer:", answer)