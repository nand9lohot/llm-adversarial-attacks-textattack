#!/usr/bin/env python3

"""
Environment bootstrap script for the LLM Adversarial Attack Lab.

This script installs required NLP resources that are not automatically
included when installing Python dependencies.

Specifically it downloads NLTK datasets required by TextAttack attacks
such as:

- TextFooler
- BERTAttack
- DeepWordBug

The script is safe to run multiple times.
"""

import nltk
import logging

logging.basicConfig(level=logging.INFO)


NLTK_PACKAGES = [
    "punkt",
    "averaged_perceptron_tagger",
    "wordnet",
    "omw-1.4"
]


def install_nltk_resources():

    logging.info("Installing required NLTK resources")

    for package in NLTK_PACKAGES:
        try:
            nltk.download(package)
            logging.info(f"Installed: {package}")
        except Exception as e:
            logging.error(f"Failed to install {package}: {e}")


def verify_installation():

    logging.info("Verifying installation")

    try:
        # Force load datasets
        nltk.data.find("tokenizers/punkt")
        nltk.data.find("taggers/averaged_perceptron_tagger")

        # Wordnet must be accessed differently
        _ = wordnet.synsets("test")

        logging.info("NLTK verification successful")

    except Exception as e:
        logging.error("NLTK verification failed")
        raise e

def main():

    install_nltk_resources()
    verify_installation()

    logging.info("Environment bootstrap completed successfully")


if __name__ == "__main__":
    main()