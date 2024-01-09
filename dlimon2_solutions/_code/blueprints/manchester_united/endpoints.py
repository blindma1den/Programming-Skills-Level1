from . import manchester_united
from .player_profiles import PLAYER_PROFILES
from flask import session, request, render_template, redirect, url_for, flash


@manchester_united.before_request
def before_request_validations():

    # check player profiles
    if 'manchester_player_profiles' not in session:
        session['manchester_player_profiles'] = PLAYER_PROFILES



@manchester_united.route('/')
def hello():

    # fastest player
    fastest_player = max(session['manchester_player_profiles'], key=lambda x: x['speed'])

    # top scorer
    top_scorer = max(session['manchester_player_profiles'], key=lambda x: x['goals'])

    # most assists
    most_assists = max(session['manchester_player_profiles'], key=lambda x: x['assists'])

    # highest passing accuracy
    highest_passing_accuracy = max(session['manchester_player_profiles'], key=lambda x: x['passing_accuracy'])

    # most defensive involvements
    most_defensive_involvements = max(session['manchester_player_profiles'], key=lambda x: x['defensive_involvements'])
    
    context = {
        'fastest_player': fastest_player['name'],
        'speed': fastest_player['speed'], 
        'top_scorer': top_scorer['name'],
        'goals': top_scorer['goals'],
        'most_assists': most_assists['name'],
        'assists': most_assists['assists'],
        'highest_passing_accuracy': highest_passing_accuracy['name'],
        'passing_accuracy': highest_passing_accuracy['passing_accuracy'],
        'most_defensive_involvements': most_defensive_involvements['name'],
        'defensive_involvements': most_defensive_involvements['defensive_involvements']
    }


    return render_template('manchester_united/hello.html', **context)


@manchester_united.route('/top_stats')
def top_stats():
        # fastest player
    fastest_player = max(session['manchester_player_profiles'], key=lambda x: x['speed'])

    # top scorer
    top_scorer = max(session['manchester_player_profiles'], key=lambda x: x['goals'])

    # most assists
    most_assists = max(session['manchester_player_profiles'], key=lambda x: x['assists'])

    # highest passing accuracy
    highest_passing_accuracy = max(session['manchester_player_profiles'], key=lambda x: x['passing_accuracy'])

    # most defensive involvements
    most_defensive_involvements = max(session['manchester_player_profiles'], key=lambda x: x['defensive_involvements'])
    
    context = {
        'fastest_player': fastest_player['name'],
        'speed': fastest_player['speed'], 
        'top_scorer': top_scorer['name'],
        'goals': top_scorer['goals'],
        'most_assists': most_assists['name'],
        'assists': most_assists['assists'],
        'highest_passing_accuracy': highest_passing_accuracy['name'],
        'passing_accuracy': highest_passing_accuracy['passing_accuracy'],
        'most_defensive_involvements': most_defensive_involvements['name'],
        'defensive_involvements': most_defensive_involvements['defensive_involvements']
    }

    return render_template('manchester_united/top_stats.html', **context)

@manchester_united.route('/compare_players', methods=['GET', 'POST'])
def compare_players():
    
    if request.method == 'GET'and not request.args:

        players = {
            'players': session['manchester_player_profiles'] }

        return render_template('manchester_united/compare_players.html', **players)
    
    if request.method == 'GET' and request.args:

        first_player = request.args.get('first_player')
        second_player = request.args.get('second_player')

        context = {
            'first_player': first_player,
            'first_player': second_player
        }

        return render_template('manchester_united/compare_players.html', **context)
    
    if request.method == 'POST':
            
            first_player = request.form.get('first_player')
            second_player = request.form.get('second_player')

            first_player = [player for player in session['manchester_player_profiles'] if player['jersey_number'] == int(first_player)][0]
            second_player = [player for player in session['manchester_player_profiles'] if player['jersey_number'] == int(second_player)][0]

            context = {
                'first_player': first_player,
                'second_player': second_player
            }
    
            return render_template('manchester_united/compare_players.html', **context)
    

@manchester_united.route('/player_details', methods=['GET', 'POST'])
def player_details():
         
        if request.method == 'GET' and not request.args:
            return render_template('manchester_united/player_details.html')
        
        if request.method == 'GET' and request.args:
    
            player = request.args.get('player')
    
            context = {
                'player': player
            }
    
            return render_template('manchester_united/player_details.html', **context)
        
        if request.method == 'POST':
    
            jersey_number = request.form.get('jersey_number')
    
            player = [player for player in session['manchester_player_profiles'] if player['jersey_number'] == int(jersey_number)]

            if player == []:
                flash('Player not found. Please enter a valid jersey number.')
                return redirect(url_for('manchester_united.player_details'))
   
            context = {
                'player': player[0]
            }
    
            return render_template('manchester_united/player_details.html', **context)