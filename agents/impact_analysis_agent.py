from agents.base_agent import BaseAgent
class ImpactAnalysisAgent(BaseAgent):

    def run(self, query, context=None):

        impacted = self.tools["impact_analysis"].impact_analysis(
    context["repo_path"],
    query
)

        prompt = f"""
You are a system impact analyzer.

Question:
{query}

Impact Analysis:
{impacted}

Provide:

1. Risk level
2. What may break
3. Why it may break
4. Safe modification suggestions
"""

        return self.llm(prompt)