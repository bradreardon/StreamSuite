import os
from menus import Menu, MenuItem
from utils import ei_update_tournament_name, get_callback, ei_update_event_name, mi_update_round, \
    ps_update_player1_score, ps_update_player2_score, ps_update_player1_name, ps_update_player2_name, \
    ps_reset_players

__author__ = 'bradreardon'


MUTABLES_PATH = 'values'

class FileProxyDict(dict):
    def __setitem__(self, key, value):
        super(FileProxyDict, self).__setitem__(key, value)
        with open('{path}/{name}.txt'.format(path=MUTABLES_PATH, name=key), 'w+') as f:
            f.write(str(value))

    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).iteritems():
            self[k] = v

class StreamSuite(object):
    def __init__(self, tournament, event, match_round):
        self.mutables = FileProxyDict()
        self.mutables.update({
            'tournament': tournament,
            'event': event,
            'match_round': match_round,
            'player1_name': 'Player 1',
            'player1_score': 0,
            'player2_name': 'Player 2',
            'player2_score': 0
        })

    def run(self, menu):
        """
        :param Menu menu: The Menu to be displayed when StreamSuite starts.
        """

        print "StreamSuite running..."
        menu.show()


if __name__ == "__main__":
    if not os.path.exists(MUTABLES_PATH):
        os.makedirs(MUTABLES_PATH)

    t = raw_input("Tournament Name: ")
    e = raw_input("Event Name: ")
    r = raw_input("Current Round: ")

    app = StreamSuite(t, e, r)
    print  # Newline never hurt no one

    app.run(Menu('Main Menu', [
        Menu('Event Information', [
            MenuItem('"<new_name>" - Updates tournament name', get_callback(app, ei_update_tournament_name)),
            MenuItem('"<new_name>" - Updates event name', get_callback(app, ei_update_event_name)),
        ]).as_menu_item(),
        Menu('Match Information', [
            MenuItem('"<new_round>" - Updates round', get_callback(app, mi_update_round)),
        ]).as_menu_item(),
        Menu('Players and Scores', [
            MenuItem('<+/-> - Increment or decrement Player 1\'s score', get_callback(app, ps_update_player1_score)),
            MenuItem('<+/-> - Increment or decrement Player 2\'s score', get_callback(app, ps_update_player2_score)),
            MenuItem('"<new_name>" - Updates Player 1\'s name', get_callback(app, ps_update_player1_name)),
            MenuItem('"<new_name>" - Updates Player 2\'s name', get_callback(app, ps_update_player2_name)),
            MenuItem('"<player_1_name>" "<player_2_name>" - Resets scores to zero with new players', get_callback(app, ps_reset_players)),
        ]).as_menu_item(),
    ], is_main_menu=True))
