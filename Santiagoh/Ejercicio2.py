import sys

class Menu:

    def select(self):
        print("1. Choose menu")
        print("2. Get help to choose the best destination")
        print("3. Exit")
        self.option = int(input("Enter option: "))
        return self.option
    

class Actions(Menu):

    def __init__(self):
        self.destinations = {
            'Winter': {'Andorra': 'skiing', 'Switzerland': 'tour of the Swiss Alps', 'cost': 100},
            'Summer': {'Spain': 'hiking and extreme sports', 'Portugal': 'beach activities', 'cost': 400},
            'Spring': {'France': 'extreme sports', 'Italy': 'cultural and historical tour', 'cost': 300},
            'Autumn': {'Belgium': 'hiking and extreme sports', 'Austria': 'cultural and historical activities', 'cost': 200}
        }

    def help_destination(self):
        print("Let's try to choose the best destination for you")
        print("We are going to ask some questions")

        budget = int(input("Enter your budget: "))
        season = input("What is your favorite season?: ").capitalize()

        if season in self.destinations and budget >= self.destinations[season]['cost']:
            print(f"In {season}, you can travel to the following destinations with these activities:")
            for destination, activity in self.destinations[season].items():
                if destination != 'cost':
                    print(f"- {destination}: {activity}")
            activity = input("Which activity do you prefer?: ")
            for destination, act in self.destinations[season].items():
                if act == activity:
                    print(f"Great! You can travel to {destination} in {season} and enjoy {activity}")
        else:
            print("Sorry, your budget is not enough to travel in that season")

    def numbers(self, option):
        if option == 1:
            print("You have chosen the menu")
        elif option == 2:
            self.help_destination()
        elif option == 3:
            print("You have chosen to exit. See you later!")
            sys.exit()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu_instance = Menu()
    actions_instance = Actions()

    while True:
        option = menu_instance.select()
        actions_instance.numbers(option)
