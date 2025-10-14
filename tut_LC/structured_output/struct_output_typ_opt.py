from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
    task='text-generation'
)

class Review(TypedDict):
    themes: Annotated[list['str'], 'list out all key themes mentioned']
    summary: Annotated[str,"A one sentence summary of the review"]
    sentiment: Annotated[str,"return sentiment of the review, postive, negative or neutral"]
    pros:Annotated[Optional[list[str]],"Return a list of keywords related to pros if any"]
    cons:Annotated[Optional[list[str]],"Return a list of keywords related to cons if any"]
    cons:Annotated[Optional[str],"Name of the individual writing the review"]

model = ChatHuggingFace(llm = llm)
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""This phone is a complete letdown. After just six months, the battery life has plummeted, barely lasting half a day even with light use. The camera, while advertised as high-end, produces grainy photos in anything less than perfect sunlight. Worst of all, the software is consistently buggy, freezing up during simple tasks and forcing a restart. For a premium price, I expected reliability and performance, but this device has delivered neither. It feels flimsy and cheap in hand, and I deeply regret this purchase.""")
print(result)
