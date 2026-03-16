FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH=/app
ENV TOKENIZERS_PARALLELISM=false
ENV HF_HOME=/models
ENV TF_CPP_MIN_LOG_LEVEL=3

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader \
    punkt \
    averaged_perceptron_tagger \
    wordnet \
    omw-1.4 \
    stopwords \
    universal_tagset

COPY scripts/download_model.py ./scripts/download_model.py
RUN python scripts/download_model.py

COPY scripts/download_textattack_assets.py ./scripts/download_textattack_assets.py
RUN python scripts/download_textattack_assets.py

COPY app/ ./app
COPY attacks/ ./attacks
COPY scripts/ ./scripts

RUN mkdir -p reports

CMD ["python", "-m", "app.attack_engine"]