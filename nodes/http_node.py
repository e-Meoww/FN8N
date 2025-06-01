import requests
from nodes.base_node import BaseNode

class HttpRequestNode(BaseNode):
    def run(self, input_data):
        method = self.config.get("method", "GET")
        url = self.config.get("url")
        params = self.config.get("params", {})
        data = self.config.get("data", {})

        response = requests.request(method, url, params=params, json=data)
        return response.json()