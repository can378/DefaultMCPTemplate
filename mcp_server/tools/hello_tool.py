from mcp_server.mcp_instance import mcp

@mcp.tool(
    name="hello tool",
    description="this will say hello to user"
)
def hello(dummy_input: str = "") -> str:

    return "hello this is for test"