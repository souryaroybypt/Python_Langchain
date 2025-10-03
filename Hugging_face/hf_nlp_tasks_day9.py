from transformers import pipeline, logging

logging.set_verbosity_error()

# Translation: English to French using Helsinki-NLP/opus-mt-en-fr
translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr",  # task-specific model
)

english_text = "Hugging Face provides powerful tools for natural language processing."
french_translation = translator(english_text)
print("French Translation:", french_translation[0]["translation_text"])


# Question-Answering using distilbert
qa = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad",  # task-specific QA model
)

context = """
The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. 
It was named after the engineer Gustave Eiffel, whose company designed and built the tower.
"""
question = "Where is the Eiffel Tower located?"
answer = qa(question=question, context=context)
print("Answer:", answer["answer"])
