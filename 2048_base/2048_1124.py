import curses
from random import randrange,choice
from collections import defaultdict

curses.wrapper(main)

letter_codes = [ord(chr) for chr in 'WASDRQwasdrq']
actions = ['Up','Left','Down','Right','Reset','Quit']
actions_dict = dict(zip(letter_codes,actions*2))

def get_user_action(keyboard):
    char = 'N'
    while char not in letter_codes:
        char = keyboard.getch()
    return actions_dict[char]

def transpose(field):
    return [list(row) for row in field]

def invert(field):
    return [row[::-1] for row in field]

class GameField(object):
    def __init__(self,win=2048,width=4,height=4):
        self.win_value = win
        self.height = height
        self.width = width
        self.heighscore = 0
        self.score = 0
        self.reset()

    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])

    def reset(self):
        if self.score > self.heighscore:
            self.heighscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()

def main(stdscr):
    state_actions = {
        'Init':init,
        'Game': game,
        'Win': lambda :not_game('Win'),
        'Gameover':lambda :not_game('Gameover')
        }

    curses.use_default_color()
    game_field= GameField(win = 32)

    state = 'Init'

    while state != 'Gameover':
        state = state_actions[state]()

    def init():
        game_field.reset()
        return 'Game'

    def not_game(state):
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        pass

    def game():
        game_field.draw(stdscr)





