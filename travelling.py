'''


2. A travel agency has a special offer for traveling in any season of 2024.
Their destinations are:

Winter: Andorra and Switzerland. In Andorra, there are skiing activities,
and in Switzerland, there's a tour of the Swiss Alps.
Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities.
In Portugal, there are activities on the beaches.
Spring: France and Italy. In France, there are extreme sports activities, and in Italy,
there's a cultural and historical tour.
Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities,
and in Austria, there are cultural and historical activities.
Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.

Design a system that helps users choose their best destination according to their personal
preferences and the season they want to travel in.
12. Important: With the information you have, you should ask the user the right questions
and display on screen what their best destination would be.

Clue: You could consider the user's budget

'''
seasons = {'summer': [['Spain', 'Portugal'], 400], 'winter': [['Andorra', 'Switzerland'], 100],
           'spring': [['France', 'Italy'], 300], 'autumn': [['Belgium', 'Austria'], 200]}
activities = {'Spain': 'hiking and extreme sports activities',
              'Portugal': 'activities on the beaches',
              'Andorra': 'skiing activities', 'Switzerland': 'tour of the Swiss Alps',
              'France': 'extreme sports activities', 'Italy': 'cultural and historical tour',
              'Belgium': 'hiking and extreme sports activities',
              'Austria': 'cultural and historical activities'}
budget_values = {'summer': 400, 'winter': 100,
                 'spring': 300, 'autumn': 200}

def season():
    choice = True
    while choice:
        choose_season = input('What season would you like to travel in? ')
        if choose_season in seasons:
            print(f'Selected season: {choose_season.capitalize()}')
            print(f'Options: {seasons[choose_season][0][0]}')
            print(f'Options: {seasons[choose_season][0][1]}')
            return choose_season  # Return the selected season
        else:
            print('Invalid season choice. Please choose from summer, winter, spring, or autumn.')

def budget():
    logic = True
    while logic:
        budget_value = int(input('What is your budget($)? '))
        return budget_value

def recommendation():
    your_season = season()
    your_budget = budget()
    
    destination = seasons[your_season]
    budget_place = budget_values[your_season]

    if your_budget >= budget_place:
        print('You can go to these destinations: ', destination)
    else:
        print('You should consider changing your destination')

if __name__ == "__main__":
    recommendation()

