#!/usr/bin/python3
def main():
    from sys import argv

    argc = len(argv) - 1
    print("{} argument".format(argc), end="")
    if argc == 0:
        print("s.")
    elif argc == 1:
            print(":")
    else:
        print("s:")
    for x in range(1, len(argv)):
        print("{}: {}".format(x, argv[x]))
if __name__ == "__main__":
    main()
