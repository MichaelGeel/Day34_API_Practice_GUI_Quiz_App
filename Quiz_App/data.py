import requests as r


PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}

def get_data():
    response = r.get(url="https://opentdb.com/api.php", params=PARAMETERS)
    response.raise_for_status()
    data = response.json()['results']
    return data
