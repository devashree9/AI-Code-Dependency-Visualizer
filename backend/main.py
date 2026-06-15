from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from clone_repo import clone_repository
from graph_builder import build_graph, graph_to_json
from pydantic import BaseModel
class RepoRequest(BaseModel):
    repo_url: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.post("/analyze")
def analyze(request: RepoRequest):

    print("\n")
    print("Repository:", request.repo_url)

    repo_path = clone_repository(
        request.repo_url
    )

    graph = build_graph(repo_path)

    print(
        f"Nodes: {len(graph.nodes())}"
    )

    print(
        f"Edges: {len(graph.edges())}"
    )

    return graph_to_json(graph)