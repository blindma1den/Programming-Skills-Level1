"""2. A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal,
 there are activities on the beaches.
Spring: France and Italy. In France, there are extreme sports activities, and in Italy,
 there's a cultural and historical tour.
Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria,
 there are cultural and historical activities.
Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.

Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.
12. Important: With the information you have, you should ask the user the right questions and display on screen what their best destination would be.

Clue: You could consider the user's budget"""

while True:
    print("Travel season 2024")
    print()
    print("system that helps users choose their best destination according to their personal preferences and the season they want to travel in")
    print("ok do you want continues?")
    answer = input("yes or not?: ")
    if answer == "yes":
        print("okay")
    else:
        print("good bye")
        exit()
    print()
    print("first tell us how much is your budget")
    budget = int(input("Insert your budget for this travel: ")) #int
    print()
    print("okay now when you travel?")
    date = (input("season of your travel: ")) #string
    print()
    print("and finally what activities you prefer?")
    activities = input("What activity would you like to do on your trip? Sport activities or cultural activities: ") #string
    print()
    print(f"okay your budget is {budget} and you travel on the {date},the activited you selected are {activities}")

    if date == "winter" and activities == "sport activities": 
        print(f"i recomend you a trip to Andorra, for this trip the cost will by $100 and your budget is {budget}.")
        continue
    elif date == "winter" and activities == "cultural activities":
        print(f"i recomend you a trip to Switzerland, for this trip the cost will by $100 and your budget is {budget}")
        continue
    elif date == "summer" and activities == "sport activities":
        print(f"i recomend you a trip to Spain, for this trip the cost will by $400 and your budget is {budget}")
        continue
    elif date == "summer" and activities == "cultural activities":
        print(f"i recomend you a trip to Portugal, for this trip the cost will by $400 and your budget is {budget}")
        continue 
    elif date == "spring" and activities == "sport activities":
        print(f"i recomend you a trip to France, for this trip the cost will by $300 and your budget is {budget}")
        continue
    elif date == "spring" and activities == "cultural activities":
        print(f"i recomend you a trip to Italy, for this trip the cost will by $300 and your budget is {budget}")
        continue  
    elif date == "autumn" and activities == "sport activities":
        print(f"i recomend you a trip to Belgium, for this trip the cost will by $200 and your budget is {budget}")
        continue
    elif date == "autumn" and activities == "cultural activities":
        print(f"i recomend you a trip to Austria, for this trip the cost will by $200 and your budget is {budget}")
        continue
    else:
        print("incorrect data")
        break   
    






