#!/usr/bin/python3

from fastapi import FastAPI
import json
from pydantic import BaseModel, ValidationError
from random import randrange

app = FastAPI()

filename = 'storage.txt'


def file_reader(filename):
    """ Helper function that Reads a file and returns a list of lines """
    with open(filename, "r") as f:
        return json.loads(f.read().strip())


@app.get("/Budgetlify/expenses")
def get_expenses():
    """ get a list of all our expenses saved someehere in the file/DB"""
    expenses = file_reader(filename)
    return expenses

class Expense(BaseModel):
    """ Validate the main expenses"""
    category:str
    date: str
    amount:int
    Id:int


@app.post("/Budgetlify/expenses")
def post_expense(new_post : Expense):
    """ Creates a post and sends data to the URL provided 
        - post:
                category: food
                date:
                amount:
                id: auto provided
    """
    try:
        new_post.dict() 
        new_post['Id'] = randrange(0, 120000000)
        expenses.append(new_post)
        return new_post.dict()
    except ValidationError as e:
        raise HTTException(status_code=400, detail=str(e))
