import logging
from model_service import model_service


logging.basicConfig(level=logging.INFO)


TEST_DATA = [
    "This movie is amazing",
    "This was the worst film ever",
    "I enjoyed every moment of it",
    "The storyline was extremely weak",
]


def validate():

    for text in TEST_DATA:

        result = model_service.predict(text)

        logging.info("TEXT: %s", text)
        logging.info("LABEL: %s", result["label"])
        logging.info("CONFIDENCE: %.4f", result["confidence"])
        logging.info("-------------------------------")


if __name__ == "__main__":
    validate()