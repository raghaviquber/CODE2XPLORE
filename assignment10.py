import math
import copy
import numpy as np
import pandas as pd

def get_input_details():
    total_zones = int(input("Enter number of zones: "))
    student_roll = int(input("Enter your roll number: "))
    return total_zones, student_roll


def create_zone(zone_number):
    print(f"\nEnter data for Zone {zone_number}")

    traffic_level = int(input("Traffic: "))
    pollution_level = int(input("Pollution: "))
    energy_usage = int(input("Energy: "))

    past_history = list(map(int, input("Enter 5 history values: ").split()))

    return {
        "zone_id": zone_number,
        "metrics": {
            "traffic": traffic_level,
            "pollution": pollution_level,
            "energy": energy_usage
        },
        "history": past_history
    }


def collect_all_zones(zone_count):
    return [create_zone(i) for i in range(1, zone_count + 1)]


def personalize_dataset(zone_data, roll_number):
    if roll_number % 2 == 0:
        return list(reversed(zone_data))
    else:
        return zone_data[3:] + zone_data[:3]


def generate_copies(original_data):
    assigned_copy = original_data
    shallow_copy = copy.copy(original_data)
    deep_copy = copy.deepcopy(original_data)
    return assigned_copy, shallow_copy, deep_copy


def apply_mutation(data_list):
    for zone in data_list:
        zone["metrics"]["traffic"] += 5
        zone["metrics"]["pollution"] -= 2
        zone["metrics"]["energy"] += 3
        zone["history"].append(50)


def calculate_risk(metrics):
    return math.log(metrics["traffic"] + metrics["pollution"] + metrics["energy"])


def convert_to_dataframe(zone_data):
    records = []
    for zone in zone_data:
        metrics = zone["metrics"]
        records.append({
            "zone_id": zone["zone_id"],
            "traffic": metrics["traffic"],
            "pollution": metrics["pollution"],
            "energy": metrics["energy"],
            "risk_score": calculate_risk(metrics)
        })
    return pd.DataFrame(records)


def perform_analysis(dataframe):
    values = dataframe[["traffic", "pollution", "energy", "risk_score"]].values

    avg_values = np.mean(values, axis=0)
    variance_values = np.var(values, axis=0)

    traffic_vals = values[:, 0]
    pollution_vals = values[:, 1]

    if len(traffic_vals) < 3:
        correlation = 0
    else:
        numerator = np.sum((traffic_vals - np.mean(traffic_vals)) * (pollution_vals - np.mean(pollution_vals)))
        denominator = (
            np.sqrt(np.sum((traffic_vals - np.mean(traffic_vals)) ** 2)) *
            np.sqrt(np.sum((pollution_vals - np.mean(pollution_vals)) ** 2))
        )

        correlation = 0 if denominator == 0 else numerator / denominator

    return avg_values, variance_values, correlation


def find_anomalies(dataframe):
    avg_risk = dataframe["risk_score"].mean()
    std_risk = dataframe["risk_score"].std()
    return dataframe[dataframe["risk_score"] > avg_risk + std_risk]


def find_risk_clusters(dataframe):
    high_risk_flags = dataframe["risk_score"] > dataframe["risk_score"].mean()
    clusters = []
    current_cluster = []

    for index, is_risky in enumerate(high_risk_flags):
        if is_risky:
            current_cluster.append(dataframe.iloc[index]["zone_id"])
        else:
            if len(current_cluster) > 1:
                clusters.append(current_cluster)
            current_cluster = []

    return clusters


def compute_stability(variance_values):
    return 1 / (np.mean(variance_values) + 1e-5)


def decide_system_status(max_risk, stability_score):
    if max_risk < 4:
        return "System Stable"
    elif max_risk < 5:
        return "Moderate Risk"
    elif stability_score < 0.1:
        return "High Corruption Risk"
    else:
        return "Critical Failure"


def main():
    zone_count, roll_number = get_input_details()

    zone_data = collect_all_zones(zone_count)
    zone_data = personalize_dataset(zone_data, roll_number)

    print("\nBEFORE MUTATION:")
    print(zone_data[0])

    assigned, shallow_copy, deep_copy = generate_copies(zone_data)

    apply_mutation(shallow_copy)

    print("\nAFTER MUTATION:")
    print(zone_data[0])  
    df = convert_to_dataframe(zone_data)
    print("\nDataFrame:\n", df)

    mean_vals, variance_vals, correlation = perform_analysis(df)

    anomalies = find_anomalies(df)
    clusters = find_risk_clusters(df)

    stability_score = compute_stability(variance_vals)

    max_risk = df["risk_score"].max()
    min_risk = df["risk_score"].min()

    final_status = decide_system_status(max_risk, stability_score)

    print("\nCorrelation:", correlation)
    print("\nAnomalies:\n", anomalies)
    print("\nClusters:", clusters)

    print("\nSummary Tuple:")
    print((max_risk, min_risk, stability_score))

    print("\nFinal Decision:", final_status)


if __name__ == "__main__":
    main()