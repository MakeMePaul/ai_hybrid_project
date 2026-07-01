# Hybrid-KI Support-Pipeline

Dieses Projekt bietet eine sichere und effiziente Lösung zur automatisierten Verarbeitung von IT-Support-Tickets durch eine Hybrid-Architektur.

## Architektur
- **Lokale Komponente (Edge):** Nutzt `PyTorch` und `Transformers` für die lokale Anonymisierung sensibler Daten und Sentiment-Analyse. Daten verlassen das lokale System erst nach der Anonymisierung.
- **Cloud-Komponente (Azure):** Nutzt Azure OpenAI (`gpt-5-mini`) zur intelligenten Zusammenfassung komplexer technischer Probleme.

## Funktionen
1. **Automatisierte Überwachung:** Überwacht Eingangs-Ordner auf neue Ticket-Dateien.
2. **Datenschutz:** Lokale Anonymisierung schützt personenbezogene Daten vor der Cloud-Verarbeitung.
3. **Effizienz:** Schnelle Kategorisierung der Dringlichkeit durch lokale Sentiment-Analyse.
4. **Intelligenz:** Hochpräzise Zusammenfassung durch Cloud-LLMs.

## Installation & Start
1. Virtuelle Umgebung aktivieren: `source venv/bin/activate`
2. Pipeline starten: `python folder_pipeline.py`
3. Ticket-Datei in `tickets_eingang/` ablegen.