
energy_data = [42, 110, 210, 28, 70, 175, -10, 55, 18, 240]
usage_categories = {
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}
for value in energy_data:
    if value < 0:
        usage_categories["invalid"].append(value)
    elif 0 <= value <= 50:
        usage_categories["efficient"].append(value)
    elif 51 <= value <= 150:
        usage_categories["moderate"].append(value)
    else:
        usage_categories["high"].append(value)
valid_values = [v for v in energy_data if v >= 0]
summary_info = (
    len(energy_data),                 
    sum(valid_values),                
    len(usage_categories["efficient"]),
    len(usage_categories["moderate"]),
    len(usage_categories["high"]),
    len(usage_categories["invalid"]),
)
analysis_result = []
if len(usage_categories["high"]) > 3:
    analysis_result.append("Overconsumption")

if abs(len(usage_categories["efficient"]) - len(usage_categories["moderate"])) <= 1:
    analysis_result.append("Balanced Usage")
else:
    analysis_result.append("Moderate Usage")

if sum(valid_values) > 600:
    analysis_result.append("Energy Waste Detected")
print(" Smart Campus Energy Report ")

print("Categorized Readings:")
for category, values in usage_categories.items():
    print(f"{category.capitalize()}: {values}")

print(f"Number of Buildings: {summary_info[0]}")
print(f"Total Consumption: {summary_info[1]}")

print("Efficiency Result:")
for res in analysis_result:
    print(res)