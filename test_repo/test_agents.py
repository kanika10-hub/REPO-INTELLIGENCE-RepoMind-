from tools.vector_store import *
from tools.dependency_graph import *
from tools.impact_analysis import *
tools = {
    "vector_store": __import__(
        "tools.vector_store",
        fromlist=[""]
    ),

    "dependency_graph": __import__(
        "tools.dependency_graph",
        fromlist=[""]
    ),

    "impact_analysis": __import__(
        "tools.impact_analysis",
        fromlist=[""]
    )
}
from agents.onboarding_agent import (
    OnboardingAgent
)

from agents.explanation_agent import (
    ExplanationAgent
)

from agents.impact_analysis_agent import (
    ImpactAnalysisAgent
)

from agents.bug_investigation_agent import (
    BugInvestigationAgent
)

onboarding = OnboardingAgent(tools)

explanation = ExplanationAgent(tools)

impact = ImpactAnalysisAgent(tools)

bug = BugInvestigationAgent(tools)



from agents.orchestrator import (
    AgentOrchestrator
)

orchestrator = AgentOrchestrator(
    {
        "onboarding": onboarding,
        "explanation": explanation,
        "impact": impact,
        "bug": bug
    }
)

context = {
    "repo_name": "repomind",
    "repo_path": r"D:\summer26\R&D\RepoMind"
}

result = orchestrator.route(
    "How does repository cloning work?",
    context
)

print(result)