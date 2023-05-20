import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/944d0463694aebefe839b2a1e3681b21/flightPrices/sayfa1"

class DataManage:
    def get_info(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()["sayfa1"]
        return data
    