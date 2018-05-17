#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ This reads n lines of a text file (UTF8) and prints it to stdout.

    Args:
        filename - This is the name of the text file being read.

        nb_lines - This is the number of lines.

    """

    with open(filename, encoding="UTF8") as x:
        tracker = 0
        for text in x:
            print(text, end="")
            tracker = tracker + 1
            if tracker == nb_lines:
                break
