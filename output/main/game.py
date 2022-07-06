import curses
import time

import loaddata


def display_result(window, wpm, best):
    window.clear()
    window.addstr(0, 0, f"WPM: {wpm}")
    window.addstr(1, 0, f"BEST: {best}")
    window.refresh()
    while True:
        if window.getkey() == '\t':
            return


def display(window, target, current, wpm=0):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    WHITE = curses.color_pair(1)
    RED = curses.color_pair(2)
    GREEN = curses.color_pair(3)
    window.clear()
    window.addstr(0, 0, target, WHITE)
    window.addstr(2, 0, f"WPM: {wpm}")
    for i, char in enumerate(current):
        true_val = target[i]

        if char == true_val:
            color = GREEN
        else:
            color = RED
            char = true_val

        window.addstr(0, i, char, color)
    window.refresh()


def WPM_test(window):
    target_text = loaddata.rand_sentence()
    current_text = []
    wpm = 0
    start_time = time.time()
    window.nodelay(True)
    while True:
        wpm = round((len(current_text) / (max(time.time() - start_time, 1) / 60))/5)
        display(window, target_text, current_text, wpm)

        if len(current_text) == len(target_text):
            window.nodelay(False)
            break
        try:
            char = window.getkey()
        except:
            continue
        if char in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif char == '\t':
            window.nodelay(False)
            return
        else:
            current_text.append(char)

    if loaddata.get_best() < wpm:
        loaddata.set_best(wpm)
    display_result(window, wpm, loaddata.get_best())
