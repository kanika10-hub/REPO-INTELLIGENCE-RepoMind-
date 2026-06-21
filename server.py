from mcp.server.fastmcp import FastMCP

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
    analyze_repository
)

from tools.dependency_graph import (
    repository_dependencies,
    impacted_files,
    dependency_chain,
    critical_files
)

mcp = FastMCP("RepoMind")


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
def repo_dependencies(
    repo_path: str
):
    """
    Analyze repository dependency graph.
    """
    return repository_dependencies(
        repo_path
    )

@mcp.tool()
def impact_analysis(
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

if __name__ == "__main__":
    print("Starting RepoMind FastMCP server...")
    mcp.run()
