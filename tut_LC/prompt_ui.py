from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompt import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", task="text-generation"
)

model = ChatHuggingFace(llm=llm)

st.header("Research Tool")
user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    res = model.invoke(user_input)
    st.text(res.content)

paper_input = st.selectbox(
    "Select Paper",
    [
        "Select ...",
        "Attention Is All You Need (Vaswani et al., 2017)",
        "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (Devlin et al., 2018)",
        "GPT-3: Language Models are Few-Shot Learners (Brown et al., 2020)",
        "ResNet: Deep Residual Learning for Image Recognition (He et al., 2015)",
        "Denoising Diffusion Probabilistic Models (Ho et al., 2020)",
    ],
)

style_input = st.selectbox(
    "select explanation style",
    ["High School Level", "Technical", "Code-Oriented", "Mathematical"],
)

length_input = st.selectbox(
    "select length",
    [
        "short( 1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanations)",
    ],
)

if st.button("Fetch"):
    st.text("Hello")
