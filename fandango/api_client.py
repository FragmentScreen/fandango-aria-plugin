from .config import *
from .utils import set_headers, get_config

config = get_config()
class APIClient:
    def __init__(self,token):
        self.token = token
        self.base_url = config['apis']['DATA_DEPOSITION_BASE']

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        headers = set_headers(self.token)
        if params:
            query_string = self._construct_query_string(params)
            url += f"?{query_string}"
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        return resp.json()

    def post(self, endpoint : str, data : dict = None):
        url = f"{self.base_url}/{endpoint}"
        headers = set_headers(self.token)
        resp = requests.post(url, json=data, headers=headers)
        resp.raise_for_status()
        return resp.json()

    def _construct_query_string(self, params):
        query_string = "&".join([f"filter[{key}]={value}" for key, value in params.items()])
        return query_string