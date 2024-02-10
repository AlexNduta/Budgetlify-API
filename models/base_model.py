#!/usr/bin/python3

from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel, ValidationError
from random import randrange
from typing import List
import uuid

app = FastAPI()

filename = 'storage.txt'


def expense_file_reader(filename) -> List[dict]:
    """ Helper function that Reads a file and returns a list of lines """
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        if not isinstance (data, (list, dict)):
            raise ValueError("Inavalid JSON format. Top-level list must be either a list or an object")
        if isinstance(data, dict):
            expenses = data.get("expenses", [])
        else: 
            expenses = data

        return expenses
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def expense_file_writer(expenses: List[dict]):
    """ writes Posted expenses to the storage file"""
    with open(filename, "a") as f:
        json.dump(expenses, f, indent =4)



@app.get("/Budgetlify/expenses")
def get_expenses():
    """ get a list of all our expenses saved someehere in the file/DB"""
    expenses = expense_file_reader(filename)

    return expenses


@app.post("/Budgetlify/expenses")
def post_expense(new_expense : dict):
    """ Creates a post and sends data to the URL provided 
        - post:
                category: food
                date:
                amount:
                id: auto provided
    """
    expenses = expense_file_reader(filename)
    try:
        #  add Id if its not provided
        if 'id' not in new_expense:
            new_expense['id'] = randrange(0, 1200000)
        # append the new expense to the existing file
        expenses.append({**new_expense})
        print(type(new_expense))
        expense_file_writer(new_expense)
        print(type(expenses))
        return new_expense
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occured : {}".format(e))
