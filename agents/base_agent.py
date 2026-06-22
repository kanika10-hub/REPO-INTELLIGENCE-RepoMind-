from tools.llm import ask_llm  # or whatever your LLM class is

class BaseAgent:
    def __init__(self, tools):
        self.llm = ask_llm
        self.tools = tools
        
        self.memory = []

    def run(self, query, context=None):
        raise NotImplementedError
    


