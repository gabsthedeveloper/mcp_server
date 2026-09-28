from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def get_favorite_color() -> str:
    return 'Teal'

if __name__ == '__main__':
    mcp.run(transport="http", host="0.0.0.0", port=8000)
