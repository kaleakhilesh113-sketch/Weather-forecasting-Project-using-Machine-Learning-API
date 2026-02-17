from meteostat import Stations, Daily
from datetime import datetime
import pandas as pd
from tqdm import tqdm

print("Fetching Indian stations...")
stations = Stations().region("IN").fetch()

start = datetime(2021, 1, 1)
end   = datetime(2025, 12, 31)

all_data = []

for station in tqdm(stations.index[:50]):  # limit for laptop safety
    try:
        data = Daily(station, start, end).fetch()
        data = data.reset_index()   # 🔴 VERY IMPORTANT
        data["station"] = station
        all_data.append(data)
    except:
        pass

df = pd.concat(all_data, ignore_index=True)
df.to_csv("india_weather.csv", index=False)

print("✅ Dataset created: india_weather.csv")
