profiles = {
    "101": {"Name": "Ali", "Dept": "CSE", "Year": "2025"},
    "102": {"Name": "Sara Khan", "Dept": "CSE", "Year": "2024"},
    "103": {"Name": "Hassan", "Dept": "CSE", "Year": "2023"}
}

# Get ID input
user_id = input("Enter User ID: ")

# Show profile or error
if user_id in profiles:
    print("\n--- Profile Details ---")
    for key, value in profiles[user_id].items():
        print(f"{key}: {value}")
else:
    print("Invalid ID! No profile found.")