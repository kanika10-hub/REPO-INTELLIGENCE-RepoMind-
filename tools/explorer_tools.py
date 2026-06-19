import os


def find_python_files(directory: str):
    """
    Find all Python files in a repository.
    """
    python_files = []

    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    python_files.append(full_path)

        return python_files

    except Exception as e:
        return {"error": str(e)}


def find_entry_points(directory: str):
    """
    Find possible application entry points.
    """
    entry_points = []

    common_entry_files = {
        "main.py",
        "app.py",
        "server.py",
        "run.py",
        "manage.py",
    }

    try:
        for root, _, files in os.walk(directory):

            for file in files:
                filepath = os.path.join(root, file)

                # common filenames
                if file in common_entry_files:
                    entry_points.append(filepath)

                # __main__ check
                if file.endswith(".py"):
                    try:
                        with open(filepath, "r", encoding="utf-8") as f:
                            content = f.read()

                        if 'if __name__ == "__main__"' in content:
                            if filepath not in entry_points:
                                entry_points.append(filepath)

                    except:
                        continue

        return {"entry_points": entry_points}

    except Exception as e:
        return {"error": str(e)}


def get_directory_structure(directory: str):
    """
    Generate tree-like directory structure.
    """

    try:
        tree = []

        for root, dirs, files in os.walk(directory):

            level = root.replace(directory, "").count(os.sep)
            indent = "│   " * level

            tree.append(f"{indent}{os.path.basename(root)}/")

            subindent = "│   " * (level + 1)

            for file in files:
                tree.append(f"{subindent}{file}")

        return "\n".join(tree)

    except Exception as e:
        return {"error": str(e)}


def get_file_summary(file_path: str):
    """
    Basic file summary without LLM.
    Phase 2 version.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.readlines()

        total_lines = len(content)

        functions = []
        classes = []
        imports = []

        for line in content:

            stripped = line.strip()

            if stripped.startswith("def "):
                functions.append(
                    stripped.split("(")[0].replace("def ", "")
                )

            elif stripped.startswith("class "):
                classes.append(
                    stripped.split("(")[0]
                    .replace("class ", "")
                    .replace(":", "")
                )

            elif stripped.startswith("import ") or stripped.startswith(
                "from "
            ):
                imports.append(stripped)

        return {
            "file": file_path,
            "total_lines": total_lines,
            "functions": functions,
            "classes": classes,
            "imports": imports,
        }

    except Exception as e:
        return {"error": str(e)}