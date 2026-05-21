import csv

with open("leads.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["name"]
        company = row["company"]
        deal_value = int(row["deal_value"])
        if deal_value > 50000:
            print(name + " | " + company + " | " + str(deal_value) + " | HIGH")
        elif deal_value < 20000:
            print(name + " | " + company + " | " + str(deal_value) + " | LOW")
        else:
            print(name + " | " + company + " | " + str(deal_value) + " | MEDIUM")
