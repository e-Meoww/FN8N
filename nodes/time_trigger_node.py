import datetime
import time
from nodes.base_node import BaseNode

class TimeTriggerNode(BaseNode):
    def run(self, input_data):
        target_time = self.config.get("time", "12:00")
        now_str = datetime.datetime.now().strftime("%H:%M")
        print(f"[TimeTrigger] Waiting for time: {target_time} (current: {now_str})")
        
        # while now_str == target_time:
        #     now_str = datetime.datetime.now().strftime("%H:%M")
        #     print("[TimeTrigger] Time matched. Triggering workflow...")
        while True:
            now_str = datetime.datetime.now().strftime("%H:%M")
            if now_str == target_time:
                print("[TimeTrigger] Time matched. Triggering workflow...")
                break
            time.sleep(5)
        return {}
    

