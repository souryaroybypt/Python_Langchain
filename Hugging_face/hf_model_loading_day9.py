from transformers import pipeline,logging
import re

logging.set_verbosity_error()  

# summarization pipeline with facebook/bart-large-cnn
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

wiki_text = """One of the earliest and most influential turns to neoliberal reform occurred in Chile after an economic crisis in the early 1970s. "
    "After several years of socialist economic policies under president Salvador Allende, a 1973 coup d'état, which established a military junta under dictator Augusto Pinochet, "
    "led to the implementation of a number of sweeping neoliberal economic reforms that had been proposed by the Chicago Boys, a group of Chilean economists educated under Milton Friedman. "
    "This 'neoliberal project' served as 'the first experiment with neoliberal state formation' and provided an example for neoliberal reforms elsewhere.[84] "
    "Beginning in the early 1980s, the Reagan administration and Thatcher government implemented a series of neoliberal economic reforms to counter the chronic stagflation the United States and United Kingdom had each experienced throughout the 1970s. "
    "Neoliberal policies continued to dominate American and British politics until the Great Recession.[75] "
    "Following British and American reform, neoliberal policies were exported abroad, with countries in Latin America, the Asia-Pacific, the Middle East, and China implementing significant neoliberal reform. "
    "Additionally, the International Monetary Fund and World Bank encouraged neoliberal reforms in many developing countries by placing reform requirements on loans, in a process known as structural adjustment."""


# Summarizer
summary = summarizer(wiki_text, max_length=100, min_length=30, do_sample=False)
print("Summary",summary)

summary_text = summary[0]['summary_text']
two_sentences = " ".join(re.split(r'(?<=[.!?]) +', summary_text)[:2]) # trim para to get only 2 lines
print(two_sentences)
