import { useEffect, useState } from "react";
import axios from "axios";

import ReactFlow, {
  Background,
  Controls,
  MiniMap,
} from "reactflow";

import "reactflow/dist/style.css";

import { getLayoutedElements } from "./layout";

function App() {
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);

  const [repoUrl, setRepoUrl] = useState(
    "https://github.com/pallets/flask"
  );

  const analyzeRepo = () => {
    axios
      .post(
        "https://YOUR-RENDER-URL.onrender.com/analyze",
        {
          repo_url: repoUrl,
        }
      )
      .then((res) => {
        const graph = res.data;

        const flowNodes = graph.nodes.map(
          (node) => ({
            id: node,
            data: {
              label: node,
            },
            position: {
              x: 0,
              y: 0,
            },
          })
        );

        const flowEdges = graph.edges.map(
          (edge, index) => ({
            id: `e${index}`,
            source: edge.source,
            target: edge.target,
            animated: true,
          })
        );

        const layouted =
          getLayoutedElements(
            flowNodes,
            flowEdges
          );

        setNodes(layouted.nodes);
        setEdges(layouted.edges);
      })
      .catch((err) => {
        console.error(
          "API ERROR:",
          err
        );
      });
  };

  useEffect(() => {
    analyzeRepo();
  }, []);

  return (
    <div
      style={{
        width: "100vw",
        height: "100vh",
      }}
    >
      <div
        style={{
          position: "absolute",
          top: 10,
          left: 10,
          zIndex: 1000,
          background: "white",
          padding: "10px",
          borderRadius: "8px",
          boxShadow:
            "0 2px 10px rgba(0,0,0,0.2)",
        }}
      >
        <input
          type="text"
          value={repoUrl}
          onChange={(e) =>
            setRepoUrl(e.target.value)
          }
          style={{
            width: "450px",
            padding: "8px",
            marginRight: "10px",
          }}
        />

        <button
          onClick={analyzeRepo}
          style={{
            padding: "8px 16px",
            cursor: "pointer",
          }}
        >
          Analyze
        </button>
      </div>

      <ReactFlow
        nodes={nodes}
        edges={edges}
        fitView
      >
        <MiniMap />
        <Controls />
        <Background />
      </ReactFlow>
    </div>
  );
}

export default App;