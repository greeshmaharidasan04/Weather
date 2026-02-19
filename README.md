# Weather CLI

A simple command-line weather app built with Python. Shows current weather and a 7-day forecast for any city.

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
```

## Setup

**1. Install dependency:**
```
pip install requests
```

**2. Add the project folder to your Windows PATH** so you can run `weather` from anywhere:
- Open Environment Variables (Win + R → `sysdm.cpl`)
- Edit `Path` under User variables
- Add the folder path (e.g. `C:\Users\yourname\documents\code`)
- Reopen PowerShell

## API

Uses [Open-Meteo](https://open-meteo.com/) — free, no API key required.
