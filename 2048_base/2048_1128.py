import curses
from collections import defaultdict
from random import randrange,choice

letter_codes = [ord(char) for char in 'WASDRQwasdrq']
actions = ['UP','Left','Down','Right','Restart','Quit']
actions_dict = dict(zip(letter_codes,actions * 2))  ###

def transpose(field):
    return list(row for row in zip(*field))

def invert(field):
    return list(row[::-1] for row in field)

def get_user_action(screen):
    char = 'N'
    while char not in actions_dict:
        char = screen.getch()  ####
    return actions_dict[char]####

class Gamefield(object):
    def __init__(self,width = 4,height = 4,win = 2048):
        self.width = width
        self.height = height
        self.win_value = win
        self.highscore = 0
        self.score = 0
        self.reset()

    def reset(self):
        if self.score >self.highscore:
            self.highscore =self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)] ####
        self.spawn()
        self.spawn()

    def draw(self,screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'

        def cast(str):
            screen.stradd(str + '\n')

        line =  ['*------' for i in range(self.width)]  + '|'
        def draw_row(row):
            cast(''.join('|{: ^5}'.format(i) if row(i) != 0 else '|     ' for i in row) + '|')

        screen.clear()
        if 0 != self.highscore:
            cast('HGHSCORE: ' + str(self.highscore))
        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)

        row = []
        for row in self.field:
            cast(line)
            draw_row(row)

    def move(self,direction):
        def move_left(field):
            def tighten(field):
                new_row = []
                def ti_row(row):
                    for i in range(row):
                        if i != 0:
                            new_row.append(i)
                    return new_row
                return list(ti_row(row) for row in field)

            def merge(field):
                def merge_row(row):
                    pair = False
                    new_row = []
                    for i in row:
                        if not pair:
                            if row(i) == row(i+1):
                                new_row.append(row(i))
                                pair = True
                            else:
                                new_row.append(row(i))
                        else:
                            pair = False
                    return list(new_row +list(0 for i in range(len(row) - len(new_row))))
                return list(merge_row(row) for row in field)

            return merge(tighten(field))

        move_dict = {}
        move_dict['Left'] = tighten(merge(self.field))
        move_dict['Right'] = invert(tighten(merge(invert(self.field))))
        move_dict['Up'] = transpose(tighten(merge(transpose(self.field))))
        move_dict['Down'] = transpose(move_dict['Right'](transpose(self.field)))

        if direction in move_dict:
            if self.move_is_possible(direction):
                self.field = move_dict[direction]()
                self.spawn()
                return True
            else:
                return False

    def move_is_possible(self,direction):
        def move_left_possible(field):
            def only_one(row):
                for i in randrange(len(row)):
                    if row(i) == 0 and row(i+1) != 0:
                        return True
                    if row(i) == row(i+1):
                        return True
                return False
            return any(only_one(row) for row in field)

        poss_dict = {}
        poss_dict['Left'] = move_left_possible(self.field)
        poss_dict['Up'] = poss_dict['Left'](transpose(self.field))
        poss_dict['Right'] = poss_dict['Left'](invert(self.field))
        poss_dict['Down'] = poss_dict['Right'](transpose(self.field))

        if direction in poss_dict:
            return poss_dict[direction]

    def is_win(self):
        return any(any(i >=self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(dir) for dir in actions)

    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i,j) = choice(list((i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0))
        self.field[i][j] = new_element

def main(stdscr):
    stdscr.use_default_colors()
    game_field = Gamefield(win = 32)

    def init():
        game_field.reset()
        return 'Game'

    def game():
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        if action == 'Quit':
            return 'Exit'
        if action == 'Restart':
            return 'Init'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'


    def not_game(state):
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        response = defaultdict(lambda : state)
        response['Restart'],response['Quit'] = 'Init' , 'Exit'
        return response[action]

    state = 'Init'
    state_dic = {}
    state_dic['Init'] = init
    state_dic['Game'] = game
    state_dic['Win'] = lambda :not_game('Win')
    state_dic['Gameover'] = lambda :not_game('Gameover')

    while state == 'Exit':
        state = state_dic[state]()

curses.wrapper(main)