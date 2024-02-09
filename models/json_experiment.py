#!/usr/bin/python3
import json

filename = 'test.txt'
with open(filename, 'r', encoding = 'utf-8') as f:
    my_data = json.loads(f.read())
    
print(my_data['people'][0]['name'])
