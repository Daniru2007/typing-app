import curses

from game import WPM_test


def main(window):

    while True:
        WPM_test(window)


curses.wrapper(main)
