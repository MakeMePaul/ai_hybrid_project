from pytorch_tool import klassifiziere_text
from azure_tool import fasse_text_zusammen

def main():
    ticket_text = """Ticket-ID: 88392. Der Kunde meldet, dass das firmeninterne ERP-System seit heute Morgen um 8:00 Uhr extrem langsam reagiert und teilweise komplett einfriert. Zunächst wurde ein Problem mit der lokalen Internetverbindung vermutet, aber ein Ping-Test des Nutzers zeigte normale Latenzen. Bei genauerer Untersuchung durch den First-Level-Support stellte sich heraus, dass ein automatisiertes Datenbank-Backup, welches eigentlich tief in der Nacht laufen sollte, aufgrund eines Fehlers in der Zeitsteuerung hängen geblieben ist. Dieser Prozess blockiert nun 95% der CPU-Ressourcen auf dem Hauptserver. Der Kunde ist sehr frustriert und bittet um eine schnelle Lösung, da die Buchhaltung ihre Monatsberichte heute zwingend abschließen muss."""

    print("=== STARTE HYBRID-KI-ANALYSE ===\n")

    # Schritt 1: Lokale KI (Schnell, kostenlos, datenschutzkonform)
    print("Schritt 1: Lokale Sentiment-Analyse (PyTorch)...")
    stimmung = klassifiziere_text(ticket_text)
    print(f"-> Lokales Ergebnis: {stimmung}\n")

    # Schritt 2: Cloud KI (Für komplexe Zusammenfassungen)
    print("Schritt 2: Sende an Azure Cloud (gpt-5-mini)...")
    zusammenfassung = fasse_text_zusammen(ticket_text)
    print(f"-> Cloud Ergebnis: {zusammenfassung}\n")

    print("=== HYBRID-PIPELINE ERFOLGREICH BEENDET ===")

if __name__ == "__main__":
    main()