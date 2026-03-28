print("Welcome to NexTrip, your Travel Planner!")

destination = input("Enter destination: ").lower()
days = int(input("How many days is your trip? "))
budget = int(input("Enter your budget: "))
interests = input("Enter your interests (comma separated): ").lower().split(",")

trips = {
    "san diego": {
        "beach": [("La Jolla Cove", 0), ("Coronado Beach", 0)],
        "food": [("Little Italy", 30), ("Tacos El Gordo", 20)],
        "nightlife": [("Gaslamp Quarter", 40)],
        "nature": [("Torrey Pines", 15)]
    },
    "los angeles": {
        "beach": [("Santa Monica Pier", 0), ("Venice Beach", 0)],
        "food": [("Grand Central Market", 25), ("In-N-Out", 15)],
        "nightlife": [("Hollywood", 35)],
        "nature": [("Griffith Park", 10)]
    }
}

if destination in trips:
    activities = []
    total_cost = 0

    for interest in interests:
        interest = interest.strip()
        if interest in trips[destination]:
            for activity, cost in trips[destination][interest]:
                if total_cost + cost <= budget:
                    activities.append((activity, cost))
                    total_cost += cost

    if len(activities) == 0:
        print("\nNo activities fit your budget and interests.")
    else:
        print("\nYour Trip Itinerary:")
        activity_index = 0

for day in range(1, days + 1):
    print(f"\nDay {day}:")

    # Creates a daily schedule with up to 3 activities (morning, afternoon, evening)
    # Morning 
    if activity_index < len(activities):
        activity, cost = activities[activity_index]
        print(f"Morning: {activity} (${cost})")
        activity_index += 1

    # Afternoon
    if activity_index < len(activities):
        activity, cost = activities[activity_index]
        print(f"Afternoon: {activity} (${cost})")
        activity_index += 1

    # Evening
    if activity_index < len(activities):
        activity, cost = activities[activity_index]
        print(f"Evening: {activity} (${cost})")
        activity_index += 1

        print(f"\nEstimated total cost: ${total_cost}")
else:
    print("Sorry, destination not found.")