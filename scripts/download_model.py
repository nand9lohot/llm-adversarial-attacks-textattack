from transformers import AutoTokenizer, AutoModelForSequenceClassification

model = "distilbert-base-uncased-finetuned-sst-2-english"

print("Downloading tokenizer...")
AutoTokenizer.from_pretrained(model)

print("Downloading model...")
AutoModelForSequenceClassification.from_pretrained(model)

print("Model cached successfully")