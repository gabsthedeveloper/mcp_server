import asyncio
import os

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider
from pydantic_ai.mcp import MCPServerStreamableHTTP

load_dotenv()


LLM_URL = os.getenv('LLM_URL')
LLM_MODEL = os.getenv('LLM_MODEL')
LLM_API_KEY = os.getenv('LLM_API_KEY')


# Define the model
model = OllamaModel(
    model_name=LLM_MODEL,
    provider=OllamaProvider(
        base_url=LLM_URL,
        api_key=LLM_API_KEY
    )
)

server = MCPServerStreamableHTTP('http://localhost:8000/mcp')

agent = Agent(model=model, toolsets=[server])


async def main():
    result = await agent.run('What is my favorite color?')
    print(result.output)


asyncio.run(main())
