import requests
import os
import json

api_endpoint = "http://" + os.getenv("API_ENDPOINT") + ":8000/"

if api_endpoint == None:
    api_endpoint = "http://localhost:8000"

def request(params = {}, path = '') -> list[dict]:
    """
    Send request to api (only support get method for now).

    Parameters:
    - params: Dictionary of parameters for query.
    - path: Path of api host.

    Returns:
    list of Sale Report.
    """
    response = requests.get(api_endpoint + path, params=params).text
    return json.loads(response)