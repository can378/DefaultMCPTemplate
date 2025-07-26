from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import asyncio
 
# import mcp tools
from mcp_server import tools

from mcp_server.mcp_instance import mcp


tool_manager = mcp._tool_manager
mcp_tools = tool_manager.list_tools()
# print(mcp_tools)


# load environment variables
load_dotenv()


# Convert to a LangChain Tool
tool_list = []
for tool in mcp_tools:
    tool_list.append(
        Tool(
            name=tool.name,
            description=tool.description,
            func=tool.fn
        )
    )


print(f"🔧 MCP 툴 {len(tool_list)}개 등록 완료")


# set LLM
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)


# Create LangChain Agent
agent = initialize_agent(
    tools=tool_list,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
    agent_kwargs={
        "system_message": """you are a test ai agent."""
    }
)


# CLI
if __name__ == "__main__":
    while True:
        try:
            query = input("👤 question: ")
            if query.lower() in ["exit", "quit"]:
                break
            response = agent.run(query)
            print("🤖 response:", response)
        except KeyboardInterrupt:
            print("\n[terminated]")
            break
