#!/usr/bin/python3
from sys import argv
import os


save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file
filename = "add_item.json"

if not os.path.exists(filename):
        save_to_json_file([], filename)

args = load_from_json_file(filename)
for x in range(1, len(argv)):
    args.append(argv[x])
save_to_json_file(args, filename)
