import curses
from random import randrange, choice  # generate and place new tile
from collections import defaultdict
#-------这段没问题--------

#定义按键并将asc码转换为十进制整数
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
# ord是一个build_in_function
#这个表达式本身是一个列表生成器，作用是把这些输入的asc码转化为十进制整数。
#也就是说我的键盘输入为asc码？？？

#定义用户的行为
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']

#將按键与用户行为关联 形成dict
actions_dict = dict(zip(letter_codes, actions * 2))
#原来没有想到过list也能* 2
#zip就是将两个list 的对应元素组合成tuple
#dict tuple 本身就是一个方法，就是见tuple里边的元素如果是tuple的话，改成对应关系。

def transpose(field):
    return [list(r) for r in zip(*field)]
    # or return list(map(list,list(zip(field))))

def invert(field):
    return [row[::-1] for row in field]
    # new_field =[]
    # for row in field:
    #     new_row = row[::-1]
    #     new_field.append(new_row)
    # return new_field



def main(sdrscr):
    state_actions = {
        'Init':init,
        'GAME':game,
        'Win':lambda :not_game('Win'),
        'Gameover':lambda :not_game('Gameover')

    }
    #现在给我感觉前边的这些''都像是索引
    state = 'Init'
    #开始时候的状态

    while state != 'Exit':
        state = state_actions[state]()

    def init():
        return 'Game'

    def game():
        #画出当前的棋盘状态
        #得到用户输入的action
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        #移动了，
            if 胜利了:
                return 'Win'
            if 失败了:
                return 'Gameover'
        return 'Game'

    def not_game(state):
        #画出Win or Gameover 的界面
        #读action，看是Restart 还是Exit
        response = defaultdict(list)
        response['Restart'],response['Exit']='Init','Exit'
        return response[action]

def get_user_action(keyboard):
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]
#这个是获得获得用户输入然后转成action，但是怎么输入的没说清

class GameField(keyboard):
    # this is mean initialization
    def __init__(self,height=4,width=4,win=2048):
        self.height=height
        self.width=width
        self.win_value=win
        self.score=0
        self.highscore=0
        self.reset()

    # 初始化棋盘的内容
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        # why we need set score = 0 here
        self.field = [[0 for i in range(self.width) for j in range(self.height)]]
        # this is a kind of list's high function
        self.spawn()
        self.spawn()
    # reset field

    def move_is_possiable(self,direction):
        def row_is_left_movable(row):
            def change(i):
                if row[i] == 0 and row[i+1] !=0:
                    return True
                if row[i]==row[i+1]:
                    return True
                else:
                    return False
            return any(change(i) for i in range(len(row)-1))

        check = {}
        check['left'] = lambda field:any(row_is_left_movable(row) for row in field)
        check['right'] = lambda field:any(check['left'](invert(field)))
        check['up'] = lambda field:any(check['left'](transpose(field)))
        check['down'] = lambda field:any(check['right'](transpose(field)))

        if direction in check:
            return check[direction](self.field)
        else:
            return False

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return any(self.move_is_possiable(direction) for direction in actions)

    def spawn(self):
        new_element = 4 if randrange(100)>89 else 2
        (i,j)=((i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] != 0)
        self.field[i][j]=new_element

    def draw(self,screen):
        help_string1='(W)Up (S)Down (A)Left (D)Right'
        help_string2='     (R)Restart (Q)Exit'
        win_string='          YOU WIN!'
        gameover_string='           GAME OVER'
        def cast(string):
            screen.addstr(string + '\n')

        def draw_hor_separator():
            line = '+' + ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda :line)
            if not hasattr(draw_hor_separator,'counter'):
                draw_hor_separator.counter=0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

        def draw_row(row):
            cast(''.join('|{: ^5}'.format(num) if num > 0 else '|     ' for num in row))

        screen.clear()
        # screen.clear() = stdscr.clear()
        cast('SCORE:' + str(self.score))
        if 0 != self.highscore:
            print('HIGHSCORE:' + str(self.highscore))
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

    def move(self,direction):

        moves = {}
        moves['left'] = lambda field: [move_row_left(row) for row in field]
        moves['right'] = lambda field: [invert(moves['left'](invert(field)))]
        moves['up'] = lambda field: [transpose(moves['left'](transpose(field)))]
        moves['down'] = lambda field: [transpose(moves['right'](transpose(field)))]

        def move_row_left(row):
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [j for j in range(len(row)-len(new_row))]
                return  new_row

            def merge(row):
                new_row= []
                # if_pair 的用处是判断我和前一个数值是否匹配
                # this pair is not only main equal ,
                # there are a,b,c
                # if b == c and a != b
                # then b pair c
                if_pair = 0
                # 0 mains not pair
                # first if you pair with the forward number
                    # new_row.append(row[i]*2)
                    #you don't care if your pair with the next number or not
                # if you not pair with the forward number
                    #if you pair with the next number
                        # i position set 0
                        #set judgement = 1
                    # if not
                        #set i = row(i)

                # when i receive the judgement, it help me to determine the relationship with the forward number
                # when i change the judgement, it means to tell the relationship to the next number
                for i in range(len(row)):
                    if if_pair == 0:
                        if i + 1 < len(row) and row[i] == row[i+1]:
                            if_pair = 1
                            # set if_pair = 1 is for telling the next number that he pair with the forward number
                            new_row.append(0)
                        else :
                            new_row.append(row[i])
                            if_pair = 0
                    else:
                        new_row.append(row[i]*2)
                        if_pair = 0
                assert  len(new_row)==len(row)
                return new_row
            return tighten(merge(tighten(row)))
