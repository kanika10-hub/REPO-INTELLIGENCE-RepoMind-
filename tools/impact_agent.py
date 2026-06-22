from tools.impact_analysis import (
    find_function_callers
)

from tools.llm import ask_llm


def impact_agent(
    repo_path,
    function_name
):

    callers = find_function_callers(
        repo_path,
        function_name
    )

    prompt = f"""
Function modified:

{function_name}

Affected files:

{callers}

Explain:

1. What may break
2. Risk level
3. Testing recommendations
"""

    return ask_llm(prompt)