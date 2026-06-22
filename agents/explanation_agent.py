from base_agent import BaseAgent
class ExplanationAgent(BaseAgent):

    def run(self, query, context=None):

        relevant_code = self.tools["vector_store"].search(query)

        call_flow = self.tools["dependency_graph"].trace_flow("auth")

        prompt = f"""
Explain clearly how this system works.

Question: {query}

Relevant Code:
{relevant_code}

Call Flow:
{call_flow}

Explain step-by-step.
"""

        return self.llm.generate(prompt)