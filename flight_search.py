import requests
import datetime
from flight_data import FlightData
from KEYS import TEQUILA_LOCATION_ENDPOINT, TEQUILA_HEADERS


fly_from = "YTO"
date_from = datetime.datetime.now().strftime('%d/%m/%Y')
date_to = (datetime.datetime.now() + datetime.timedelta(days=180)).strftime('%d/%m/%Y')


class FlightSearch:
    def __init__(self):
        pass

    def find_iata(self, destination):
        city_name = destination["city"]
        query = {
            "term": city_name
        }
        response = requests.get(url=f"{TEQUILA_LOCATION_ENDPOINT}locations/query",
                                params=query,
                                headers=TEQUILA_HEADERS)
        iata = response.json()["locations"][0]["code"]
        return iata

    def find_flights(self, destination):
        query = {
            "fly_from": fly_from,
            "fly_to": destination["iataCode"],
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "price_to": destination["lowestPrice"],
            "curr": "CAD",
            "max_stopovers": 0,
        }
        response = requests.get(url=f"{TEQUILA_LOCATION_ENDPOINT}v2/search",
                                params=query,
                                headers=TEQUILA_HEADERS)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No direct flights found for {destination['city']}!")
            try:
                query["max_stopovers"] = 1
                response = requests.get(url=f"{TEQUILA_LOCATION_ENDPOINT}v2/search",
                                        params=query,
                                        headers=TEQUILA_HEADERS)
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {destination['city']} (even with stopover)!")
                return None
            else:
                new_flights = FlightData(
                    price=data['price'],
                    origin_city=data['route'][0]['cityFrom'],
                    origin_airport=data['route'][0]['flyFrom'],
                    destination_city=data['route'][1]['cityTo'],
                    destination_airport=data['route'][1]['flyTo'],
                    out_date=data['route'][0]['local_departure'].split("T")[0],
                    return_date=data['route'][2]['local_departure'].split("T")[0],
                    airline=data['route'][0]['airline'],
                    stop_overs=1,
                    via_city=data['route'][0]['cityTo'])

                return new_flights
                # print(f"Flights found: {new_flight.destination_city} for {new_flight.price}")
        else:
            new_flights = FlightData(
                price=data['price'],
                origin_city=data['route'][0]['cityFrom'],
                origin_airport=data['route'][0]['flyFrom'],
                destination_city=data['route'][0]['cityTo'],
                destination_airport=data['route'][0]['flyTo'],
                out_date=data['route'][0]['local_departure'].split("T")[0],
                return_date=data['route'][1]['local_departure'].split("T")[0],
                airline=data['route'][0]['airline'])

            return new_flights
            # print(f"Flights found: {new_flight.destination_city} for {new_flight.price}")
