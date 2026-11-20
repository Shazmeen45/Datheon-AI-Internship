
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0,
    num_predict=150
)

prompt = """
Answer the question using the facts below.

Facts:
1. Artificial Intelligence is a branch of computer science.
2. AI focuses on creating machines and software that perform tasks
   normally requiring human intelligence.
3. Machine Learning is a subset of Artificial Intelligence.
4. Machine Learning allows computers to learn patterns from data
   and make predictions.

Question:
What is the difference between AI and Machine Learning?

Give a simple answer in two bullet points.
"""

response = llm.invoke(prompt)

print("\nLLM TEST ANSWER:\n")
print(response.content)
