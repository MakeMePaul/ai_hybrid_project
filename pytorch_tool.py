from transformers import pipeline

# Lädt beim ersten Start automatisch ein kleines PyTorch-Modell herunter
print("Lade PyTorch-Modell...")
classifier = pipeline("sentiment-analysis")
print("Modell bereit!")

def klassifiziere_text(text: str) -> str:
    """
    Analysiert einen Text lokal mit PyTorch und gibt die Stimmung zurück.
    """
    ergebnis = classifier(text)[0]
    label = ergebnis['label']
    score = ergebnis['score']
    
    return f"Ergebnis der lokalen PyTorch-Analyse: {label} (Sicherheit: {score:.2f})"

# Kleiner Test, wenn du die Datei direkt ausführst:
if __name__ == "__main__":
    test_text = "Die neue Software-Version stürzt ständig ab, ich brauche dringend Hilfe!"
    print(klassifiziere_text(test_text))