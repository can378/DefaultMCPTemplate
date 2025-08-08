from mcp_server.mcp_instance import mcp

@mcp.tool(
    name="hello tool",
    description="this will say hello to user"
)
def hello(dummy_input: str = "") -> str:

    return "hello this is for test"

@mcp.resource("greeting://{name}")
def get_greeting(name:str)->str:
    """get a personalized greeting"""
    return f"HEllo, {name}"

mcp.prompt()
def greet_user(name:str, style:str="friendly") -> str:
    """Generate a greeting prompt"""
    result=""
    return result