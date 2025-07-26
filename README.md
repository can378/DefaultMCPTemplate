# MCP Server & AI agent

simple MCP (Model Context Protocol) server and AI agent template

using [FastMCP](https://github.com/chain-ml/model-context-protocol) library and `httpx`


## ⚠️ warning
- python 3.10+

---

# MCP Server Test

```bash
# 1. Create and activate a Python virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Install required packages
pip install httpx "mcp[cli]"

# 3. Run the MCP server
cd mcp_server
mcp dev main.py

```

### ❗ERROR - No module named 'mcp_server'

This usually means the Python path is not set correctly.

```bash
# Set PYTHONPATH to the root of your project
set PYTHONPATH=<project root path>
# Example:
set PYTHONPATH=C:\workspace\DefaultMCPTemplate
```

### Optional: For MCP Inspector

Arguments 

```run --with mcp main.py```

Command

```uv```

---

# MCP AI Agent Test

```bash
#1. create .env on root and add "OPENAI_API_KEY"
OPENAI_API_KEY=dddd.....

#2.  Install required packages
pip install langchain langchain-openai python-dotenv openai

#3. Run the mcp agent
cd mcp_agent
python main.py

```