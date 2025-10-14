from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Step 1: Load PDF
loader = PyPDFLoader("./sampletext.pdf")  # path to your 2-page PDF
documents = loader.load()
print(f"Loaded {len(documents)} pages from PDF.")

# # Step 2: Split into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_docs = text_splitter.split_documents(documents)

# # Step 3: Initialize Hugging Face model
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# # Step 4: Create summarization chain
chain = load_summarize_chain(
    llm=model,
    chain_type="map_reduce",
    verbose=True
)

# # Step 5: Run summarization
summary = chain.run(split_docs)

print("\n=== Summary of the PDF ===\n")
print(summary)