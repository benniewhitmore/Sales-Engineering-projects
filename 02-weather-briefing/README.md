# Sales Rep Weather Briefing Tool

A Python script that pulls live weather data for each rep's territory and prints a pre-call briefing — so reps can open every conversation with something relevant.

## What It Does

Reads a CSV file of sales reps and their assigned cities. For each rep, it calls the OpenWeatherMap API and returns the current temperature and conditions. Output is formatted as a quick-scan briefing before a call block.

## Sample Output

```
Marcus | Atlanta | 84.2F | clear sky
Jordan | Chicago | 61.5F | light rain
Taylor | Seattle | 55.1F | overcast clouds
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
3. Run: `python weather_briefing.py`

## Why I Built This

Small talk is a real part of enterprise sales. Knowing it's raining in Chicago before you call a buyer there takes 2 seconds and signals you're paying attention. This tool automates that context so reps can focus on the conversation, not the prep.
