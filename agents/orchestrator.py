
class AgentOrchestrator:

    def __init__(self, agents):
        self.agents = agents

    def route(self, query):

        query_lower = query.lower()

        if "start" in query_lower or "where should i begin" in query_lower:
            return self.agents["onboarding"].run(query)

        elif "how" in query_lower:
            return self.agents["explanation"].run(query)

        elif "bug" in query_lower or "failing" in query_lower:
            return self.agents["bug"].run(query)

        elif "what breaks" in query_lower or "impact" in query_lower:
            return self.agents["impact"].run(query)

        else:
            return self.agents["explanation"].run(query)