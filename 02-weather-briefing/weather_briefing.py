import csv
import os
import requests

API_KEY = os.environ.get("OPENWEATHER_API_KEY")

with open("cities.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        city = row["city"]
        rep = row["rep"]
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=" + city +
            "&appid=" + API_KEY + "&units=imperial"
        )
        data = response.json()
        temp = data["main"]["temp"]
        conditions = data["weather"][0]["description"]
        print(rep + " | " + city + " | " + str(temp) + "F | " + conditions)
