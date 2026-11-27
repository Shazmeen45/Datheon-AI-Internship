from langchain_ollama import ChatOllama


# Connect to local Ollama model
llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)


def get_ai_response(user_input):

    response = llm.invoke(user_input)

    return response.content


from langchain.agents import create_agent
from langchain.tools import tool

from task_03_ai_agent.src.tools import (
    calculator,
    read_file,
    web_search
)

@tool
def calculator_tool(expression: str) -> str:
    """
    Calculate mathematical expressions.

    IMPORTANT:
    Pass the mathematical expression as a STRING argument.
    Example: expression="250 * 4"
    Do not pass a JSON schema or dictionary.
    """
    return calculator(expression)


@tool
def file_reader_tool() -> str:
    """Read information from the sample.txt file."""
    return read_file()


@tool
def web_search_tool(query: str) -> str:
    """Search the web for information about a topic."""
    return web_search(query)

# List of available tools
tools = [
    calculator_tool,
    file_reader_tool,
    web_search_tool
]


# Create AI Agent
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
    "You are a helpful multi-tool AI assistant. "
    "Use the available tools whenever needed. "
    "Use calculator_tool for mathematical calculations. "
    "Use file_reader_tool for questions about sample.txt. "
    "Use web_search_tool for current or online information. "
    "For web searches, summarize the retrieved results "
    "and include at least three actual source URLs from the tool output. "
    "Never invent source links or claim information that search results do not support. "
    "Do not provide a final answer until the selected tool has returned its result. "
    "Give clear and simple answers."
    )
)


def get_agent_response(user_input):

    response = agent.invoke({
        "messages": [
            {"role": "user", "content": user_input}
        ]
    })

    # Display agent execution details
    web_results = []

    for message in response["messages"]:

        print("\nMessage Type:", type(message).__name__)

        if type(message).__name__ == "ToolMessage":
            print("Tool Result:", message.content)

            if "Title:" in message.content:
                web_results.append(message.content)

        elif type(message).__name__ == "AIMessage":
            if message.tool_calls:
                print("Tools Called:", message.tool_calls)

    # Get final AI response
    final_answer = response["messages"][-1].content

    # Attach actual web search results
    if web_results:
        final_answer += "\n\nSources:\n" + "\n\n".join(web_results)

    return final_answer
