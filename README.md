# Weather CLI

A simple command-line weather app built with Python. Shows current weather, a 7-day forecast, and ASCII bar charts for temperature and rain probability.

## Usage

```
weather <city>
```

**Examples:**
```
weather chennai
weather new york
weather london
```

## Sample Output

```
============================================
  Chennai, India
============================================
  Now          : Partly cloudy
  Temperature  : 31°C
  Humidity     : 72%
  Wind         : 12.0 km/h

  7-Day Forecast
  ----------------------------------------
  Today       31° /  26°  Rain   0%  Partly cloudy
  Fri 20 Feb  30° /  25°  Rain  10%  Mainly clear
  Sat 21 Feb  31° /  26°  Rain   5%  Clear sky
  ...
============================================

  Max Temperature (°C)

# Max Temp

Today     : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 31.4°C
Mon 23 Feb: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 32.0°C
Tue 24 Feb: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 31.9°C
Wed 25 Feb: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 31.5°C
Thu 26 Feb: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 32.8°C
Fri 27 Feb: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 33.1°C
Sat 28 Feb: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 32.1°C

  Rain Probability (%)

# Rain Prob

Today     : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 15%
Mon 23 Feb: ▇▇▇▇▇▇▇▇ 3%
Tue 24 Feb:  0%
Wed 25 Feb: ▇▇▇▇▇▇▇▇▇▇▇▇▇ 5%
Thu 26 Feb:  0%
Fri 27 Feb:  0%
Sat 28 Feb:  0%
```

## Setup

**1. Install dependencies:**
```
pip install requests termgraph
```

**2. Add the project folder to your Windows PATH** so you can run `weather` from anywhere:
- Open Environment Variables (Win + R → `sysdm.cpl`)
- Edit `Path` under User variables
- Add the folder path (e.g. `C:\Users\yourname\documents\code`)
- Reopen PowerShell

## API

Uses [Open-Meteo](https://open-meteo.com/) — free, no API key required.
