#!/usr/bin/env python3
import sys
import requests
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

try:
    from termgraph.termgraph import chart
    from termgraph.data import Data
    HAS_TERMGRAPH = True
except ImportError:
    HAS_TERMGRAPH = False

WMO_CODES = {
    0: "Clear sky",
    1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Icy fog",
    51: "Light drizzle", 53: "Drizzle", 55: "Heavy drizzle",
    61: "Light rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Light snow", 73: "Moderate snow", 75: "Heavy snow",
    77: "Snow grains",
    80: "Light showers", 81: "Showers", 82: "Heavy showers",
    85: "Light snow showers", 86: "Heavy snow showers",
    95: "Thunderstorm", 96: "Thunderstorm + hail", 99: "Thunderstorm + heavy hail",
}

def weather_desc(code):
    return WMO_CODES.get(code, "Unknown")

def geocode(city):
    try:
        r = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1},
            timeout=10,
        )
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"Network error: {e}")
        sys.exit(1)

    data = r.json()
    if not data.get("results"):
        print(f"City not found: '{city}'")
        sys.exit(1)

    res = data["results"][0]
    return res["latitude"], res["longitude"], res["name"], res.get("country", "")

def fetch_weather(lat, lon):
    try:
        r = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,relative_humidity_2m,windspeed_10m,weathercode",
                "daily": "temperature_2m_max,temperature_2m_min,weathercode,precipitation_probability_max",
                "timezone": "auto",
                "forecast_days": 7,
            },
            timeout=10,
        )
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"Network error: {e}")
        sys.exit(1)
    return r.json()

def fmt_date(date_str):
    d = datetime.strptime(date_str, "%Y-%m-%d")
    return d.strftime("%a %d %b")  # e.g. "Thu 19 Feb"

def print_graphs(daily):
    if not HAS_TERMGRAPH:
        print("  (Install termgraph for charts: pip install termgraph)\n")
        return

    labels = ["Today    "] + [fmt_date(daily["time"][i]) for i in range(1, 7)]
    temps = [[daily["temperature_2m_max"][i] or 0.0] for i in range(7)]
    rains = [[daily["precipitation_probability_max"][i] or 0] for i in range(7)]

    base_args = {
        "title": "",
        "width": 40,
        "format": "{:.1f}",
        "suffix": "",
        "no_labels": False,
        "no_values": False,
        "space_between": False,
        "color": None,
        "custom_tick": "",
        "vertical": False,
        "stacked": False,
        "histogram": False,
        "bins": 5,
        "different_scale": False,
        "percentage": False,
        "no_readable": False,
        "label_before": False,
    }

    print("\n  Max Temperature (°C)")
    chart(Data(temps, labels), {**base_args, "title": "Max Temp", "suffix": "°C"}, [])

    print("\n  Rain Probability (%)")
    chart(Data(rains, labels), {**base_args, "title": "Rain Prob", "format": "{:.0f}", "suffix": "%"}, [])


def main():
    if len(sys.argv) < 2:
        print("Usage: weather <city>")
        print("Example: weather chennai")
        sys.exit(1)

    city = " ".join(sys.argv[1:])

    print(f"\nFetching weather for '{city}'...")

    lat, lon, name, country = geocode(city)
    data = fetch_weather(lat, lon)

    cur = data["current"]
    daily = data["daily"]

    sep = "=" * 44
    print(f"\n{sep}")
    print(f"  {name}, {country}")
    print(sep)
    print(f"  Now          : {weather_desc(cur['weathercode'])}")
    print(f"  Temperature  : {cur['temperature_2m']}°C")
    print(f"  Humidity     : {cur['relative_humidity_2m']}%")
    print(f"  Wind         : {cur['windspeed_10m']} km/h")

    print(f"\n  7-Day Forecast")
    print(f"  {'-' * 40}")
    for i in range(7):
        label = "Today     " if i == 0 else fmt_date(daily["time"][i])
        tmax = daily["temperature_2m_max"][i]
        tmin = daily["temperature_2m_min"][i]
        rain = daily["precipitation_probability_max"][i]
        desc = weather_desc(daily["weathercode"][i])
        print(f"  {label}  {tmax:>4}° / {tmin:>3}°  Rain {rain:>3}%  {desc}")

    print(f"{sep}\n")
    print_graphs(daily)

if __name__ == "__main__":
    main()
