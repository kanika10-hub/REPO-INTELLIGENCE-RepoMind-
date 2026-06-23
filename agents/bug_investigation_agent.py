from agents.base_agent import BaseAgent


class BugInvestigationAgent(BaseAgent):

    def run(self, query, context=None):

        logs = self.tools["vector_store"].semantic_search(
    query,
    context["repo_name"]
)
        affected_code = self.tools["dependency_graph"].repository_dependencies(
    context["repo_path"]
)

        prompt = f"""
You are a debugging expert.

Problem:
{query}

Relevant Code:
{logs}

Repository Dependencies:
{affected_code}

List:

1. Possible root causes
2. Likely failing functions
3. Debug steps
4. Suggested fixes
"""

        return self.llm(prompt)