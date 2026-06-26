from tools.github_tools import (
    clone_repo,
    repo_metadata,
    generate_repo_summary
)

from tools.vector_store import (
    index_repository
)

from tools.dependency_graph import (
    repository_dependencies
)


def analyze_repository(repo_url):

    # Clone repository
    clone_result = clone_repo(
        repo_url
    )

    if clone_result["status"] == "failed":
        return clone_result

    repo_path = clone_result["path"]

    #print("Repository cloned")

    # Metadata
    metadata = repo_metadata(
        repo_path
    )

    #print("Metadata generated")

    # Summary
    summary = generate_repo_summary(
        repo_path
    )

    #print("Summary generated")

    # Dependency graph
    dependencies = repository_dependencies(
        repo_path
    )

    #print("Dependencies analyzed")

    # Vector indexing
    repo_name = (
    repo_url.rstrip("/")
    .split("/")[-1]
    .replace(".git", "")
)

    index_result = index_repository(
        repo_path,
        repo_name
    )

    #print("Repository indexed")

    return {
    "status": "ready",
    "repo_name": repo_name,
    "repo_path": repo_path,
    "indexed_chunks": index_result["indexed_chunks"],
    "metadata": metadata,
    "summary": summary
}