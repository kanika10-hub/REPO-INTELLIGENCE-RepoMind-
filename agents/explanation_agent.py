from agents.base_agent import BaseAgent
class ExplanationAgent(BaseAgent):

    def run(self, query, context=None):
        print("1. Agent started")
        relevant_code = self.tools["vector_store"].semantic_search(
    query,
    context["repo_name"]
)       
        relevant_code = str(relevant_code)[:4000]
        print("2. Semantic search done")
 
        call_flow = self.tools["dependency_graph"].repository_dependencies(
    context["repo_path"]
)
        call_flow = str(call_flow)[:2000]
        print("3. Dependency analysis done")
        prompt = f"""
Explain clearly how this repository works.

Question:
{query}


Relevant Code:
{relevant_code}

Dependency Flow:
{call_flow}

Explain step-by-step.
"""
        print("4. Calling LLM")
        response= self.llm(prompt)
        print("5. LLM returned")
        return response