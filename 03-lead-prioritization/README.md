# Lead Prioritization Tool

A Python script that reads a pipeline of leads from a CSV file and automatically categorizes each one as HIGH, MEDIUM, or LOW priority based on deal value.

## What It Does

Reads a CSV with rep names, company names, and deal values. Applies threshold logic to categorize each lead — giving reps an instant view of where to focus their time.

## Sample Output

```
Sarah | Nike | 75000 | HIGH
Marcus | Foot Locker | 34000 | MEDIUM
Jordan | Local Retailer | 12000 | LOW
```

## Logic

| Deal Value | Priority |
|------------|----------|
| > $50,000 | HIGH |
| $20,000 – $50,000 | MEDIUM |
| < $20,000 | LOW |

## Tech Stack

- Python 3
- CSV module

## Setup

1. Run: `python lead_prioritization.py`

## Why I Built This

Pipeline prioritization is one of the most time-consuming parts of sales management. This script replicates the logic a sales manager applies manually every Monday morning — and runs it instantly across any size pipeline.
