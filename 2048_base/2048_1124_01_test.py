from random import randrange, choice
from collections import defaultdict
import curses

letter_code = [ord(chr) for chr in 'WASDRQwasdrq']
actions = ['Up','Left','Down','Right','Reset','Quit']
action_dict = dict(zip(letter_code,actions * 2))

def get_user_action(keyboard):
    char = 'Not'
    while char not in action_dict:
        char = keyboard.getch()
    return action_dict[char]

def move_left_possible(row):
    pass

check = {}
check['Left'] = lambda field: any(move_left_possible(row) for row in field)