from mcp_server.mcp_instance import mcp

@mcp.tool(
    name="add two number tool",
    description="you can add two numbers"
)
def add(num1: int,num2: int) -> int:

    if num1 is None or num2 is None:
        return "ther is no appropriate numbers"
    return num1+num2



@mcp.tool(
    name="subtract two numbers tool",
    description="tool to subtract two numbers"
)
def subtract(num1: int,num2: int) -> int:

    if num1 is None or num2 is None:
        return "ther is no appropriate numbers"
    return abs(num1-num2)



@mcp.tool(
    name="multiply all numbers tool",
    description="tool to multiply all numbers"
)
def multiply_all(num_list: list[int]) -> int:
    result = 1
    for num in num_list:
        result *= num
    return result