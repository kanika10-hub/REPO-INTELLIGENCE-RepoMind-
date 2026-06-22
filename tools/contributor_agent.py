from tools.ask_repo import ask_repo

def contributor_agent():

    prompt = """
    Suggest beginner-friendly areas
    to contribute to this repository.
    """

    return ask_repo(prompt)