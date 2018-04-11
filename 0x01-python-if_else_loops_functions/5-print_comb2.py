#!/usr/bin/python3
for x in range(0, 100):
    if x != 99:  # end here so no comma
        print("{:02d}, ".format(x), end="")  # no new line
print("{:d}".format(x))  # must be out of for loop because x is 99 after exit
