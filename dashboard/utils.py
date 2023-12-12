import requests
import os
import json

# api_endpoint = "http://localhost:8000/"
api_endpoint = os.getenv("API_ENDPOINT")

def request(params = {}, path = '') -> list[dict]:
    """
    Send request to api (only support get method for now).

    Parameters:
    - params: Dictionary of parameters for query.
    - path: Path of api host.

    Returns:
    list of Sale Report.
    """
    return json.loads(requests.get(api_endpoint + path, params=params).text)