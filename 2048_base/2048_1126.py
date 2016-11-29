import curses
from collections import defaultdict
from random import randrange,choice

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions = ['Up','Left','Down','Right','Restart','Quit']
actions_dict = dict(zip(letter_codes,actions*2))

def get_user_action(screen):
    action = 'N'
    while action not in actions_dict:
        action =screen.getch()
    return actions_dict[action]

def transport(list_2048):
    return [list(row) for row in zip(*list_2048)]

def invert(list_2048):
    return [row[::-1] for row in list_2048]

class Gamefield():
    def __init__(self,width = 4,height = 4,win = 2048):
        self.width = width
        self.height = height
        self.win_value = win
        self.score = 0
        self.heighscore = 0
        self.reset()

    def reset(self):
        self.field = [0 for i in range(self.width) for j in range(self.height)]
        self.spawn()
        self.spawn()

    def spawn(self):
        while True:
            i = choice(i for i in range(self.width - 1))
            j = choice(j for j in range(self.height - 1))
            new_element = 4 if choice(100) > 89 else 2
            if self.field[i][j] == 0:
                self.field[i][j] =new_element
                break

    def spawn2(self):
        new_element = 4 if choice(100) > 89 else 2
        (i,j)= choice([(i,j) for i in range(self.width - 1) for j in range(self.height -1) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    def move_is_possible(self,direction):
        def move_left_possible(row):
            def only_one(i):
                if row(i) == 0 and row(i+1) != 0:
                    return True
                if row(i) == row(i+1):
                    return True
                else:
                    return False
            return any(only_one(i) for i in range(len(row)-1))

        dic = {}
        dic['Left'] = lambda field: any(move_left_possible(row) for row in field)
        dic['Up']= lambda field:any(move_left_possible(row) for row in transport(field))
        dic['Right'] = lambda field:any(move_left_possible(row) for row in invert(field))
        dic['Down'] = lambda field:dic['Right'](transport(field))

        if direction in dic:
            return dic[direction](self.field)
        else:
            return False

    def move(self,direction):
        dir_dict = {}
        dir_dict['Left'] = lambda field: [move_left(row) for row in field]
        #There is to be a list generator
        dir_dict['Up'] = lambda field:transport(dir_dict['Left'](transport(field)))
        dir_dict['Right'] = lambda field:invert(dir_dict['Left'](invert(field)))
        dir_dict['Down'] = lambda field:transport(dir_dict['Right'](transport(field)))
        dir_dict['Right2'] = lambda field:invert(move_left(row) for row in (invert(field)))

        def move_left(row):
            def tighten(row):
                new_row = []
                for i in range(len(row) - 1):
                    if row(i) == 0:
                        pass
                    else:
                        new_row.append(row(i))
                return new_row

            def merge(row):
                new_row = []
                pair = False
                for i in range(len(row) - 1):
                    if pair:
                        pass
                    else:
                        if row(i) == row(i+1):
                            new_row.append(row(i) * 2)
                return new_row

            return tighten(merge(row))

        if direction in dir_dict:
            dir_dict[direction](self.field)
            return True
        else:
            return False

    def draw(self,screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'
        def cast(str):
            screen.addstr(str + '\n')
        def draw_hor_line():
            line = '*' + ('*------' *self.width + '*')[1:]
            cast(line)

        def draw_row(row):
            line = ''.join('|{: ^5}'.format(num) if num > 0 else '|     ' for num in row +'|')
            cast(line)

        screen.clear()
        cast('Score:' + str(self.score))
        if self.score > self.heighscore:
            self.heighscore = self.score
        for row in self.field:
            draw_hor_line()
            draw_row(row)
        draw_hor_line()

        if self.is_win():
            cast('you win')
        if self.is_gameover():
            cast('you lost')
        else:
            cast(help_string1)
        cast(help_string2)


    def is_win1(self,field):
        win_true = 0
        for row in field:
            for i in row:
                if i >= self.win_value:
                    win_true = 1
                else:
                    pass
        if win_true == 1:
            return True
        else:
            return False

    def is_gameover1(self,field):
        move_can = 1
        for dir in ['Up','Down','Left','Right']:
            if self.move_is_possible(dir):
                pass
            else:
                move_can = 0
        if move_can == 1:
            return False
        if move_can ==0:
            return True

    def is_win(self):
        return any(any(i>= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(action1) for action1 in ['Up','Down','Left','Right'])

def main(stdscr):
    curses.use_default_colors()
    game_field = Gamefield(win = 32)
    state = 'Init'

    def init():
        game_field.reset()
        return 'Game'

    def game():
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        if action == 'Restart':
            return 'Init'
        if action == 'Quit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    def not_game(state):
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        response =defaultdict(lambda :state)
        response['Restart'],response['Quit'] = 'Init'  , 'Exit'
        return  response[action]

    state_dict = {}
    state_dict['Game'] = game()
    state_dict['Init'] = init()
    state_dict['Win'] = lambda :not_game('Win')
    state_dict['Gameover'] =lambda :not_game('Gameover')

    while state != 'Exit':
        state = state_dict[state]()

curses.wrapper(main)