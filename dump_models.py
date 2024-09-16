from os import getenv

from sentence_transformers import SentenceTransformer, CrossEncoder

# Sentences we want sentence embeddings for
sentences = ['This is an example sentence', 'Each sentence is converted']

# Load model from HuggingFace Hub
sentence_name = f'{getenv("ENCODER_MODEL_NAME_USER", "sentence-transformers")}/{getenv("ENCODER_MODEL_NAME", "all-MiniLM-L6-v2")}'
model = SentenceTransformer(sentence_name)

# Create embeddigs + normalisation
model.encode(sentences=sentences, normalize_embeddings=True, convert_to_tensor= True)

print("Sentence embeddings has been computed successfully, the model is working!")

# We can now dump the model on disk
model.save("./embedder_model_files")

question = "how are you doing?"
crossencoder_model = f'{getenv("CROSSENCODER_MODEL_NAME_USER", "cross-encoder")}/{getenv("CROSSENCODER_MODEL_NAME", "ms-marco-TinyBERT-L-2-v2")}'
model = CrossEncoder(crossencoder_model)
inputs = [[question, sentence] for sentence in sentences]
out = model.predict(inputs)
print("Cross encoder is working!")

model.save("./cross_encoder_model_files")