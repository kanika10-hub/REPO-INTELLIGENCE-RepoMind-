from base_agent import BaseAgent
class OnboardingAgent(BaseAgent):

    def run(self, query, context=None):

        entry_points = self.tools["dependency_graph"].get_entry_points()

        key_files = self.tools["vector_store"].search(
            "main entry initialization startup"
        )

        prompt = f"""
You are an onboarding assistant.

User Question: {query}

Entry Points:
{entry_points}

Key Files:
{key_files}

Give a step-by-step learning path.
"""

        return self.llm(prompt)