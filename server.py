from mcp.server.fastmcp import FastMCP
from tools.ask_repo import ask_repo

from tools.file_tools import (
    list_files,
    read_file,
    search_text
    
)
from tools.explorer_tools import (
    find_python_files,
    find_entry_points,
    get_directory_structure,
    get_file_summary

)

from tools.github_tools import (
    clone_repo,
    repo_metadata,
    generate_repo_summary,
    get_folder_purposes
)

from tools.code_intelligence import (
    find_classes,
    find_functions,
    find_imports,
    find_api_routes,
    generate_file_intelligence,
    analyze_repository,
    extract_functions,
    extract_classes,
    extract_function_chunks
)

from tools.dependency_graph import (
    extract_imports,
     build_dependency_graph,
    repository_dependencies,
    impacted_files,
    dependency_chain,
    critical_files
)

from tools.vector_store import (
    index_repository,
    semantic_search
)

from tools.impact_analysis import (
    impact_analysis,
    find_function_callers
)

from tools.repo_ingestion import (
    analyze_repository
)
from agents.orchestrator import AgentOrchestrator
from agents.onboarding_agent import OnboardingAgent
from agents.explanation_agent import ExplanationAgent
from agents.bug_investigation_agent import BugInvestigationAgent
from agents.impact_analysis_agent import ImpactAnalysisAgent

from tools.repo_ingestion import analyze_repository




mcp = FastMCP("RepoMind")

@mcp.tool()
def analyze_and_prepare(
    repo_url: str
):
    """
    Clone, analyze, index and prepare a repository
    for future questions.
    """

    result = analyze_repository(
        repo_url
    )

    return result

@mcp.tool()
def list_repo_files(path: str):
    """
    List all files and folders inside a directory.

    Use this tool when you need to explore repository structure
    before reading or analyzing files.
    """
    return list_files(path)


@mcp.tool()
def read_repo_file(file_path: str):
    """
    Read and return the contents of a file.

    Use this tool when you need to inspect source code,
    configuration files, documentation, or project files.
    """
    return read_file(file_path)
@mcp.tool()
def search_repo_text(directory: str, query: str):
    """
    Search for a text pattern across repository files.

    Use this tool to locate keywords, functions, classes,
    APIs, imports, or implementation details.
    """
    return search_text(directory, query)

@mcp.tool()
def repo_python_files(directory: str):
    """
    Find all Python files in a repository.

    Use this tool when identifying code modules,
    project structure, or files for further analysis.
    """
    return find_python_files(directory)

@mcp.tool()
def repo_entry_points(directory: str):
    """
    Detect likely application entry points.

    Finds files such as main.py, app.py, server.py,
    manage.py, index.js, and similar startup files.
    """
    return find_entry_points(directory)

@mcp.tool()
def repo_directory_structure(directory: str):
    """
    Generate a directory tree of the repository.

    Use this tool to understand the overall layout
    before performing deeper code analysis.
    """
    return get_directory_structure(directory)

@mcp.tool()
def repo_file_summary(file_path: str):
    """
    Generate a summary of a file.

    Use this tool to quickly understand a file's purpose
    before reading the complete contents.
    """
    return get_file_summary(file_path)


@mcp.tool()
def clone_github_repo(repo_url: str):
    """
    Clone a GitHub repository to local storage.

    Use this tool before analyzing repositories that
    are provided as GitHub URLs.
    """
    return clone_repo(repo_url)

@mcp.tool()
def get_repo_metadata(repo_path: str):
    """
    Analyze repository statistics.

    Returns file counts, language distribution,
    and repository-level metadata.
    """
    return repo_metadata(repo_path)

@mcp.tool()
def summarize_repo(repo_path: str):
    """
    Generate a high-level repository summary.

    Detects technologies, project type, Docker usage,
    GitHub Actions, and other important characteristics.
    """
    return generate_repo_summary(repo_path)

@mcp.tool()
def analyze_folders(repo_path: str):
    """
    Analyze repository folders and infer their purpose.

    Identifies source code directories, test folders,
    documentation, configuration folders, and more.
    """
    return get_folder_purposes(repo_path)
@mcp.tool()
def debug_paths():
    """
    Return server execution paths and environment details.

    Use this tool only for debugging MCP server issues,
    path resolution problems, or repository storage errors.
    """
    import os

    return {
        "cwd": os.getcwd(),
        "server_file": __file__,
    }

@mcp.tool()
def repo_classes(file_path: str):
    """
    Find all classes defined in a Python file.
    """
    return find_classes(file_path)


@mcp.tool()
def repo_functions(file_path: str):
    """
    Find all functions defined in a Python file.
    """
    return find_functions(file_path)


@mcp.tool()
def repo_imports(file_path: str):
    """
    Find all imports used in a Python file.
    """
    return find_imports(file_path)


@mcp.tool()
def repo_routes(file_path: str):
    """
    Detect FastAPI API routes in a Python file.
    """
    return find_api_routes(file_path)


@mcp.tool()
def file_intelligence(file_path: str):
    """
    Generate a complete structural analysis of a Python file.
    """
    return generate_file_intelligence(file_path)


@mcp.tool()
def repository_intelligence(repo_path: str):
    """
    Analyze all Python files in a repository.
    """
    return analyze_repository(repo_path)

@mcp.tool()
def get_functions(repo_path: str):
    """
    Extract all functions from a repository.
    """
    return extract_functions(repo_path)


@mcp.tool()
def get_classes(repo_path: str):
    """
    Extract all classes from a repository.
    """
    return extract_classes(repo_path)


@mcp.tool()
def get_function_chunks(repo_path: str):
    """
    Extract function-level chunks for embedding/indexing.
    """
    return extract_function_chunks(repo_path)


@mcp.tool()
def get_imports(file_path: str):
    """
    Extract imports from a Python file.
    """
    return extract_imports(file_path)


@mcp.tool()
def get_dependency_graph(repo_path: str):
    """
    Build repository dependency graph.
    """
    return build_dependency_graph(repo_path)


@mcp.tool()
def get_repo_dependencies(
    repo_path: str
):
    """
    Analyze repository dependency graph.
    """
    return repository_dependencies(
        repo_path
    )

@mcp.tool()
def get_impacted_files(
    repo_path: str,
    target_file: str
):
    """
    Find files affected by
    changing a file.
    """
    return impacted_files(
        repo_path,
        target_file
    )

@mcp.tool()
def find_dependency_path(
    repo_path: str,
    source_file: str,
    destination_file: str
):
    """
    Find dependency path
    between two files.
    """
    return dependency_chain(
        repo_path,
        source_file,
        destination_file
    )


@mcp.tool()
def repository_hotspots(
    repo_path: str
):
    """
    Find critical files with
    highest dependency count.
    """
    return critical_files(
        repo_path
    )



@mcp.tool()
def build_repo_embeddings(
    repo_path: str,
    collection_name: str
):
    """
    Build embeddings for a repository
    and store them in ChromaDB.
    """
    return index_repository(
        repo_path,
        collection_name
    )

@mcp.tool()
def search_repository(
    question: str,
    collection_name: str
):
    """
    Search repository using
    semantic similarity.
    """
    return semantic_search(
        question,
        collection_name
    )

@mcp.tool()
def ask_repository(question: str):

    """
    Ask questions about the indexed repository.
    """

    return ask_repo(question)


@mcp.tool()
def analyze_impact(
    repo_path: str,
    function_name: str
):
    """
    Analyze the impact of modifying a function.
    """
    return impact_analysis(
        repo_path,
        function_name
    )


@mcp.tool()
def get_function_callers(
    repo_path: str,
    function_name: str
):
    """
    Find all callers of a function.
    """
    return find_function_callers(
        repo_path,
        function_name
    )



@mcp.tool()
def ingest_repository(
    repo_url: str
):
    return analyze_repository(
        repo_url
    )



if __name__ == "__main__":
    mcp.run()
