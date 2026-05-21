import csv
import os
import requests

API_KEY = os.environ.get("OPENWEATHER_API_KEY")

with open("accounts.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        company = row["company"]
        city = row["city"]
        deal_value = int(row["deal_value"])
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=" + city +
            "&appid=" + API_KEY + "&units=imperial"
        )
        data = response.json()
        temp = data["main"]["temp"]
        conditions = data["weather"][0]["description"]
        if deal_value > 50000:
            priority = "HIGH"
        elif deal_value < 20000:
            priority = "LOW"
        else:
            priority = "MEDIUM"
        print(company + " | " + city + " | " + str(temp) + "F | " + conditions + " | $" + str(deal_value) + " | " + priority)
