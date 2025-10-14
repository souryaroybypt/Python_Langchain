import time
import json
from transformers import pipeline, logging

logging.set_verbosity_error()

distilbert_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
bert_pipeline = pipeline("sentiment-analysis", model="textattack/bert-base-uncased-SST-2")

sentences = sentences = [
    "I absolutely love this new phone, it’s perfect.",
    "The meal was delicious and beautifully presented.",
    "She gave me the best advice I’ve ever received.",
    "I’m really enjoying this book so far.",
    "The weather today is amazing, so bright and warm.",
    "He is such a kind and thoughtful friend.",
    "The concert last night was unforgettable.",
    "This app makes my life so much easier.",
    "I’m proud of the work we accomplished together.",
    "The teacher explained everything so clearly.",
    "That was a wonderful surprise!",
    "I feel optimistic about the future.",
    "The movie was inspiring and beautifully shot.",
    "This coffee tastes fantastic.",
    "I had a great workout this morning.",
    "The team showed incredible dedication.",
    "This new feature works perfectly.",
    "Her smile always brightens my day.",
    "I appreciate your help more than words can say.",
    "Traveling there was the best decision I ever made.",
    "The food was cold and tasteless.",
    "I hate being stuck in traffic for hours.",
    "This product broke the first day I bought it.",
    "The service at the restaurant was terrible.",
    "I feel exhausted and disappointed.",
    "The movie was boring and too long.",
    "He spoke rudely and ignored my questions.",
    "I regret wasting my time on that project.",
    "The software keeps crashing.",
    "That was the worst customer experience I’ve ever had.",
    "I felt lonely and ignored the whole evening.",
    "The package arrived damaged and late.",
    "Nothing about this place feels welcoming.",
    "I can’t believe how careless they were.",
    "It was a frustrating and stressful day.",
    "The store opens at nine o’clock tomorrow.",
    "She lives two blocks away from the park.",
    "The cat is sleeping on the couch.",
    "We met at the library yesterday.",
    "The car is blue and parked outside.",
    "Water boils at one hundred degrees Celsius.",
    "He is reading a newspaper in the garden.",
    "The meeting lasted exactly one hour.",
    "I will travel to New York next month.",
    "They are watching television in the living room.",
    "The trip was fun, but the hotel was disappointing.",
    "I like the design, though it feels a bit overpriced.",
    "The concert was exciting, although the seats were uncomfortable.",
    "The game was thrilling but ended with a frustrating loss.",
    "The class was informative, but the pace was too fast."
]

# measure inference time
def measure_time(pipeline_model, sentences):
    start_time = time.time()
    results = []
    for s in sentences:
        output = pipeline_model(s)
        results.append(output[0])
    end_time = time.time()
    total_time = end_time - start_time
    avg_time = total_time / len(sentences)
    return total_time, avg_time, results

distil_total, distil_avg, distil_results = measure_time(distilbert_pipeline, sentences)

bert_total, bert_avg, bert_results = measure_time(bert_pipeline, sentences)


print(f"DistilBERT - total: {distil_total:.2f}s, avg: {distil_avg:.4f}s")
print(f"BERT      - total: {bert_total:.2f}s, avg: {bert_avg:.4f}s")

log_data = {
    "DistilBERT": {"total_time": distil_total, "average_time_per_sentence": distil_avg},
    "BERT": {"total_time": bert_total, "average_time_per_sentence": bert_avg}
}
with open("inference_speed_log.json", "w") as f:
    json.dump(log_data, f, indent=4)

print("Results saved to inference_speed_log.json")