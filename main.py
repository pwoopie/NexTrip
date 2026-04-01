import random


def get_trip_data():
    return {
        "san diego": {
            "beach": [("La Jolla Cove", 0), ("Coronado Beach", 0)],
            "food": [("Little Italy", 30), ("Tacos El Gordo", 20)],
            "nightlife": [("Gaslamp Quarter", 40)],
            "nature": [("Torrey Pines", 15)],
            "extras": [("Seaport Village", 0), ("Balboa Park", 20), ("Old Town", 10)]
        },
        "los angeles": {
            "beach": [("Santa Monica Pier", 0), ("Venice Beach", 0)],
            "food": [("Grand Central Market", 25), ("In-N-Out", 15)],
            "nightlife": [("Hollywood", 35)],
            "nature": [("Griffith Park", 10)],
            "extras": [("The Grove", 0), ("Walk of Fame", 0), ("The Getty", 20)]
        },
        "las vegas": {
            "beach": [],
            "food": [("Bacchanal Buffet", 50), ("In-N-Out", 15)],
            "nightlife": [("The Strip", 0), ("Fremont Street", 10)],
            "nature": [("Red Rock Canyon", 20)],
            "extras": [("Bellagio Fountains", 0), ("Caesars Palace", 0), ("AREA15", 35)]
        },
        "san francisco": {
            "beach": [("Baker Beach", 0)],
            "food": [("Fisherman's Wharf", 30), ("Chinatown", 20)],
            "nightlife": [("North Beach", 25)],
            "nature": [("Golden Gate Park", 0), ("Twin Peaks", 0)],
            "extras": [("Pier 39", 0), ("Lombard Street", 0), ("Alamo Square", 0)]
        },
        "new york": {
            "beach": [],
            "food": [("Times Square Eats", 25), ("Katz's Delicatessen", 30)],
            "nightlife": [("Broadway Area", 40), ("Rooftop Lounge", 35)],
            "nature": [("Central Park", 0), ("Bryant Park", 0)],
            "extras": [("Brooklyn Bridge", 0), ("Fifth Avenue", 0), ("Grand Central Terminal", 0)]
        }
    }


def show_menu(trips):
    print("Welcome to NexTrip, your Travel Planner!")
    print("\nAvailable destinations:")
    for city in trips:
        print(f"- {city.title()}")

    print("\nAvailable interest categories:")
    print("- beach")
    print("- food")
    print("- nightlife")
    print("- nature")


def get_user_input():
    destination = input("\nEnter destination: ").lower().strip()
    days = int(input("How many days is your trip? "))
    budget = int(input("Enter your budget: "))
    interests = input("Enter your interests (comma separated): ").lower().split(",")

    cleaned_interests = []
    for interest in interests:
        cleaned_interests.append(interest.strip())

    return destination, days, budget, cleaned_interests


def build_activities(destination, days, budget, interests, trips):
    activities = []
    total_cost = 0

    for interest in interests:
        if interest in trips[destination]:
            for activity, cost in trips[destination][interest]:
                if total_cost + cost <= budget and (activity, cost) not in activities:
                    activities.append((activity, cost))
                    total_cost += cost

    random.shuffle(activities)

    max_activities = days * 3

    if len(activities) < max_activities:
        extras = trips[destination]["extras"][:]
        random.shuffle(extras)

        for activity, cost in extras:
            if len(activities) >= max_activities:
                break
            if total_cost + cost <= budget and (activity, cost) not in activities:
                activities.append((activity, cost))
                total_cost += cost

    return activities, total_cost


def print_itinerary(activities, total_cost, days):
    if len(activities) == 0:
        print("\nNo activities fit your budget and interests.")
        return

    print("\nYour Trip Itinerary:")
    activity_index = 0

    for day in range(1, days + 1):
        if activity_index >= len(activities):
            break

        print(f"\nDay {day}:")

        if activity_index < len(activities):
            activity, cost = activities[activity_index]
            print(f"Morning: {activity} (${cost})")
            activity_index += 1

        if activity_index < len(activities):
            activity, cost = activities[activity_index]
            print(f"Afternoon: {activity} (${cost})")
            activity_index += 1

        if activity_index < len(activities):
            activity, cost = activities[activity_index]
            print(f"Evening: {activity} (${cost})")
            activity_index += 1

    print(f"\nEstimated total cost: ${total_cost}")


def main():
    trips = get_trip_data()
    show_menu(trips)
    destination, days, budget, interests = get_user_input()

    if destination in trips:
        activities, total_cost = build_activities(destination, days, budget, interests, trips)
        print_itinerary(activities, total_cost, days)
    else:
        print("\nSorry, destination not found. Please choose from the listed destinations.")


main()