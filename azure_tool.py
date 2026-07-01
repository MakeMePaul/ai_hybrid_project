import os
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Lädt die geheimen Schlüssel aus deiner .env-Datei
load_dotenv()

def fasse_text_zusammen(text: str) -> str:
    """
    Schickt einen Text an Azure AI (Cloud) und bittet um eine Zusammenfassung.
    """
    # Zieht die echten Schlüssel aus dem System (bereitgestellt durch dotenv)
    azure_endpoint = os.environ.get("AZURE_ENDPOINT")
    azure_key = os.environ.get("AZURE_KEY")

    # Kleiner Sicherheitscheck
    if not azure_key or "hier_fügst_du_jetzt" in azure_key:
        return "Fehler: Der Azure Key fehlt oder ist noch der Platzhalter!"

    try:
        # Der tatsächliche Anruf bei Azure
        client = ChatCompletionsClient(
            endpoint=azure_endpoint,
            credential=AzureKeyCredential(azure_key)
        )
        
        response = client.complete(
            messages=[
                SystemMessage(content="Du bist ein hilfreicher Assistent. Fasse den Text in einem kurzen Satz zusammen."),
                UserMessage(content=text),
            ],
            model="gpt-5-mini" # Das Modell, das du in Azure bereitgestellt hast
        )
        return f"Azure Zusammenfassung: {response.choices[0].message.content}"
        
    except Exception as e:
        return f"Fehler bei der Azure-Verbindung: {str(e)}"

# Ein kleiner Test, wenn du die Datei direkt ausführst:
if __name__ == "__main__":
    
    test_text = """
    Ticket-ID: 88392. Der Kunde meldet, dass das firmeninterne ERP-System seit heute 
    Morgen um 8:00 Uhr extrem langsam reagiert und teilweise komplett einfriert. 
    Zunächst wurde ein Problem mit der lokalen Internetverbindung vermutet, aber ein 
    Ping-Test des Nutzers zeigte normale Latenzen. Bei genauerer Untersuchung durch den 
    First-Level-Support stellte sich heraus, dass ein automatisiertes Datenbank-Backup, 
    welches eigentlich tief in der Nacht laufen sollte, aufgrund eines Fehlers in der 
    Zeitsteuerung hängen geblieben ist. Dieser Prozess blockiert nun 95% der CPU-Ressourcen 
    auf dem Hauptserver. Der Kunde ist sehr frustriert und bittet um eine schnelle 
    Lösung, da die Buchhaltung ihre Monatsberichte heute zwingend abschließen muss.
    """
    
    print("Sende Text an Azure OpenAI in Frankfurt...")
    ergebnis = fasse_text_zusammen(test_text)
    
    print("\n--- ERGEBNIS ---")
    print(ergebnis)
    print("----------------")