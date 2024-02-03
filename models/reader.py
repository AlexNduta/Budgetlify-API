#!/usr/bin/python3
filename = 'storage.txt'

with open(filename, 'r') as f:
    file_content = f.read()
    for item in file_content:
        print(item)
