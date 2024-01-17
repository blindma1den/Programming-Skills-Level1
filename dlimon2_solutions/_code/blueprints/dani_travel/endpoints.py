from . import dani_travel
from .travel_data import TRAVEL_DATA
from flask import session, redirect, url_for, render_template, request


"""
A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland,
    there's a tour of the Swiss Alps.
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

"""

@dani_travel.before_request
def before_request_validations():

    if 'dani_travel_destinations' not in session:
        session['dani_travel_destinations'] = TRAVEL_DATA


@dani_travel.route('/', methods=['GET', 'POST'])
def hello():
    
    if request.method == 'GET':
        if request.args:
            context = request.args.to_dict()
            return render_template('dani_travel/hello.html', **context)
        return render_template('dani_travel/hello.html')
    
    elif request.method == 'POST':

        data = request.form.to_dict()
        
        budget = int(data['budget'])
        print(session['dani_travel_destinations'][0]['activities'].values())
        best_travels = [item for item in session['dani_travel_destinations'] 
                        if item['season'].lower() == data['season'] 
                        and item['cost'] <= budget 
                        and any(data['experiences'].lower() in activity.lower() for activity in item['activities'].values())]

        best_travels_sorted_by_cost = sorted(best_travels, key=lambda x: x['cost'])
        print(best_travels_sorted_by_cost)
        context = {
            'best_travels': best_travels_sorted_by_cost
        }

        return redirect(url_for('dani_travel.hello', **context))
