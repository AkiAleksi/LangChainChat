# LangChain Agent

This project implements a simple conversational agent using [LangChain](https://github.com/hwchase17/langchain) and OpenAI's `gpt-3.5-turbo` model. The agent takes user input, processes it through a LangChain pipeline, and generates responses using OpenAI's chat model.

## Features
- **Dynamic Prompting**: Uses `PromptTemplate` to structure user input.
- **OpenAI Integration**: Powered by OpenAI's `gpt-3.5-turbo` model.
- **Interactive Conversation**: Allows users to interact with the agent in a terminal-based interface.
- **Graceful Exit**: Type `exit` or `quit` to stop the agent.

## Prerequisites
- Python 3.8 or higher
- OpenAI API key

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/langchain-agent.git
   cd langchain-agent

  2.Create a virtual environment:

Install dependencies:

Set up your .env file:

Create a .env file in the project root.
Add your OpenAI API key:
Usage
Run the agent:
python3 src/agent.py
Interact with the agent:

Enter your input in the terminal.
Type exit or quit to stop the agent.
File Structure
langchain-agent/
├── src/
│   ├── agent.py       # Main agent implementation
├── .env               # Environment variables (not included in Git)
├── .gitignore         # Git ignore file
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

Dependencies
langchain
langchain-openai
python-dotenv
openai
Install all dependencies using:
pip install -r requirements.txt
Notes
Ensure your .env file is not included in version control to keep your API key secure.
This project is a basic implementation and can be extended with additional LangChain features.

