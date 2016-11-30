import curses
from random import randrange,choice
from collections import defaultdict

letter_code = [ord(char) for char in 'WASDRQwasdrq']
actions = ['Up','Left','Down','Right','Restart','Quit']
actions_dict = dict(zip(letter_code,actions*2))

def get_user_action(stdscr):
    char = 'N'
    while char not in actions_dict:
        char = stdscr.getch()
    return actions_dict[char]

def transpose(field):
    return list(list(row) for row in zip(*field))

def invert(field):
    return list(list(row) for row in field[::-1])

class Gamefield(object):
    def __init__(self,width = 4,height = 4,win = 2048):
        self.width = width
        self.height = height
        self.win_value = win
        self.score = 0
        self.highscore = 0
        self.reset()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in self.width] for j in self.height]
        self.spawn()
        self.spawn()

    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i,j)=((i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] ==0)
        self.field[i][j] = new_element

    def draw(self,screen):
        def cast(str):
            screen.addstr(str + '\n')

        line = ('*' + str('*-----'for i in range(self.width)) + '|')[1:]

        def draw_row(row):
            cast(''.join('|{: ^5}'.format(i) if i != 0 else '|    ' for i in row))




    def move(self,direction):
        def tighten(field):
            def tighten_row(row):
                new_row = []
                for i in row :
                    if i != 0:
                        new_row.append(i)
                    else:
                        pass
                return new_row
            return list(tighten_row(row) for row in field)

        def merge(field):
            def merge_row(row):
                new_row = []
                pair = False
                for i in range(len(row) - 1):
                    if not pair:
                        if row(i) == row(i+1):
                            new_row.append(row(i) * 2)
                            pair = True
                        else:
                            new_row.append(row(i))
                            pair = False
                    else:
                        pair = False
                new_row = new_row + [0 for i in range(len(row) - len(new_row))]
                return new_row
            return list(merge_row(row) for row in field)


        move_dict = {}
        move_dict['Left'] = merge(tighten(self.field))
        move_dict['Right'] = invert(move_dict['Left'](invert(self.field)))
        move_dict['Up'] = transpose(move_dict['Left'](transpose(self.field)))
        move_dict['Down'] = transpose(move_dict['Right'](transpose(self.field)))

        if direction in actions_dict:
            if self.movable(direction):
                self.field = move_dict[direction]
                self.spawn()
                return True
            else:
                return False



    def is_win(self):
        return any(self.field[i][j] >= self.win_value for i in range(self.width) for j in range(self.height))

    def is_gameover(self):
        return not any(self.movable(dir) for dir in actions_dict)

    def movable(self,direction):
        def movable_left(field):
            def only_one(row):
                return any(((row[i] == 0 and row[i+1] != 0) or (row(i) != 0 and row(i) == row(i+1))) for i in range(self.width))
            return any(only_one(row) for row in field)

        mv_dict = {}
        mv_dict['Left'] = movable_left(self.field)
        mv_dict['Right'] = mv_dict['Left'](invert(self.field))
        mv_dict['Up'] = mv_dict['Left'](transpose(self.field))
        mv_dict['Down'] = mv_dict['Right'](transpose(self.field))

        if direction in actions_dict:
            return mv_dict[direction]
        else:
            return False

def main(stdscr):
    game_field = Gamefield(win = 32)
    stdscr.use_default_colors()

    def init():
        game_field.reset()
        return 'Game'

    def game():
        game_field.draw()
        action = get_user_action(stdscr)
        if action == 'Restart':
            return 'Init'
        if action == 'Quit':
            return 'Gameover'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'


    def not_game(state):
        game_field.draw()
        action = get_user_action(stdscr)
        response = defaultdict(lambda :state)
        response['Restart'],response['Quit'] = 'Init' , 'Exit'
        return response[action]

    state = 'Init'
    state_dict = {}
    state_dict['Init'] = init
    state_dict['Game'] = game
    state_dict['Win'] = lambda :not_game('Win')
    state_dict['Gameover'] = lambda :not_game('Gameover')

    while state != 'Exit':
        state = state_dict[state]()

curses.wrapper(main)