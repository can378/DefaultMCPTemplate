import random
from mcp_server.mcp_instance import mcp

WORDS = [
    "apple", "banana", "grape", "orange", "mango",
    "peach", "plum", "cherry", "melon", "kiwi"
]

@mcp.tool(
    name="random_words_tool",
    description="Return 3 random words from a predefined list"
)
def random_words(dummy_input: str = "") -> list[str]:
    return random.sample(WORDS, 3)


@mcp.tool(
    name="random_number_tool",
    description="Return a random number between min and max (inclusive)"
)
def random_number(min: int = 1, max: int = 100) -> int:
    if min > max:
        temp=min
        min=max
        max=temp
    return random.randint(min, max)