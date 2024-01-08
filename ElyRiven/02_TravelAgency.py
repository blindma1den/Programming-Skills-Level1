# 2. A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

# Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
# Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
# Spring: France and Italy. In France, there are extreme sports activities, and in Italy, there's a cultural and historical tour.
# Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria, there are cultural and historical activities.
# Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.

# Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.
# 12. Important: With the information you have, you should ask the user the right questions and display on screen what their best destination would be.

# Clue: You could consider the user's budget

TRAVELDESTINATIONS = {
    "winter": {
        "andorra": "Skying activities",
        "switzerland": "Tour of the Swiss Alps"
        },
    "summer": {
        "spain": "Hiking and extreme sports activities",
        "portugal": "Activities on the beaches"
    },
    "spring": {
        "france": "Extreme sports activities",
        "italy": "Cultural and historical tour"
    },
    "autumn": {
        "belgium": "Hiking and extreme sports activities",
        "austria": "Cultural and historical activities"
    }
}

def main():
    print("\t\tWelcome to our travel agency!\n\n")
    budget = getBudget()
    if budget != None:
        print(f"Your budget is: ${budget}")
        season = getSeason(budget)
        if season != None:
            print(f"Your season is: {season}")
            destination = getActivity(season)
            if type(destination) != str:
                print("Since you have no preferences, we can offer you to travel to these beautiful destinations:\n")
                for country, activity in destination.items():
                    print(f"Country - {country.title()}\t Activities - {activity}") in destination
            else:
                print(f"Your best destination based on your preferences is: {destination.title()}")
        print("\nThank you for using our travel agency!")

def travelSuggestion(season, activity):
    print(f"Your travel suggestion is: {TRAVELDESTINATIONS[season]}")

# Ask for the activity of preference
def getActivity(season):
    x = 1
    activity1 = ""
    activity2 = ""
    print("What is your activity of preference? Select one of the following\n")
    for key in TRAVELDESTINATIONS[season]:
        print(f"{x}. {TRAVELDESTINATIONS[season][key]}")
        if x == 1:
            activity1 = TRAVELDESTINATIONS[season][key]
        if x == 2:
            activity2 = TRAVELDESTINATIONS[season][key]
        x += 1
    print(f"{x}. No preference")
    try:
        option = int(input(">> "))
        if option == 3:
            return TRAVELDESTINATIONS[season]
        elif option == 1:
            return getDestination(season, activity1)
        elif option == 2:
            return getDestination(season, activity2)
    except:
        print("Invalid input.")

def getDestination(season, activity):
    for inner_key, inner_value in TRAVELDESTINATIONS[season].items():
        if inner_value == activity:
            return inner_key

def seasonRecommend(budget):
    if budget <= 100:
        return "Winter"
    elif budget <= 200:
        return "Autumn"
    elif budget <= 300:
        return "Spring"
    elif budget <= 400:
        return "Summer"
    else:
        return "Summer"

def getSeason(budget):
    try:
        recomendation = seasonRecommend(budget)
        print(f"\nSeasons Available\nWinter - Spring - Summer - Autumn | RECOMMENDED SEASON -> {recomendation}\n")
        season = input(">> ").lower()
        if season in TRAVELDESTINATIONS:
            return season
        else:
            print("Invalid input.")
    except:
        print("Invalid input.")

def getBudget():
    try:
        budget = float(input("Enter your budget: $"))
        if budget > 0:
            return budget
        else:
            print("Invalid input.")
    except:
        print("Invalid input.")

if __name__ == "__main__":
    main()