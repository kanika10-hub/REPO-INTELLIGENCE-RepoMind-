from agents.base_agent import BaseAgent
class OnboardingAgent(BaseAgent):

    def run(self, query, context=None):

        entry_points = self.tools["dependency_graph"].critical_files(
    context["repo_path"]
)

        key_files = self.tools["vector_store"].semantic_search(
    "main entry initialization startup",
    context["repo_name"]
)

        prompt = f"""
You are an onboarding assistant.

User Question:
{query}

Important Files:
{entry_points}

Relevant Code:
{key_files}

Give a step-by-step learning path for understanding this repository.
"""

        return self.llm(prompt)