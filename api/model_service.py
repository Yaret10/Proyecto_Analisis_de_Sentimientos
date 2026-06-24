from transformers import pipeline

BASE_MODEL_NAME = "pysentimiento/robertuito-sentiment-analysis"
FINETUNED_MODEL_PATH = "models/robertuito_finetuned"

base_classifier = pipeline(
    "sentiment-analysis",
    model=BASE_MODEL_NAME,
    tokenizer=BASE_MODEL_NAME
)

finetuned_classifier = pipeline(
    "sentiment-analysis",
    model=FINETUNED_MODEL_PATH,
    tokenizer=FINETUNED_MODEL_PATH
)


def predict_base(text: str):
    result = base_classifier(text)[0]

    return {
        "model": "base",
        "text": text,
        "label": result["label"],
        "score": round(result["score"], 4)
    }


def predict_finetuned(text: str):
    result = finetuned_classifier(text)[0]

    return {
        "model": "finetuned",
        "text": text,
        "label": result["label"],
        "score": round(result["score"], 4)
    }
