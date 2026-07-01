from mcp.server.fastmcp import FastMCP
from pytorch_tool import klassifiziere_text
from azure_tool import fasse_text_zusammen

mcp = FastMCP("Mein KI-Hybrid-Server")

@mcp.tool()
def lokaler_klassifikator(text: str) -> str:
    """Nutze dieses Tool, um herauszufinden, ob ein Text positiv oder negativ ist."""
    return klassifiziere_text(text)

@mcp.tool()
def cloud_zusammenfassung(text: str) -> str:
    """Nutze dieses Tool, um einen langen Text zusammenzufassen."""
    return fasse_text_zusammen(text)

if __name__ == "__main__":
    mcp.run()