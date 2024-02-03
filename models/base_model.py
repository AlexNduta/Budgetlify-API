#!/usr/bin/python3

from fastapi import FastAPI
from uuid import uuid4
app = FastAPI()

filename = 'storage.txt'

def file_reader(filename):
    with open(filename, 'r') as f:
        file_content = f.read()
        print(file_content)
    return file_content


@app.get("/Budgetlify/expenses")
def get_expenses():
    """ get a list of all our expenses"""
    content = file_reader(filename)
    return content
