class BaseNode:
    def __init__(self, node_id, config):
        self.node_id = node_id
        self.config = config

    def run(self, input_data):
        raise NotImplementedError("Each node must implement the run() method")
