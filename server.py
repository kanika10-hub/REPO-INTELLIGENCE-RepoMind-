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


mcp = FastMCP("RepoMind")


@mcp.tool()
def list_repo_files(path: str):
    """
    List files and folders inside a directory.
    """
    return list_files(path)


@mcp.tool()
def read_repo_file(file_path: str):
    """
    Read contents of a file.
    """
    return read_file(file_path)


@mcp.tool()
def search_repo_text(directory: str, query: str):
    """
    Search text across repository files.
    """
    return search_text(directory, query)


@mcp.tool()
def repo_python_files(directory: str):
    return find_python_files(directory)


@mcp.tool()
def repo_entry_points(directory: str):
    return find_entry_points(directory)


@mcp.tool()
def repo_directory_structure(directory: str):
    return get_directory_structure(directory)


@mcp.tool()
def repo_file_summary(file_path: str):
    return get_file_summary(file_path)

@mcp.tool()
def clone_github_repo(repo_url: str):
    return clone_repo(repo_url)


@mcp.tool()
def get_repo_metadata(repo_path: str):
    return repo_metadata(repo_path)


@mcp.tool()
def summarize_repo(repo_path: str):
    return generate_repo_summary(repo_path)


@mcp.tool()
def analyze_folders(repo_path: str):
    return get_folder_purposes(repo_path)

@mcp.tool()
def debug_paths():
    import os

    return {
        "cwd": os.getcwd(),
        "server_file": __file__,
    }

if __name__ == "__main__":
    print("Starting RepoMind FastMCP server...")
    mcp.run()
