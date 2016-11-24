from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr.addstr('111111111111111')
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)