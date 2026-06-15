from clone_repo import clone_repository

from graph_builder import (
    build_graph,
    graph_to_json
)

repo_path = clone_repository(
    "https://github.com/pallets/flask"
)

graph = build_graph(repo_path)

data = graph_to_json(graph)

print(
    "Total Nodes:",
    len(data["nodes"])
)

print(
    "Total Edges:",
    len(data["edges"])
)

print("\nFirst 10 Edges:\n")

for edge in data["edges"][:10]:
    print(edge)

print(data["nodes"][:10])

print("\n")

for edge in data["edges"][:20]:
    print(edge)