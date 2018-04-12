#!/usr/bin/python3
def main():

    from sys import argv
    arguments = 0
    for x in range(1, len(argv)):
        arguments = arguments + int(argv[x])
    print(arguments)

if __name__ == "__main__":
    main()
