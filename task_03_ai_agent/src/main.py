import sys
from pathlib import Path

# Add the project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from task_03_ai_agent.src.agent import get_agent_response


def main():

    print("=" * 50)
    print("          MULTI-TOOL AI AGENT")
    print("=" * 50)

    print("\nAvailable Tools:")
    print("1. Calculator")
    print("2. File Reader")
    print("3. Web Search")

    print("\nType 'exit' to stop the agent.")

    while True:

        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            print("\nAI Agent: Goodbye!")
            break

        if not user_input:
            print("Please enter a question.")
            continue

        print("\nAI Agent is working...")

        try:
            response = get_agent_response(user_input)
            print("\nAI Agent:", response)

        except Exception as error:
            print("\nError:", error)


if __name__ == "__main__":
    main()
