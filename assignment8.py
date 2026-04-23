import random
import math
import numpy as np
import pandas as pd

zones_data = []

user_choice = input("Select input mode (1: Manual, 2: Random): ")
num_zones = int(input("How many zones? "))

for i in range(1, num_zones + 1):
    if user_choice == "1":
        print(f"\nZone {i}")
        traffic_level = int(input("Enter traffic (0-100): "))
        air_level = int(input("Enter air quality (0-300): "))
        energy_level = int(input("Enter energy usage (0-500): "))
    else:
        traffic_level = random.randint(0, 100)
        air_level = random.randint(0, 300)
        energy_level = random.randint(0, 500)

    zones_data.append({
        "zone": i,
        "traffic": traffic_level,
        "air": air_level,
        "energy": energy_level
    })

def get_zone_status(zone):
    if zone["air"] > 200 or zone["traffic"] > 80:
        return "High Risk"
    elif zone["energy"] > 400:
        return "Energy Critical"
    elif zone["traffic"] < 30 and zone["air"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"

def compute_risk(zone):
    return zone["traffic"] * 0.5 + zone["air"] * 0.3 + zone["energy"] * 0.2

def sort_zones(zones):
    for i in range(len(zones)):
        for j in range(len(zones) - 1):
            if zones[j]["risk"] < zones[j + 1]["risk"]:
                zones[j], zones[j + 1] = zones[j + 1], zones[j]
    return zones

def overall_status(avg_score):
    if avg_score < 80:
        return "City Stable"
    elif avg_score < 120:
        return "Moderate Risk"
    elif avg_score < 180:
        return "High Alert"
    else:
        return "Critical Emergency"

for z in zones_data:
    z["status"] = get_zone_status(z)
    z["risk"] = compute_risk(z)
    z["sqrt_risk"] = math.sqrt(z["risk"])

roll_number = 7

if roll_number % 3 == 0:
    random.shuffle(zones_data)
else:
    zones_data = sort_zones(zones_data)

df = pd.DataFrame(zones_data)

top_zones = zones_data[:3]

max_risk = max(df["risk"])
min_risk = min(df["risk"])
avg_risk = sum(df["risk"]) / len(df)

risk_summary = (max_risk, avg_risk, min_risk)

final_result = overall_status(avg_risk)

print("\nFull Data:")
print(df)

print("\nZone Status:")
print(df[["zone", "status"]])

print("\nTop 3 Risky Zones:")
for zone in top_zones:
    print("Zone", zone["zone"], "->", zone["risk"])

print("\nRisk Summary (max, avg, min):")
print(risk_summary)

print("\nFinal Decision:")
print(final_result)

print("\nInsight:")
print("A smart city works best when traffic, pollution, and energy use are well balanced.")