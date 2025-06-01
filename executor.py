import json
from nodes.http_node import HttpRequestNode

NODE_TYPE_MAP = {
    "HttpRequest": HttpRequestNode,
}

def load_workflow(path):
    with open(path, "r") as file:
        return json.load(file)

def execute_node(node, input_data):
    node_type = node["type"]
    node_class = NODE_TYPE_MAP.get(node_type)
    if not node_class:
        raise Exception(f"Unknown node type: {node_type}")
    instance = node_class(node["id"], node["config"])
    return instance.run(input_data)

def run_workflow(workflow_path):
    workflow = load_workflow(workflow_path)
    data = None

    for node in workflow["nodes"]:
        data = execute_node(node, data)
        print(f"Node {node['id']} output:", data)

if __name__ == "__main__":
    run_workflow("workflows/sample_workflow.json")
