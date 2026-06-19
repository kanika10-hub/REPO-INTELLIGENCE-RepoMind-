import os


def list_files(path: str):
    """
    List all files and folders in a directory.
    """
    try:
        return os.listdir(path)
    except Exception as e:
        return {"error": str(e)}


def read_file(file_path: str):
    """
    Read contents of a file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return {"error": str(e)}


def search_text(directory: str, query: str):
    """
    Search text across all files in a directory.
    """
    results = []

    try:
        for root, _, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)

                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        lines = f.readlines()

                    for idx, line in enumerate(lines, start=1):
                        if query.lower() in line.lower():
                            results.append(
                                {
                                    "file": filepath,
                                    "line": idx,
                                    "content": line.strip(),
                                }
                            )

                except:
                    continue

        return results

    except Exception as e:
        return {"error": str(e)}
    

