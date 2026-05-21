# Inventory Alert System

A Python script that monitors stock levels and sends automated WhatsApp alerts when inventory drops below defined thresholds.

## What It Does

Reads a CSV file containing product names, current quantities, and threshold levels. For each product, it checks whether stock has dropped below the threshold — if so, it fires a WhatsApp message via Twilio's messaging API alerting the sales rep in real time.

## Sample Output

```
Air Jordan 1 — OK
Nike Dri-FIT — OK
Foot Locker Tee — Alert sent
Adidas Ultraboost — Alert sent
```

WhatsApp message received:
```
LOW STOCK: Foot Locker Tee — only 8 left
LOW STOCK: Adidas Ultraboost — only 15 left
```

## Tech Stack

- Python 3
- Twilio Messaging API (WhatsApp)
- CSV module

## Setup

1. Install dependencies: `pip install twilio`
2. Set environment variables:
```bash
export TWILIO_ACCOUNT_SID=your_sid
export TWILIO_AUTH_TOKEN=your_token
export TWILIO_TO_NUMBER=whatsapp:+1XXXXXXXXXX
```
3. Run: `python inventory_alert.py`

## Why I Built This

In my previous role managing 20+ professional sports and arena retail accounts, inventory visibility was a constant pain point. Reps would spend time chasing stock updates over email and phone. This script automates that entirely — the alert comes to you when it matters, without anyone having to ask.
