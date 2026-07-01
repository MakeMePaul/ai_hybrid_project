from transformers import pipeline

# 1. Die Sentiment-Analyse (die wir vorher hatten)
# Wir definieren das Modell hier einmal, damit es beim Import geladen wird
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def klassifiziere_text(text: str) -> str:
    result = sentiment_pipeline(text)[0]
    return f"{result['label']} (Sicherheit: {result['score']:.2f})"

# 2. Die neue Anonymisierung (NER)
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

def anonymisiere_text(text: str) -> str:
    entities = ner_pipeline(text)
    anonymisierter_text = text
    # Von hinten nach vorne ersetzen, damit die Indizes nicht verrutschen
    for entity in sorted(entities, key=lambda x: x['start'], reverse=True):
        start, end = entity['start'], entity['end']
        anonymisierter_text = anonymisierter_text[:start] + "[ANONYM]" + anonymisierter_text[end:]
    return anonymisierter_text