import curses

import loaddata
from game import WPM_test

if loaddata.get_username() == None: loaddata.set_username(input("username: "))


def main(window):

    while True:
        WPM_test(window)


curses.wrapper(main)
