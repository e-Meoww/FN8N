import json
from nodes.http_node import HttpRequestNode
from nodes.transform_node import TransformNode
from nodes.delay_node import DelayNode
from nodes.time_trigger_node import TimeTriggerNode
from nodes.webhook_trigger_node import WebhookTriggerNode
NODE_TYPE_MAP = {
    "HttpRequest": HttpRequestNode,
    "Transform": TransformNode,
    "Delay" : DelayNode,
    "TimeTrigger": TimeTriggerNode,
    "WebhookTrigger": WebhookTriggerNode,
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
    nodes = workflow["nodes"]
    
    # Map node ID to node data
    node_map = {node["id"]: node for node in nodes}
    executed = {}
    
    def execute_node_recursive(node_id, input_data):
        node = node_map[node_id]
        node_type = node["type"]
        node_class = NODE_TYPE_MAP.get(node_type)
        if not node_class:
            raise Exception(f"Unknown node type: {node_type}")
        
        instance = node_class(node_id, node["config"])
        output = instance.run(input_data)
        executed[node_id] = output
        print(f"Node {node_id} output:", output)

        for next_id in node.get("next", []):
            execute_node_recursive(next_id, output)

    # Start with node having no incoming connections (root)
    start_node = nodes[0]  # Assumes first node is start
    execute_node_recursive(start_node["id"], None)



if __name__ == "__main__":
    run_workflow("workflows/sample_workflow.json")
