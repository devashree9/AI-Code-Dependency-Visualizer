import os
import networkx as nx

from parser import get_imports


def build_graph(repo_path):

    graph = nx.DiGraph()

    python_files = {}

    # First pass: collect all Python files
    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if (
                    file.endswith(".py")
                    and not file.startswith("test_")
                    and file != "conftest.py"
                ):
                module_name = file.replace(".py", "")

                python_files[module_name] = file

    # Second pass: build graph
    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if (
                    file.endswith(".py")
                    and not file.startswith("test_")
                    and file != "conftest.py"
                ):

                filepath = os.path.join(root, file)

                imports = get_imports(filepath)

                graph.add_node(file)

                for imp in imports:

                    module = imp.split(".")[0]

                    if module in python_files:

                        target_file = python_files[module]

                        # Prevent self-loops
                        if target_file != file:

                            graph.add_edge(
                                file,
                                target_file
                            )

    return graph


def graph_to_json(graph):

    return {
        "nodes": list(graph.nodes()),
        "edges": [
            {
                "source": source,
                "target": target
            }
            for source, target in graph.edges()
        ]
    }