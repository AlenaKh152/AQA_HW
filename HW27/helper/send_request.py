import requests


def send_request(method, url, headers=None, params=None, data=None, json=None):
    response = requests.request(method, url, headers=headers, params=params, data=data, json=json)
    assert response.status_code == 200, f"Statuse code is not 200, response: {response.text}"
    return response.json()
