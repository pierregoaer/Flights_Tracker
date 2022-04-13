import requests
from twilio.rest import Client
import smtplib
from KEYS import SHEETY_USERS_ENDPOINT, twilio_account_sid, twilio_auth_token, from_number, to_number, google_email, google_password


client = Client(twilio_account_sid, twilio_auth_token)


class NotificationManager:
    def __init__(self):
        self.recipients = []
        self.get_email_recipients()

    def get_email_recipients(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        self.recipients = response.json()["users"]
        print(self.recipients)

    def send_text(self, flight):
        layover = ""
        if flight.stop_overs == 1:
            layover = f"The flight has 1 stopover in {flight.via_city}"
        msg = f"Pack your things, new flights alert! " \
              f"Only ${flight.price} to fly from {flight.origin_city} ({flight.origin_airport}) " \
              f"to {flight.destination_city} ({flight.destination_airport}), " \
              f"from {flight.out_date} to {flight.return_date}, with {flight.airline}!\n" \
              f"{layover}"

        print(msg)

        message = client.messages \
            .create(
                body=msg,
                from_=from_number,
                to=to_number
            )
        print(message.status)

    def send_emails(self, flight):
        for recipient in self.recipients:
            layover = ""
            if flight.stop_overs == 1:
                layover = f"The flight has 1 stopover in {flight.via_city}"

            recipient_first_name = recipient["firstName"]
            recipient_email = recipient["email"]
            msg = f"Hello {recipient_first_name},\n\n" \
                  f"It's time to pack your things, new flights alert! " \
                  f"Only ${flight.price} to fly from {flight.origin_city} ({flight.origin_airport}) " \
                  f"to {flight.destination_city} ({flight.destination_airport}), " \
                  f"from {flight.out_date} to {flight.return_date}, with {flight.airline}!\n" \
                  f"{layover}"

            with smtplib.SMTP("smtp.gmail.com") as connexion:
                # enable secure connexion
                connexion.starttls()
                connexion.login(user=google_email, password=google_password)
                connexion.sendmail(from_addr=google_email, to_addrs=recipient_email,
                                   msg=f"Subject: Pack you bags {recipient_first_name} ✈️\n\n{msg}")