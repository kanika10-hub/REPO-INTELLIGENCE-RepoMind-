import os
import ast
import networkx as nx


def extract_imports(file_path):
    """
    Extract imports from a Python file.
    """

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            tree = ast.parse(f.read())

        imports = []

        for node in ast.walk(tree):

            if isinstance(
                node,
                ast.Import
            ):

                for name in node.names:

                    imports.append(
                        name.name.split(".")[0]
                    )

            elif isinstance(
                node,
                ast.ImportFrom
            ):

                if node.module:

                    imports.append(
                        node.module.split(".")[0]
                    )

        return list(set(imports))

    except Exception:

        return []
    
def build_dependency_graph(
    repo_path
):
    """
    Build dependency graph for
    all Python files.
    """

    graph = nx.DiGraph()

    python_files = {}

    for root, dirs, files in os.walk(
        repo_path
    ):

        for file in files:

            if file.endswith(".py"):

                module_name = (
                    file.replace(".py", "")
                )

                file_path = os.path.join(
                    root,
                    file
                )

                python_files[
                    module_name
                ] = file_path

                graph.add_node(file)

    for module_name, file_path in (
        python_files.items()
    ):

        imports = extract_imports(
            file_path
        )

        current_file = (
            os.path.basename(
                file_path
            )
        )

        for imported_module in imports:

            if (
                imported_module
                in python_files
            ):

                imported_file = (
                    os.path.basename(
                        python_files[
                            imported_module
                        ]
                    )
                )

                graph.add_edge(
                    current_file,
                    imported_file
                )

    return graph

def repository_dependencies(
    repo_path
):
    """
    Repository dependency stats.
    """

    graph = build_dependency_graph(
        repo_path
    )

    return {

        "nodes":
        graph.number_of_nodes(),

        "edges":
        graph.number_of_edges(),

        "files":
        list(graph.nodes()),

        "dependencies":
        [
            {
                "from": u,
                "to": v
            }
            for u, v in graph.edges()
        ]
    }

def impacted_files(
    repo_path,
    target_file
):
    """
    Find files impacted by
    changing a target file.
    """

    graph = build_dependency_graph(
        repo_path
    )

    impacted = []

    reverse_graph = graph.reverse()

    target = os.path.basename(
        target_file
    )

    if target not in reverse_graph:

        return {
            "error":
            "File not found in graph"
        }

    descendants = nx.descendants(
        reverse_graph,
        target
    )

    impacted.extend(
        descendants
    )

    return {

        "target":
        target,

        "impacted_files":
        sorted(
            list(impacted)
        ),

        "count":
        len(impacted)
    }

def dependency_chain(
    repo_path,
    source_file,
    destination_file
):
    """
    Find dependency path between
    two files.
    """

    graph = build_dependency_graph(
        repo_path
    )

    try:

        path = nx.shortest_path(
            graph,
            source=source_file,
            target=destination_file
        )

        return {

            "path":
            path,

            "length":
            len(path)
        }

    except Exception:

        return {
            "path": []
        }
    
def critical_files(
    repo_path,
    top_k=10
):
    """
    Find most connected files.
    """

    graph = build_dependency_graph(
        repo_path
    )

    scores = []

    for node in graph.nodes():

        score = (
            graph.in_degree(node)
            +
            graph.out_degree(node)
        )

        scores.append(
            {
                "file": node,
                "score": score
            }
        )

    scores.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scores[:top_k]