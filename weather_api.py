# import requests
# from datetime import datetime

# # ---------- REGION INTENT MAP (GOOGLE-LIKE LOGIC) ----------
# REGION_ALIASES = {
#     "kashmir": {
#         "city": "Srinagar",
#         "state": "Jammu and Kashmir",
#         "country": "India",
#         "lat": 34.0837,
#         "lon": 74.7973
#     },
#     "jammu and kashmir": {
#         "city": "Srinagar",
#         "state": "Jammu and Kashmir",
#         "country": "India",
#         "lat": 34.0837,
#         "lon": 74.7973
#     }
# }

# # ---------- LOCATION RESOLUTION ----------
# def get_coordinates(place):
#     place_clean = place.strip().lower()

#     # ✅ GOOGLE-STYLE REGION HANDLING
#     if place_clean in REGION_ALIASES:
#         return REGION_ALIASES[place_clean]

#     # ✅ CITY LOOKUP (INDIA ONLY)
#     url = (
#         "https://geocoding-api.open-meteo.com/v1/search"
#         f"?name={place}&count=5&country=IN"
#     )
#     data = requests.get(url).json()

#     if "results" not in data or len(data["results"]) == 0:
#         raise ValueError("Location not found")

#     # Pick best city by population
#     best = sorted(
#         data["results"],
#         key=lambda x: x.get("population", 0),
#         reverse=True
#     )[0]

#     return {
#         "lat": best["latitude"],
#         "lon": best["longitude"],
#         "city": best.get("name", ""),
#         "state": best.get("admin1", ""),
#         "country": best.get("country", "")
#     }

# # ---------- WEATHER DATA ----------
# def get_live_weather(lat, lon):
#     url = (
#         f"https://api.open-meteo.com/v1/forecast"
#         f"?latitude={lat}&longitude={lon}"
#         f"&current_weather=true"
#         f"&hourly=relativehumidity_2m,pressure_msl,"
#         f"precipitation,apparent_temperature"
#         f"&daily=temperature_2m_max,temperature_2m_min,"
#         f"apparent_temperature_max"
#         f"&timezone=auto"
#     )

#     data = requests.get(url).json()

#     now = datetime.now().strftime("%Y-%m-%dT%H:00")
#     idx = data["hourly"]["time"].index(now)

#     current = {
#         "temperature": data["current_weather"]["temperature"],
#         "feels_like": data["hourly"]["apparent_temperature"][idx],
#         "windspeed": data["current_weather"]["windspeed"],
#         "humidity": data["hourly"]["relativehumidity_2m"][idx],
#         "pressure": data["hourly"]["pressure_msl"][idx],
#         "rain": data["hourly"]["precipitation"][idx]
#     }

#     forecast_5day = []
#     for i in range(5):
#         forecast_5day.append({
#             "date": data["daily"]["time"][i],
#             "max": data["daily"]["temperature_2m_max"][i],
#             "min": data["daily"]["temperature_2m_min"][i],
#             "feels_like": data["daily"]["apparent_temperature_max"][i]
#         })

#     return current, forecast_5day


import requests
from datetime import datetime

REGION_ALIASES = {
    "kashmir": {
        "city": "Srinagar",
        "state": "Jammu and Kashmir",
        "country": "India",
        "lat": 34.0837,
        "lon": 74.7973
    }
}

def get_coordinates(place):
    key = place.strip().lower()
    if key in REGION_ALIASES:
        return REGION_ALIASES[key]

    url = (
        "https://geocoding-api.open-meteo.com/v1/search"
        f"?name={place}&count=5&country=IN"
    )
    data = requests.get(url).json()

    if "results" not in data:
        raise ValueError("Location not found")

    best = sorted(
        data["results"],
        key=lambda x: x.get("population", 0),
        reverse=True
    )[0]

    return {
        "lat": best["latitude"],
        "lon": best["longitude"],
        "city": best["name"],
        "state": best.get("admin1", ""),
        "country": best["country"]
    }

def get_live_weather(lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current_weather=true"
        f"&hourly=relativehumidity_2m,pressure_msl,"
        f"precipitation,apparent_temperature"
        f"&daily=temperature_2m_max,temperature_2m_min"
        f"&timezone=auto"
    )

    data = requests.get(url).json()

    now = datetime.now().strftime("%Y-%m-%dT%H:00")
    idx = data["hourly"]["time"].index(now)

    current = {
        "temp": data["current_weather"]["temperature"],
        "wind": data["current_weather"]["windspeed"],
        "humidity": data["hourly"]["relativehumidity_2m"][idx],
        "pressure": data["hourly"]["pressure_msl"][idx],
        "rain": data["hourly"]["precipitation"][idx]
    }

    forecast = []
    for i in range(5):
        forecast.append({
            "date": data["daily"]["time"][i],
            "max": data["daily"]["temperature_2m_max"][i],
            "min": data["daily"]["temperature_2m_min"][i]
        })

    return current, forecast
