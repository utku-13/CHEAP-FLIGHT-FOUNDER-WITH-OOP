import os
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ.get("TEQAPI")
import requests
import datetime as dt

now = dt.datetime.now()

days_later_60 = now + dt.timedelta(days=60)

current_date = now.strftime("%d/%m/%Y")
date_of_60_days_later = days_later_60.strftime("%d/%m/%Y")

class FlightFounder:

    def search_flightt(self,origincity, cityname):
        location_endpoint = f"{TEQUILA_ENDPOINT}/search"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from":origincity,
            "fly_to":cityname,
            #it accepts multiple destination and it can give multiple output .
            "date_from":current_date,
            "date_to":date_of_60_days_later,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            #for cheapest flight.
            "max_stopovers": 0,
            #it indices direct flight.
            "curr": "EUR"
            #GBP is the code of sterlin . You can alter it with EUR if you would like.
        }

        response = requests.get(url=location_endpoint, headers=headers, params=query)
        data = response.json()["data"][0]["price"]
        return data
