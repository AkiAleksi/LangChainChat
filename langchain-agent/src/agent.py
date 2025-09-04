import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain_openai import ChatOpenAI  # Use ChatOpenAI for chat models

# Load environment variables from .env file
load_dotenv(dotenv_path="/Users/aki/Desktop/HelloWorld/.env")

class LangchainAgent:
    def __init__(self):
        self.config = None
        self.chain = None

    def initialize(self, config):
        self.config = config
        # Initialize LangChain components
        template = "You are a helpful assistant. User said: {user_input}"
        prompt = PromptTemplate(input_variables=["user_input"], template=template)
        openai_api_key = os.getenv("OPENAI_API_KEY")  # Fetch API key from .env
        if not openai_api_key:
            raise Exception("OPENAI_API_KEY not found in environment variables.")
        llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)  # Use ChatOpenAI
        self.chain = prompt | llm  # Use the `|` operator to chain components

    def run(self):
        if self.config is None:
            raise Exception("Agent not initialized. Please call initialize() with a valid config.")
        # Main loop for the agent's operation
        print("Type 'exit' or 'quit' to stop the agent.")
        while True:
            user_input = input("Enter your input: ")
            if user_input.lower() in ["exit", "quit"]:  # Check for exit command
                print("Shutting down the agent. Goodbye!")
                break
            response = self.process_input(user_input)
            print(response)

    def process_input(self, user_input):
        # Use LangChain to process the input
        if self.chain is None:
            raise Exception("LangChain not initialized. Please call initialize() first.")
        response = self.chain.invoke({"user_input": user_input})  # Use invoke method
        return response.content  # Access the content attribute of the AIMessage object

if __name__ == "__main__":
    agent = LangchainAgent()
    config = {}  # Add any configuration you need here
    agent.initialize(config)
    agent.run()