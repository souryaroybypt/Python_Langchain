from transformers import pipeline,AutoTokenizer

# sentiment analyser
sentiment_analyzer = pipeline("sentiment-analysis")
result = sentiment_analyzer("I love Hugging Face!")
print(result)
print('###########################################################################################')

# sentiment summarizer
summarizer = pipeline("summarization")
text = """Neoliberalism originated among European liberal scholars in the 1930s. It arose in response to the decline of classical liberalism, as social liberalism increasingly favored market regulation. The Great Depression shaped this shift, leading to policies aimed at stabilizing volatile free markets. These measures sought to prevent a repeat of the economic failures of the early 1930s, which were often linked to classical liberal policies.

In policymaking, neoliberalism came to describe a shift following the inability of the post-war consensus and neo-Keynesian economics to resolve the stagflation of the 1970s. The 1973 oil crisis, however, was an external factor beyond the control of any economic model.

The dissolution of the Soviet Union and the end of the Cold War further facilitated the global rise of neoliberalism, particularly in the United States and the United Kingdom."""
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
print(summary)

print('###########################################################################################')

# Tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
tokens = tokenizer("Hugging Face is amazing!", return_tensors="pt")
print(tokens)
print('###########################################################################################')

# sentiment analysis for 3 sentences
# sentiment_analyzer = pipeline("sentiment-analysis")

sentences = [
    "I absolutely love this new phone, it’s fantastic!",
    "This movie was boring and way too long.",
    "The weather is okay, not great but not terrible either."
]

for s in sentences:
    result = sentiment_analyzer(s)
    print(f"Sentence: {s}")
    print(f"Result: {result}\n")
    print('###########################################################################################')