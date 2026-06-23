
class AgentOrchestrator:

    def __init__(self, agents):
        self.agents = agents

    def route(self, query,context=None):

        query_lower = query.lower()

        if "start" in query_lower or "where should i begin" in query_lower:
            return self.agents["onboarding"].run(query,context)

        elif "how" in query_lower:
            return self.agents["explanation"].run(query,context)

        elif "bug" in query_lower or "failing" in query_lower:
            return self.agents["bug"].run(query,context)
        elif "what breaks" in query_lower or "impact" in query_lower:
            return self.agents["impact"].run(query,context)

        else:
            return self.agents["explanation"].run(query,context)