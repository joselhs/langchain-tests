# langchain-tests

This repository contains several tests on different LangChain components. In the following list, some of the small tests are described:

- **Simple LLM App with LCEL**: Creation of a Simple app to translate user messages from english to another language. It uses LCEL to create the chain, LangServer to expose it as an API and LangSmith to trace the calls and responses made through the Chain. 
- **Conversational Chatbot**: Creation of a simple Chatbot with message history and session in a Jupyter Notebook
- **Vector Stores and Retrievers**: Use of Vector stores and retriever to look for textual information in a vector database.
- **Simple Agent**: Build a Simple ReAct Agent with Tavily Search tool. Adding memory to agent to remember past interactions.


- **LangGraph**: Contains Tutorials and Tests specific to LangGraph.
    - **Intro to LangGraph**: Introduction to LangGraph where an Agentic ChatBot is built