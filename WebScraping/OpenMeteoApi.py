import requests
import pandas as pd

# Lista miast z ich współrzędnymi (latitude, longitude)
cities = {
    #"Warsaw": (52.23, 21.01),
    #"Berlin": (52.52, 13.41),
    #"Prague": (50.088, 14.4208),
    #"Vilnius": (54.6892, 25.2798),
    "Minsk": (53.9, 27.5667),
    "Kyiv": (50.4547, 30.5238)
}

# Zakres dat (20 lat)
start_date = "2004-01-01"
end_date = "2023-12-31"

# Parametry dzienne do pobrania
daily_params = [
    "temperature_2m_max",
    "temperature_2m_min",
    "precipitation_sum",
    "rain_sum",
    "snowfall_sum",
    "windspeed_10m_max",
    "sunshine_duration"
]

def fetch_city_data(city_name, lat, lon):
    print(f"Pobieram dane dla: {city_name}")
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "daily": ",".join(daily_params),
        "timezone": "auto"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "daily" not in data:
        print(f"Brak danych dla: {city_name}")
        return

    df = pd.DataFrame(data["daily"])
    df["city"] = city_name
    df.to_csv(f"{city_name}_weather_2004_2023.csv", index=False)
    print(f"Dane zapisane: {city_name}_weather_2004_2023.csv")

# Pobierz dane dla wszystkich miast
for city, (lat, lon) in cities.items():
    fetch_city_data(city, lat, lon)
