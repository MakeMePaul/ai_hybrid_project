import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

def fasse_text_zusammen(text: str) -> str:
    """
    Schickt einen Text an Azure AI (Cloud) und bittet um eine Zusammenfassung.
    """
    # HIER trägst du später deine echten Azure-Daten ein:
    azure_endpoint = os.getenv("AZURE_ENDPOINT", "DEIN_AZURE_ENDPOINT_HIER")
    azure_key = os.getenv("AZURE_KEY", "DEIN_AZURE_API_KEY_HIER")
    
    # Schutzmechanismus, falls du noch keine Keys hast:
    if azure_key == "DEIN_AZURE_API_KEY_HIER":
        return f"[MOCK-MODUS] Azure ist noch nicht verbunden. Der Text war: '{text[:30]}...'"

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
            model="gpt-4o-mini" # oder das Modell, das eure Firma nutzt
        )
        return f"Azure Zusammenfassung: {response.choices[0].message.content}"
        
    except Exception as e:
        return f"Fehler bei der Azure-Verbindung: {str(e)}"