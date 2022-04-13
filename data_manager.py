import requests
from KEYS import SHEETY_PRICES_ENDPOINT


class DataManager:
    def __init__(self):
        self.data = []
        self.get_data()

    def get_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        self.data = response.json()["prices"]
        # print(self.data)

    def put_data(self):
        for city in self.data:
            update = {
                "price": city
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=update)
            # print(response.text)