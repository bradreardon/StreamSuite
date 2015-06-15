import functools

__author__ = 'bradreardon'

def get_callback(stream, function):
    return functools.partial(function, stream)

def ei_update_tournament_name(stream, name):
    stream.mutables['tournament'] = name

def ei_update_event_name(stream, name):
    stream.mutables['event'] = name

def mi_update_round(stream, match_round):
    stream.mutables['match_round'] = match_round

def ps_update_score(stream, token, operation):
    if operation == '+':
        add = 1
    elif operation == '-':
        add = -1
    else:
        print "Invalid argument '{}'.".format(operation)
        return

    stream.mutables[token] += add

def ps_update_player1_score(stream, operation):
    ps_update_score(stream, 'player1_score', operation)

def ps_update_player2_score(stream, operation):
    ps_update_score(stream, 'player2_score', operation)

def ps_update_player1_name(stream, name):
    stream.mutables['player1_name'] = name

def ps_update_player2_name(stream, name):
    stream.mutables['player2_name'] = name

def ps_reset_players(stream, p1_name, p2_name):
    stream.mutables['player1_name'] = p1_name
    stream.mutables['player1_score'] = 0
    stream.mutables['player2_name'] = p2_name
    stream.mutables['player2_score'] = 0