from nodes.base_node import BaseNode

class TransformNode(BaseNode):
    def run(self, input_data):
        title = input_data.get("title", "")
        return {"title_upper": title.upper()}
