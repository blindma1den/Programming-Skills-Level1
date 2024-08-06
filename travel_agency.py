'''2. A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
Spring: France and Italy. In France, there are extreme sports activities, and in Italy, there's a cultural and historical tour.
Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria, there are cultural and historical activities.
Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.

Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.
12. Important: With the information you have, you should ask the user the right questions and display on screen what their best destination would be.

Clue: You could consider the user's budget'''

budget = {
    100:{"Winter":{"Andorra":"You can go to skiing activities","Switzerland":"You can go on a tour to the Swiss Alps"}},
    200:{
        "Winter":{"Andorra":"You can go to skiing activities","Switzerland":"You can go on a tour to the Swiss Alps"},
        "Autumn":{"Belgium":"there are hiking and extreme sports activities", "Australia":"there are cultural and historical activities"}
        },
    300:{
        "Winter":{"Andorra":"You can go to skiing activities","Switzerland":"You can go on a tour to the Swiss Alps"},
        "Autumn":{"Belgium":"there are hiking and extreme sports activities", "Australia":"there are cultural and historical activities"},
        "Spring":{"France":"there are extreme sports activities", "Italy":"there's a cultural and historical tour"}
        }, 
    400:{
        "Winter":{"Andorra":"You can go to skiing activities","Switzerland":"You can go on a tour to the Swiss Alps"},
        "Autumn":{"Belgium":"there are hiking and extreme sports activities", "Australia":"there are cultural and historical activities"},
        "Spring":{"France":"there are extreme sports activities", "Italy":"there's a cultural and historical tour"},
        "Summer":{"Spain":"there are hiking and extreme sports activities", "Portugal":"there are activities on the beaches"}
    }
}

def choose_budget(key:int):
    if key >=400:
        return budget[400]
    elif key >=300:
        return budget[300]
    elif key >=200:
        return budget[200]
    elif key >=100:
        return budget[100]
    
    
def destination(budgetkey:int, season:str, country:str):
    return f"{country}: {choose_budget(budgetkey)[season][country]}"

def main():
    budgetkey=int(input("Welcome, please type your budget."))
    if budgetkey <100:
        print("Sorry, you don't have enoguh funds.")
    else:
        print(f"Based on your budget, we recommend you these seasons to travel: {list(choose_budget(budgetkey).keys())}")
        season=input("please type the season you'd like among the available options. ")
        country=input(f"please type the country you'd like among the options.\n {list(choose_budget(budgetkey)[season].keys())} ")
        print(f"this is your choice and the activities that come with the offer:\n{destination(budgetkey, season, country)}")
        print("Thank you for using our services.")

main()