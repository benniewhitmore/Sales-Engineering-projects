import csv
import os
from twilio.rest import Client

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TO_NUMBER = os.environ.get("TWILIO_TO_NUMBER")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

with open("inventory.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        quantity = int(row["quantity"])
        threshold = int(row["threshold"])

        if quantity < threshold:
            message = client.messages.create(
                body="LOW STOCK: " + product + " — only " + str(quantity) + " left",
                from_="whatsapp:+14155238886",
                to=TO_NUMBER
            )
            print("Alert sent for " + product)
        else:
            print(product + " — OK")
