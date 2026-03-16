import textattack

print("Downloading TextAttack word embeddings...")

textattack.shared.utils.download_from_s3("word_embeddings/paragramcf")

print("TextAttack assets cached successfully")