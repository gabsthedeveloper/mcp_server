import asyncio
import os

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPToolset

load_dotenv()


model = os.getenv('GOOGLE_MODEL')
server = MCPToolset('http://localhost:8000/mcp')
agent = Agent(model=model, toolsets=[server])


async def main():
    result = await agent.run('What is my favorite color?')
    print(result.output)


asyncio.run(main())
