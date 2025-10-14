from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
    task='text-generation'
)

model = ChatHuggingFace(llm = llm)
# result = model.invoke("What is the capital of India (in one sentence please) ?")
# print(result.content)

sentence = 'Give me a glass of water'

# Instruction for the model
prompt = f"Please rewrite the following sentence in polite and professional English while preserving its meaning:\n\n'{sentence}'"

result = model.invoke(prompt)
print(result.content)