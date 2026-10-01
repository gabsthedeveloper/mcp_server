from mcp.server.mcpserver import MCPServer

mcp = MCPServer("MCP_Server")

@mcp.tool()
def get_favorite_color() -> str:
    return 'Teal'

if __name__ == '__main__':
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
