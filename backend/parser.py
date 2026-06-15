import ast


def get_imports(filepath):

    imports = []

    try:

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            tree = ast.parse(
                file.read()
            )

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

    except Exception as e:

        print(
            f"Error parsing {filepath}: {e}"
        )

    return imports