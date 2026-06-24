import pandas as pd
from transformers import pipeline

MODEL_PATH = "models/robertuito_finetuned"

classifier = pipeline(
    "sentiment-analysis",
    model=MODEL_PATH,
    tokenizer=MODEL_PATH
)

df = pd.read_csv("data/processed/comentarios_hoteles_sintetico.csv")

sentimientos = []
scores = []

for texto in df["texto"]:
    result = classifier(texto)[0]

    sentimientos.append(result["label"])
    scores.append(round(result["score"], 4))

df["sentimiento"] = sentimientos
df["score"] = scores

df.to_csv("data/processed/comentarios_hoteles_predicho.csv", index=False, encoding="utf-8")

print("CSV con predicciones generado correctamente")
