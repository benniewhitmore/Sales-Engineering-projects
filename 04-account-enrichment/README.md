# Account Enrichment Tool

A Python script that combines CRM pipeline data with live weather API data to produce an enriched account briefing — deal value, priority tier, and current conditions in the account's city.

## What It Does

Reads a CSV of accounts with company name, city, and deal value. For each account, it calls the OpenWeatherMap API to pull live conditions, then applies deal prioritization logic. The result is a single enriched output row per account.

## Sample Output

```
Nike | Portland | 68.3F | clear sky | $75000 | HIGH
Foot Locker | New York | 72.1F | partly cloudy | $34000 | MEDIUM
Arena Sports | Dallas | 91.4F | sunny | $12000 | LOW
```

## Tech Stack

- Python 3
- OpenWeatherMap REST API
- requests library
- CSV module

## Setup

1. Install dependencies: `pip install requests`
2. Set environment variable:
```bash
export OPENWEATHER_API_KEY=your_api_key
```
3. Run: `python account_enrichment.py`

## Why I Built This

This combines two real problems I saw in enterprise sales: reps don't have context before calls, and pipeline data lives in a spreadsheet disconnected from everything else. This script pulls both together into one view — the kind of tool an SE would build during a POC to show a prospect what's possible with their data and an API integration.
