import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax


class ModelService:

    def __init__(
        self,
        model_name="distilbert-base-uncased-finetuned-sst-2-english",
        revision="714eb0fa89d2f80546fda750413ed43d93601a13",
    ):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            revision=revision
        )

        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            revision=revision
        ).to(self.device)

        self.model.eval()

    def predict(self, text: str):

        encoded = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
        )

        encoded = {k: v.to(self.device) for k, v in encoded.items()}

        with torch.no_grad():
            logits = self.model(**encoded).logits
            probs = softmax(logits, dim=1)

        neg = probs[0][0].item()
        pos = probs[0][1].item()

        label = "POSITIVE" if pos > neg else "NEGATIVE"

        return {
            "label": label,
            "confidence": pos if label == "POSITIVE" else neg,
            "probabilities": {
                "negative": neg,
                "positive": pos,
            },
        }


model_service = ModelService()