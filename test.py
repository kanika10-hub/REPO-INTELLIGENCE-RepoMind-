import os


def load_python_files(repo_path):

    files = []

    skip_dirs = {
        ".venv",
        "__pycache__",
        ".git",
        "chroma_db"
    }

    for root, dirs, filenames in os.walk(repo_path):

        # Skip unwanted directories
        dirs[:] = [
            d for d in dirs
            if d not in skip_dirs
        ]

        for file in filenames:

            if file.endswith(".py"):

                files.append(
                    os.path.join(root, file)
                )

    return files


repo_path = r"D:\summer26\R&D\RepoMind"

python_files = load_python_files(repo_path)

print("\n=== PYTHON FILES FOUND ===\n")

for f in python_files:
    print(f)

print("\n==========================")
print(f"Total Python Files: {len(python_files)}")