import time 
from nodes.base_node import BaseNode

class DelayNode(BaseNode):
    def run(self, input_data):
        seconds = self.config.get("seconds",1)
        print(f"Delaying for {seconds} seconds...")
        time.sleep(seconds)
        return input_data