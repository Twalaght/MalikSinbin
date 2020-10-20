#!/usr/bin/python3

# Midnight Max Krump, Chill, Car Music, Max attack


import curses

menu = ['Home', 'Play', 'Scoreboard', 'Exit']


def print_menu(main, selected_row_idx):
    main.clear()
    h, w = main.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            main.attron(curses.color_pair(1))
            main.addstr(y, 0, row)
            main.attroff(curses.color_pair(1))
        else:
            main.addstr(y, 0, row)
    main.refresh()


def print_center(main, text):
    main.clear()
    h, w = main.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    main.addstr(y, x, text)
    main.refresh()


def main(main):


    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(main, current_row)

    while 1:
        key = main.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            print_center(main, "You selected '{}'".format(menu[current_row]))
            main.getch()
            # if user selected last row, exit the program
            if current_row == len(menu)-1:
                break

        print_menu(main, current_row)


curses.wrapper(main)
