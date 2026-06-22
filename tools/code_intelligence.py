import ast
import os


def find_classes(file_path):
    """
    Find all class definitions in a Python file.
    """

    try:
        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            tree = ast.parse(f.read())

        classes = []

        for node in ast.walk(tree):

            if isinstance(
                node,
                ast.ClassDef
            ):
                classes.append(
                    node.name
                )

        return classes

    except Exception as e:

        return {
            "error": str(e)
        }


def find_functions(file_path):
    """
    Find all function definitions in a Python file.
    """

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            tree = ast.parse(f.read())

        functions = []

        for node in ast.walk(tree):

            if isinstance(
                node,
                ast.FunctionDef
            ):

                functions.append(
                    node.name
                )

        return functions

    except Exception as e:

        return {
            "error": str(e)
        }


def find_imports(file_path):
    """
    Find all imports used in a Python file.
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
                        name.name
                    )

            elif isinstance(
                node,
                ast.ImportFrom
            ):

                if node.module:

                    imports.append(
                        node.module
                    )

        return list(
            set(imports)
        )

    except Exception as e:

        return {
            "error": str(e)
        }


def find_api_routes(file_path):
    """
    Detect FastAPI routes.
    """

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            tree = ast.parse(f.read())

        routes = []

        for node in ast.walk(tree):

            if isinstance(
                node,
                ast.FunctionDef
            ):

                for decorator in node.decorator_list:

                    if not isinstance(
                        decorator,
                        ast.Call
                    ):
                        continue

                    if not isinstance(
                        decorator.func,
                        ast.Attribute
                    ):
                        continue

                    method = (
                        decorator.func.attr
                    )

                    if method not in [
                        "get",
                        "post",
                        "put",
                        "delete",
                        "patch"
                    ]:
                        continue

                    route_path = ""

                    if (
                        decorator.args
                        and isinstance(
                            decorator.args[0],
                            ast.Constant
                        )
                    ):

                        route_path = (
                            decorator.args[0].value
                        )

                    routes.append(
                        {
                            "method":
                            method.upper(),

                            "path":
                            route_path,

                            "function":
                            node.name
                        }
                    )

        return routes

    except Exception as e:

        return {
            "error": str(e)
        }


def generate_file_intelligence(
    file_path
):
    """
    Generate complete intelligence
    about a Python file.
    """

    return {

        "file":
        os.path.basename(
            file_path
        ),

        "classes":
        find_classes(
            file_path
        ),

        "functions":
        find_functions(
            file_path
        ),

        "imports":
        find_imports(
            file_path
        ),

        "routes":
        find_api_routes(
            file_path
        )
    }


def analyze_repository(
    repo_path
):
    """
    Analyze every Python file
    inside a repository.
    """

    repo_report = []

    for root, dirs, files in os.walk(
        repo_path
    ):

        for file in files:

            if not file.endswith(
                ".py"
            ):
                continue

            file_path = os.path.join(
                root,
                file
            )

            repo_report.append(
                generate_file_intelligence(
                    file_path
                )
            )

    return repo_report

# refining retrival , now chunking module , classes and fucnstion wise 

def extract_functions(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as f:

        source_code = f.read()

    tree = ast.parse(source_code)

    functions = []

    for node in ast.walk(tree):

        if isinstance(
            node,
            ast.FunctionDef
        ):

            functions.append(
                {
                    "name": node.name,
                    "line": node.lineno
                }
            )

    return functions


def extract_classes(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as f:

        source_code = f.read()

    tree = ast.parse(source_code)

    classes = []

    for node in ast.walk(tree):

        if isinstance(
            node,
            ast.ClassDef
        ):

            classes.append(
                {
                    "name": node.name,
                    "line": node.lineno
                }
            )

    return classes



def extract_function_chunks(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as f:
        source = f.read()

    tree = ast.parse(source)

    chunks = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            start = node.lineno - 1
            end = node.end_lineno

            function_code = "\n".join(
                source.splitlines()[start:end]
            )

            chunks.append(
                {
                    "file": file_path,
                    "type": "function",
                    "name": node.name,
                    "text": function_code
                }
            )

    
    return chunks