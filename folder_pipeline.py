import os
import time
from pytorch_tool import klassifiziere_text
from azure_tool import fasse_text_zusammen

# Wir definieren unsere Ordner
EINGANG_ORDNER = "tickets_eingang"
AUSGANG_ORDNER = "tickets_ausgang"

def setup_ordner():
    """Erstellt die Ordner, falls sie noch nicht existieren."""
    os.makedirs(EINGANG_ORDNER, exist_ok=True)
    os.makedirs(AUSGANG_ORDNER, exist_ok=True)

def main():
    setup_ordner()
    print(f"👀 Überwache Ordner '{EINGANG_ORDNER}' auf neue .txt Dateien...\n")

    # Eine Endlos-Schleife, die permanent läuft
    while True:
        # Schau nach, was im Eingangs-Ordner liegt
        for dateiname in os.listdir(EINGANG_ORDNER):
            if dateiname.endswith(".txt"):
                filepath = os.path.join(EINGANG_ORDNER, dateiname)
                print(f"📥 Neue Datei entdeckt: {dateiname} - Starte Analyse...")

                # 1. Den Text aus der Datei lesen
                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read()

                # 2. Unsere Hybrid-KI arbeiten lassen
                stimmung = klassifiziere_text(text)
                zusammenfassung = fasse_text_zusammen(text)

                # 3. Das Ergebnis in den Ausgangs-Ordner schreiben
                ausgangs_filepath = os.path.join(AUSGANG_ORDNER, f"analyse_{dateiname}")
                with open(ausgangs_filepath, "w", encoding="utf-8") as f:
                    f.write(f"=== KI ANALYSE BERICHT ===\n")
                    f.write(f"Original-Datei: {dateiname}\n")
                    f.write(f"Dringlichkeit/Stimmung: {stimmung}\n")
                    f.write("-" * 30 + "\n")
                    f.write(f"Zusammenfassung:\n{zusammenfassung}\n")

                # 4. Die Originaldatei löschen, damit sie nicht doppelt verarbeitet wird
                os.remove(filepath)
                print(f"✅ Analyse fertig! Ergebnis liegt im Ordner '{AUSGANG_ORDNER}'.\n")

        # Das Skript 2 Sekunden schlafen lassen, um den Prozessor zu schonen
        time.sleep(2)

if __name__ == "__main__":
    main()