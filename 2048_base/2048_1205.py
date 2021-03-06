#-*- coding:utf-8 -*-

import curses
from random import randrange, choice
from collections import defaultdict
# 引入3个扩展包

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
actions_dict = dict(zip(letter_codes, actions * 2))
# 创建我们将要用的键盘输入字典，这个字典将在后边通过第18行的
# keyboard.getch()
# 而这个方法被封装成一个函数，调用函数以实现该方法。

def get_user_action(keyboard):
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]
# 键盘输入以匹配字典的方法

def transpose(field):
    return [list(row) for row in zip(*field)]
# 矩阵转置，
# 这是一个数学方法，如望详细了解，请先了解矩阵
# 对于初学者，比较推荐暂时忽略。

def invert(field):
    return [row[::-1] for row in field]
# 矩阵逆转，同上

class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = 2048
        self.score = 0
        self.highscore = 0
        self.reset()
    # 定义类的__init__方法，为初始化方法

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()
    # 重置方法，虽然命名为reset，但是初始化也同样使用该方法。
    # 如果你觉得命名为set更合适，请改为set。
    # 这个方法中使用了spawn()函数，这个函数放在了后边，
    # spawn()函数的功能是生成新的数字，reset()需要生成两次。


    def move(self, direction):
    # 最重要的3个函数之一
        def move_row_left(row):
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            return tighten(merge(tighten(row)))
        #这里可以有不同的写法，就是tighten一次，merge一次。在merge的时候没必要加0了。
        # 欢迎大家把好的方法发给我，谢谢。http://www.cnblogs.com/danjawwi/
        # def merge(row):
        #     pair = False
        #     new_row = []
        #     for i in range(len(row)):
        #         if pair:
        #             new_row.append(2 * row[i])
        #             self.score += 2 * row[i]
        #             pair = False
        #         else:
        #             if i + 1 < len(row) and row[i] == row[i + 1]:
        #                 pair = True
        #             else:
        #                 new_row.append(row[i])
        #     new_row += [0 for j in range(len(row) - len(new_row))]
        #     return new_row
        #
        # return merge(tighten(row))

        moves = {}
        moves['Left']  = lambda field:                              \
                [move_row_left(row) for row in field]
        moves['Right'] = lambda field:                              \
                invert(moves['Left'](invert(field)))
        moves['Up']    = lambda field:                              \
                transpose(moves['Left'](transpose(field)))
        moves['Down']  = lambda field:                              \
                transpose(moves['Right'](transpose(field)))
        # 这里把row的迭代放在了方法外边，在对应字典值这里实现了。也可以放在方法里边


        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)
    #判断是否赢

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)
    # 判断是否输

    def draw(self, screen):
    # 最重要的3个函数之一
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'
        def cast(string):
            screen.addstr(string + '\n')

        def draw_hor_separator():
            line = '+' + ('+------' * self.width + '+')[1:]
            #不明白为什么这里要这样写
            #直接line = '+------' * self.width + '+' 不行吗？
            #http://www.cnblogs.com/danjawwi/

            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1
            #这里我也不明白，直接根据self.height输出不就行了？

        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')
            #用到了join 和 format这两种方法。
        screen.clear()
        cast('SCORE: ' + str(self.score))
        if 0 != self.highscore:
            cast('HGHSCORE: ' + str(self.highscore))
        for row in self.field:
            draw_hor_separator()
            draw_row(row)
        draw_hor_separator()
        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)

    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element
        #迭代器既可以根据层级来进行迭代，也可以在同层中迭代两次

    def move_is_possible(self, direction):
    # 最重要的3个函数之一
        def row_is_left_movable(row):
            def change(i):
                if row[i] == 0 and row[i + 1] != 0:
                # 这里是不是在说None != 0 ？
                    return True
                if row[i] != 0 and row[i + 1] == row[i]:
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))

        check = {}
        check['Left']  = lambda field:                              \
                any(row_is_left_movable(row) for row in field)

        check['Right'] = lambda field:                              \
                 check['Left'](invert(field))

        check['Up']    = lambda field:                              \
                check['Left'](transpose(field))

        check['Down']  = lambda field:                              \
                check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False

def main(stdscr):
    def init():
        game_field.reset()
        return 'Game'

    def not_game(state):
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        responses = defaultdict(lambda: state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]

    def game():
        game_field.draw(stdscr)
        action = get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'


    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
        }

    curses.use_default_colors()
    game_field = GameField(win=32)

    state = 'Init'

    while state != 'Exit':
        state = state_actions[state]()

curses.wrapper(main)
