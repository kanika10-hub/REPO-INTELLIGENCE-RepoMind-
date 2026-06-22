from base_agent import BaseAgent
class ImpactAnalysisAgent(BaseAgent):

    def run(self, query, context=None):

        impacted_files = self.tools["dependency_graph"].find_dependents("User")

        prompt = f"""
You are a system impact analyzer.

Question: {query}

Affected Files:
{impacted_files}

Provide:
1. Risk level (Low/Medium/High)
2. What breaks
3. Why it breaks
4. Safe modification suggestions
"""

        return self.llm.generate(prompt)