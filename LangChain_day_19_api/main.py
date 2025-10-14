from fastapi import FastAPI
from pydantic import BaseModel
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_huggingface import ChatHuggingFace
from dotenv import load_dotenv
import uvicorn

load_dotenv()
app = FastAPI()

llm = ChatHuggingFace(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    temperature=0.2,
)

prompt = ChatPromptTemplate.from_template(
    """You are a helpful assistant. Use only the information provided below.

Context:
{context}

Question:
{question}

Answer:"""
)

chain = LLMChain(prompt=prompt, llm=llm)


class QARequest(BaseModel):
    context: str
    question: str


@app.post("/qa")
async def qa_endpoint(data: QARequest):
    response = chain.run(context=data.context, question=data.question)
    return {"answer": response.strip()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
