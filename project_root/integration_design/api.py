```python
import requests
from requests.exceptions import HTTPError

class TrelloAPI:
    def __init__(self, api_key, token):
        self.api_key = api_key
        self.token = token
        self.base_url = "https://api.trello.com/1/"

    def get_board(self, board_id):
        url = f"{self.base_url}boards/{board_id}"
        query = {
            'key': self.api_key,
            'token': self.token
        }
        try:
            response = requests.request("GET", url, params=query)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()

    def get_list(self, list_id):
        url = f"{self.base_url}lists/{list_id}"
        query = {
            'key': self.api_key,
            'token': self.token
        }
        try:
            response = requests.request("GET", url, params=query)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()

    def create_card(self, idList, name, desc=None):
        url = f"{self.base_url}cards"
        query = {
            'key': self.api_key,
            'token': self.token,
            'idList': idList,
            'name': name,
            'desc': desc
        }
        try:
            response = requests.request("POST", url, params=query)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()
```