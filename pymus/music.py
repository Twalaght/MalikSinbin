#!/usr/bin/python3

from pathlib import Path
import os
import curses

songs = []
playlists = ["Max Atk", "Chillin", "Running", "Singing"]


# TODO - Change this to environmental vars
music_path = Path("/mnt/c/Users/Jono/Desktop/Music")
# print(music_path.exists())

for path, subdir, files in os.walk(music_path):
    for file in files:
        songs.append(list(os.path.splitext(file)[:2]))


# for song in songs:
#     dict[song] = [False] * 5


def print_menu(main, height, width, selected, start):
    main.clear()


    for i in range(height - 2):
        # TODO - Eventually splice this with playlist sels, not width
        title = songs[i + start][0]
        if len(title) > width / 2:
            title = title[:int(width / 2 - 3)] + "..."



        if i + start == selected:
            main.attron(curses.color_pair(1))
            main.addstr(i + 1, 1, title)
            main.attroff(curses.color_pair(1))
        else:
            main.addstr(i + 1, 1, title)


    # Print border
    main.addstr(0, 0, "╔" + "═" * (width - 2) + "╗")
    main.addstr(0, 2, "[Song title]")
    main.addstr(height - 1, 0, "╚" + "═" * (width - 2))

    for i in range(1, height - 1):
        main.addstr(i, 0, "║")
        main.addstr(i, width - 1, "║")

        # TODO
        # main.addstr(i, int(width / 2), "║")

    # TODO - Not really happy with this sytem yet
    for j in range(len(playlists)):
        main.addstr(0, width - 10 * (j + 1), "[" + playlists[j] + "]")

    main.addstr(0, width - 10 * (len(playlists) + 1) - 2, "[Playlists]")

    for i in range(height - 2):
        for j in range(len(playlists)):
            # TODO - IF ENTRY EXISTS
            main.addstr(i + 1, width - 10 * (j + 1), "[   X   ]")



    main.refresh()



# def print_center(main, text):
#     main.clear()
#     h, w = main.getmaxyx()
#     x = w//2 - len(text)//2
#     y = h//2
#     main.addstr(y, x, text)
#     main.refresh()



# Define the programs main loop to be run with curses
def main(main):
    # Turn off cursor blinking
    curses.curs_set(0)

    # TODO - Colour scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Get the height and width of the terminal
    term_h, term_w = main.getmaxyx()

    # TODO
    size = len(songs)
    if size  > term_h:
        size = term_h

    # TODO
    # specify the current selected row
    selected = 0
    # Specify the starting row
    start = 0


    # Print the menu initially
    print_menu(main, size, term_w, selected, 0)

    while True:
        # Get the users key presses
        key = main.getch()

        # Change the selected line based on key presses
        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(songs) - 1:
            selected += 1

        # Push the start line up or down as needed
        if selected < start:
            start -= 1
        elif selected - size >= start - 2:
            start += 1


        # elif key == curses.KEY_ENTER or key in [10, 13]:
        #     print_center(main, "You selected '{}'".format(menu[current_row]))
        #     main.getch()
        #     # if user selected last row, exit the program
        #     if current_row == len(menu)-1:
        #         break

        print_menu(main, size, term_w, selected, start)


# Run the main program loop with curses
curses.wrapper(main)
