import copy

def create_users():
    user_list = []
    total_users = int(input("Enter number of users: "))

    for i in range(total_users):
        print(f"\nUser {i+1}")

        total_files = int(input("Enter number of files: "))
        file_list = []

        for j in range(total_files):
            name = input(f"Enter file {j+1}: ")
            file_list.append(name)

        usage_value = int(input("Enter usage: "))

        user_list.append({
            "id": i + 1,
            "data": {
                "files": file_list,
                "usage": usage_value
            }
        })
    return user_list


def make_copies(data):
    direct_ref = data
    shallow_copy = copy.copy(data)
    deep_copy = copy.deepcopy(data)
    return direct_ref, shallow_copy, deep_copy


def update_data(dataset, roll_no):
    for user in dataset:
        user["data"]["usage"] += 50

        if roll_no % 2 == 0:
            user["data"]["files"].append("new.txt")
        else:
            if len(user["data"]["files"]) > 0:
                user["data"]["files"].pop()

    return dataset


def analyze_integrity(original, shallow, deep):
    leakage_count = 0
    safe_count = 0
    overlap_count = 0

    for i in range(len(original)):
        original_files = set(original[i]["data"]["files"])
        shallow_files = set(shallow[i]["data"]["files"])
        deep_files = set(deep[i]["data"]["files"])

        if original_files != deep_files:
            leakage_count += 1

        if deep_files != shallow_files:
            safe_count += 1

        overlap_count += len(original_files.intersection(shallow_files))

    return leakage_count, safe_count, overlap_count


users_data = create_users()

print("\n--- BEFORE ---")
print(users_data)

assigned_data, shallow_data, deep_data = make_copies(users_data)

roll_number = int(input("\nEnter your roll number: "))

shallow_data = update_data(shallow_data, roll_number)

print("\n--- AFTER ---")

print("\nOriginal Data:")
print(users_data)

print("\nShallow Copy:")
print(shallow_data)

print("\nDeep Copy:")
print(deep_data)

report = analyze_integrity(users_data, shallow_data, deep_data)

print("\nIntegrity Report (leakage, safe, overlap):")
print(report)

print("\nData Corruption:")
print("Original data got affected because shallow copy shares inner structures.")