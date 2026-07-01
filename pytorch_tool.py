from transformers import pipeline

# Lädt ein Modell zur Erkennung von Namen (NER)
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

def anonymisiere_text(text: str) -> str:
    entities = ner_pipeline(text)
    anonymisierter_text = text
    # Wir ersetzen alle gefundenen Namen/Orte durch [ANONYM]
    for entity in sorted(entities, key=lambda x: x['start'], reverse=True):
        start, end = entity['start'], entity['end']
        anonymisierter_text = anonymisierter_text[:start] + "[ANONYM]" + anonymisierter_text[end:]
    return anonymisierter_text