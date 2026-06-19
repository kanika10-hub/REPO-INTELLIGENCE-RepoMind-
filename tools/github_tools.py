import os
from git import Repo



def clone_repo(repo_url: str):

    try:
        # RepoMind project root
        BASE_DIR = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        # Storage folder
        REPO_STORAGE = os.path.join(
            BASE_DIR,
            "repos",
            "cloned_repos"
        )

        # Create folders if missing
        os.makedirs(REPO_STORAGE, exist_ok=True)

        # Extract repo name
        repo_name = (
            repo_url.rstrip("/")
            .split("/")[-1]
            .replace(".git", "")
        )

        save_path = os.path.join(
            REPO_STORAGE,
            repo_name
        )

        if os.path.exists(save_path):
            return {
                "status": "already_exists",
                "path": save_path
            }

        Repo.clone_from(
            repo_url,
            save_path
        )

        return {
            "status": "success",
            "path": save_path,
            "cwd": os.getcwd(),
            "save_path": save_path
        }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e),
            "cwd": os.getcwd()
        }
    
def repo_metadata(repo_path):

    total_files = 0

    language_counts = {
        ".py": 0,
        ".js": 0,
        ".ts": 0,
        ".java": 0,
        ".cpp": 0
    }

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            total_files += 1

            ext = os.path.splitext(file)[1]

            if ext in language_counts:
                language_counts[ext] += 1

    return {
        "total_files": total_files,
        "languages": language_counts
    }


def generate_repo_summary(repo_path):

    files = []

    for root, dirs, filenames in os.walk(repo_path):

        for file in filenames:
            files.append(file)

    summary = []

    if "requirements.txt" in files:
        summary.append(
            "Python project detected"
        )

    if "package.json" in files:
        summary.append(
            "JavaScript/Node project detected"
        )

    if "Dockerfile" in files:
        summary.append(
            "Uses Docker"
        )

    if ".github" in str(files):
        summary.append(
            "GitHub Actions configured"
        )

    return {
        "summary": summary
    }

import os


def get_folder_purposes(repo_path):

    folders = []

    for item in os.listdir(repo_path):

        full_path = os.path.join(
            repo_path,
            item
        )

        if os.path.isdir(full_path):

            purpose = "Unknown"

            if item.lower() == "src":
                purpose = "Application source code"

            elif item.lower() == "tests":
                purpose = "Testing code"

            elif item.lower() == "docs":
                purpose = "Documentation"

            elif item.lower() == "config":
                purpose = "Configuration files"

            folders.append(
                {
                    "folder": item,
                    "purpose": purpose
                }
            )

    return folders