from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", task="text-generation"
)

model = ChatHuggingFace(llm=llm)

summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in 2 sentences:\n\n{text}",
)

summary_chain = LLMChain(llm=model, prompt=summary_prompt, output_key="summary")

keyword_prompt = PromptTemplate(
    input_variables=["summary"],
    template="Extract the 5 most important keywords from the following summary:\n\n{summary}",
)

keyword_chain = LLMChain(llm=model, prompt=keyword_prompt, output_key="keywords")

overall_chain = SequentialChain(
    chains=[summary_chain, keyword_chain],
    input_variables=["text"],
    output_variables=["summary", "keywords"],
    verbose=True,
)

# Step 5: Run the chain
text_input = """
The Akula class submarines, also known as the Project 971 Shchuka-B class, are a series of nuclear-powered attack submarines designed and built for the Soviet Navy and later operated by the Russian Navy. The name "Akula" means "shark" in Russian, which reflects the submarine's aggressive and formidable design.The Akula class submarines are considered to be among the quietest and most advanced submarines in the world, making them highly effective in stealth reconnaissance and anti-ship and anti-submarine warfare. The submarines have a double hull design, with a pressure hull made of high-strength titanium alloy, which allows them to operate at great depths of up to 600 meters.The Akula class submarines are powered by a pressurized water reactor, which provides a sustained power output of approximately 51,000 shaft horsepower, enabling them to reach speeds of up to 35 knots while submerged. The submarines are equipped with a variety of torpedoes, anti-ship missiles, and cruise missiles, as well as mines and decoys, giving them a powerful and versatile weapon system.The Akula class submarines feature a sophisticated suite of sensors, including advanced sonar and radar systems, electronic intelligence gathering equipment, and a variety of countermeasure systems for self-defense. The submarines also have a large complement of crew members, typically around 80, who are trained to operate and maintain the complex systems and equipment on board.The first Akula class submarine, the K-284, was commissioned in 1984, and a total of seven submarines were built by the end of the decade. However, the collapse of the Soviet Union in 1991 led to a decline in funding for the Russian Navy, and only four of the seven submarines remain in service today. Despite this, the Akula class submarines continue to be a significant component of the Russian Navy's submarine fleet, and they are regarded as a major strategic asset for the country.In recent years, there have been reports of upgrades and modernization programs for the Akula class submarines, including the installation of new weapon systems, sensors, and communications equipment. These upgrades are intended to enhance the submarines' capabilities and extend their service lives for many years to come, ensuring that the Akula class submarines will remain a formidable presence on the world's oceans for the foreseeable future.
"""

result = overall_chain.invoke({"text": text_input})

print("Summary:\n", result["summary"])
print("\nKeywords:\n", result["keywords"])
