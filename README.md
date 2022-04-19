# Flights Tracker ✈️

This is a simple app that scans the internet to find flights to a list of destinations that you have selected. Enter your destinations in a Google Sheet, enter a maximum amount you would like to pay for each destination and get notified when something matches your query.

`main.py` is the python file to run.

## 👨🏼‍🎓 Learnings:
1. I got to discover new APIs that I had never used before, including Twilio which can be extremely powerful
2. This project was a great opportunity to not only use different APIs but also combine them all together (the list of APIs is detailed below)
3. I learned how to handle situations where no flights can be found and what to do in that case 

## 🚀 Tech and tools:

This app was built using python and 4 different APIs:
- **Sheety**: Sheety is an API that lets you access and edit Google Sheets. In this case, the destinations, max prices and IATA codes are written on a Google Sheet.
- **Tequila by Kiwi**: this is an API that is similar to Kayak (which might be the post popular tool to find deals on flights). Tequila allows to pass a large list of arguments in our request such as:
  - Trip duration
  - Trip dates
  - Max price
  - Flights durations and layover
  - Number of passengers and checked bags
  - And many more parameter to customize the search
- **Twilio**: Twilio is a communications API for SMS, voice, video and more. In this case, we're using the SMS feature to text users when a flight has been found and the flitghts details
- **Gmail**: Just like Twilio, we're using GMail to also alert users via Email. This is a handy feature in case a user would prefer email notifications rather than text. It is important to note that this is not a secure user sign in using Google. It requires the Gmail account to allow unsecured apps to work.

## 🔜 Things I would improve:
- Get away from Sheety and use a database instead to store users' destinations and desired prices
- Make it a web app so users can log and change their preferences themselves

## ⚙️ How does it work:
1. Using Sheety, create a list of destinations from the Google Sheet
2. Using Tequila, find the IATA code for every destination where the code is missing in Google Sheet
3. Still using Tequila, find all the flights that match the price for each destination, if no flights match the request, an empty list is returned
4. If flights are found, notify the user via text message and email of the flights, with the important details (destination, price, dates)
![](assets/flight_sms__alert_iphone_mockup.png)
