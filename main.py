from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.data

for destination in sheet_data:
    # get iata code of destination city
    if destination["iataCode"] == "":
        destination["iataCode"] = flight_search.find_iata(destination)

    # search for new flights
    new_flights = flight_search.find_flights(destination)

    # notify when flights found
    if new_flights is not None:
        notification_manager.send_text(new_flights)
        notification_manager.send_emails(new_flights)
