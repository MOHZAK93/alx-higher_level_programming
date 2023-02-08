#!/usr/bin/python3
"""Create Object module"""
import json
import sys
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


item_list = []
size = len(sys.argv)
i = 1
while i < size:
    item_list.append(sys.argv[i])
    i += 1

save_to_json_file(item_list, "add_item.json")
load_from_json_file("add_item.json")
