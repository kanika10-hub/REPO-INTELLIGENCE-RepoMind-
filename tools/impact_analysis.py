import os


def impact_analysis(repo_path, target_name):

    affected_files = []

    for root, dirs, files in os.walk(repo_path):

        if ".venv" in root:
            continue

        for file in files:

            if not file.endswith(".py"):
                continue

            file_path = os.path.join(
                root,
                file
            )

            try:

                with open(
                    file_path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    content = f.read()

                if target_name in content:

                    affected_files.append(
                        file_path
                    )

            except:
                continue

    return {
        "target": target_name,
        "affected_files": affected_files,
        "count": len(affected_files)
    }

import ast
import os


def find_function_callers(
    repo_path,
    target_function
):

    callers = []

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if not file.endswith(".py"):
                continue

            path = os.path.join(
                root,
                file
            )

            try:

                with open(
                    path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    source = f.read()

                tree = ast.parse(source)

                for node in ast.walk(tree):

                    if (
                        isinstance(node, ast.Call)
                        and isinstance(
                            node.func,
                            ast.Name
                        )
                    ):

                        if (
                            node.func.id
                            == target_function
                        ):

                            callers.append(
                                path
                            )

            except:
                pass

    return list(
        set(callers)
    )