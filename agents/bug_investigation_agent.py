from base_agent import BaseAgent
class BugInvestigationAgent(BaseAgent):

    def run(self, query, context=None):

        logs = self.tools["vector_store"].search(query)
        affected_code = self.tools["dependency_graph"].find_related("login")

        prompt = f"""
You are a debugging expert.

Problem: {query}

Logs / Similar Code:
{logs}

Related Code:
{affected_code}

List:
1. Possible root causes
2. Likely failing functions
3. Debug steps
"""

        return self.llm.generate(prompt)