from flask import Flask , request
import threading 
from nodes.base_node import BaseNode

class WebhookTriggerNode(BaseNode):
    def __init__(self, node_id, config):
        super().__init__(node_id, config)
        self.input_data = None
        self.app = Flask(__name__)
        self.event = threading.Event()

        @self.app.route('/webhook', methods =['POST', 'GET'])
        def webhook():
            self.input_data = request.json if request.is_json else request.args.to_dict()
            print(f"[Webhooktrigger] Data Recived: {self.input_data}")
            self.event.set() 
            return {"status": "triggered"}
        

    def run(self, input_data):
        port = self.config.get("port", 5000)
        print(f"[WebhookTrigger] Waiting on http://localhost:{port}/webhook")

        threading.Thread(target=self.app.run, kwargs = {"port": port, "use_reloader": False}).start()

        self.event.wait()
        return self.input_data or {}
    