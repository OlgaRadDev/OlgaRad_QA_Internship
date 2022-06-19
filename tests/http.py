import requests

class HttpClient(object):

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def get(self, path):
        res = requests.get(f"{self.base_url}{path}")
        result = res.json()
        print(result)
        return res

    def post(self, path, data):
        res = requests.post(f"{self.base_url}{path}", json=data, headers= self.headers)
        print(res.json())
        return res


