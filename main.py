print("Welcome to the Trip Planner!")

# Step 1: Get user input
destination = input("Enter destination: ").lower()
days = int(input("How many days is your trip? "))
budget = input("Enter your budget: ")
interests = input("Enter your interests (comma separated): ").lower().split(",")

# Step 2: Store trip data
trips = {
    "san diego": {
        "beach": ["La Jolla Cove", "Coronado Beach"],
        "food": ["Little Italy", "Tacos El Gordo"],
        "nightlife": ["Gaslamp Quarter"],
        "nature": ["Torrey Pines"]
    }
}

# Step 3: Generate itinerary
if destination in trips:
    activities = []

    for interest in interests:
        interest = interest.strip()
        if interest in trips[destination]:
            activities.extend(trips[destination][interest])

    print("\nYour Trip Itinerary:")
    activity_index = 0

    for day in range(1, days + 1):
        print(f"\nDay {day}:")
        for _ in range(2):
            if activity_index < len(activities):
                print("-", activities[activity_index])
                activity_index += 1
else:
    print("Sorry, destination not found.")