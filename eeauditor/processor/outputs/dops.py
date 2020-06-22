import json
import os
import requests
from processor.outputs.output_base import ElectricEyeOutput

client_id = os.environ.get("DOPS_CLIENT_ID", None)
api_key = os.environ.get("DOPS_API_KEY", None)


@ElectricEyeOutput
class DopsProvider(object):
    __provider__ = "dops"

    def __init__(self):
        self.url = "https://collector.dev2.disruptops.com/event"

    def write_findings(self, findings: list, **kwargs):
        if client_id and api_key:
            for finding in findings:
                response = requests.post(
                    self.url, data=json.dumps(finding), auth=(client_id, api_key)
                )
        else:
            raise ValueError("Missing credentials for client_id or api_key")
