from tools.llm import ask_llm
from tools.vector_store import semantic_search


def ask_repo(question):

    results = semantic_search(
        question
    )

    context = ""

    for doc, meta in zip(
        results["documents"][0],
        results["metadatas"][0]
    ):

        context += f"""

Function:
{meta['name']}

File:
{meta['file']}

RELEVANCE:
Retrieved because it matched the user query.

Code:
{doc}

"""

    prompt = f"""
You are a repository assistant.

Answer the question using ONLY
the repository context.

Question:
{question}

Repository Context:
{context}
"""

    return ask_llm(prompt)