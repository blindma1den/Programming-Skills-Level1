#2. A travel agency has a special offer for traveling in any season of 2024. Their destinations are:
#
#Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
#Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
#Spring: France and Italy. In France, there are extreme sports activities, and in Italy, there's a cultural and historical tour.
#Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria, there are cultural and historical activities.
#Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.
#
#Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.
#12. Important: With the information you have, you should ask the user the right questions and display on screen what their best destination would be.
#
#Clue: You could consider the user's budget

destinations = {
    "Winter": {
        "Andorra": {
            "cost": 100,
            "activities": ["skiing"]
        },
        "Switzerland": {
            "cost": 100,
            "activities": ["tour of the Alps"]
        }
    },
    "Summer": {
        "Spain": {
            "cost": 400,
            "activities": ["hiking"]
        },
        "Portugal": {
            "cost": 300,
            "activities": ["beaches"]
        }
    },
    "Spring": {
        "France": {
            "cost": 300,
            "activities": ["extreme sports"]
        },
        "Italy": {
            "cost": 200,
            "activities": ["cultural and historical tour"]
        }
    },
    "Autumn": {
        "Belgium": {
            "cost": 200,
            "activities": ["hiking"]
        },
        "Austria": {
            "cost": 200,
            "activities": ["cultural and historical activities"]
        }
    }
}

def get_user_input():
    print("Welcome to the travel agency!")
    print("Please enter your budget:")
    budget = int(input())
    if budget < 0:
        print("Invalid budget")
        return None
    elif budget < 100:
        print("You should consider a higher budget")
    elif budget >= 100 and budget < 200:
        print("You can choice Winter")
    elif budget >= 200 and budget < 300:
        print("You can choice Winter and Spring")
    elif budget >= 300 and budget < 400:
        print("You can choice Winter, Spring and Summer")
    elif budget >= 400:
        print("You can choice all seasons")
    print("Please enter your season:")
    season = input()
    return budget, season

def personal_preferences(season):
    if season == "Winter":
        print("What activities would you prefer?")
        print("1. Skiing")
        print("2. Tour of the Alps")
        
        while True:
            preference = int(input("Enter your preference: "))
            if preference == 1:
                print("You should go to Andorra")
                break
            if preference == 2:
                print("You should go to Switzerland")
                break
            else:
                print("Invalid choice")
    if season == "Autumn":
        print("What activities would you prefer?")
        print("1. Hiking and extreme sports")
        print("2. Cultural and Historical activities")
        
        while True:
            preference = int(input("Enter your preference: "))
            if preference == 1:
                print("You should go to Belgium")
                break
            if preference == 2:
                print("You should go to Austria")
                break
            else:
                print("Invalid choice")
                
    if season == "Spring":
        print("What activities would you prefer?")
        print("1. Extreme sports")
        print("2. Cultural and historical tour")

        while True:
            preference = int(input("Enter your preference: "))
            if preference == 1:
                print("You should go to France")
                break
            if preference == 2:
                print("You should go to Italy")
                break
            else:
                print("Invalid choice")
    if season == "Summer":
        print("What activities would you prefer?")
        print("1. Hiking and extreme sports")
        print("2. Activities on the Beache")

        while  True:
            preference = int(input("Enter your preference: "))
            if preference == 1:
                print("You should go to Spain")
                break
            if preference == 2:
                print("You should go to Portugal")
                break
            else:
                print("Invalid choice")
            


while True:
    user_input = get_user_input()
    if user_input:
        budget, season = user_input
        personal_preferences(season)
        
    print("Thanks for your preference")
    break