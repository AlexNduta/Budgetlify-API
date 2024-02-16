#!/usr/bin/python3

from fastapi import FastAPI, HTTPException, status
import json
from pydantic import BaseModel, ValidationError
from random import randrange
from typing import List
import uuid

app = FastAPI()

filename = 'storage.txt'

expense_array = []

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
        return {"message": "This is not an array"}


def expense_file_writer(expenses: List[dict]):
    """ Writes Posted expenses to the storage file"""
    try:
        with open(filename, "r") as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = []

    updated_data = existing_data + expenses

    with open(filename, "w") as f:
        json.dump(updated_data, f, indent=4)


@app.get("/Budgetlify/expenses")
def get_expenses():
    """ get a list of all our expenses saved someehere in the file/DB"""
    expenses = expense_file_reader(filename)
    return expenses


class Post(BaseModel):
    """ Verify that the inputed data is valid according to a our schema"""
    category: str
    date: str
    amount: int
    description: str

@app.post("/Budgetlify/expenses", status_code=status.HTTP_201_CREATED)
def post_expense(new_expense: Post):
    """ Creates a post and sends data to the URL provided 
        - new_post:
                category: food
                date:
                amount:
                id: auto provided
    """
   # expenses = expense_file_reader(filename)
    try:
         post_dict= new_expense.dict() # convert the post type to a dictionary
         # use the ID property to generate a random ID between 0 an a million
         post_dict['id'] = randrange(0, 1000000)

         #append the new expense sent by the user  to the existing file and pass it to the function to write it to a file
         expense_array.append(post_dict)
         expense_file_writer(expense_array)
         return {"Message": "Expense added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occured : {}".format(e))



def expense_finder(id: int):
    """Gets a list of expenses from from the function call"""
    expenses = expense_file_reader(filename)
    for expense in expenses:
        if expense['id'] == id:
            return expense
    return None


@app.get("/Budgetlify/expenses/{id}")
def get_single_item(id:int):
    """ gets a single item from the list of expenses with the specified ID"""
    found_expense = expense_finder(int(id))
    if found_expense:
        return found_expense
    else:
        raise HTTPException(status_code=404, detail="The item with the ID {} is not found".format(id) )

def index_finder(id:int):
    """ returns an index of the item from the list"""
    # call the function that returns a list
    list_of_expenses = expense_file_reader(filename)
    for index, element in enumerate(list_of_expenses):
        if element['id'] == id:
            return index

@app.delete("/Budgetlify/expenses/{id}")
def delete_a_single_item(id:int):
    """
    deletes an item specified by ID from the list
    """
    # get the list of items
    list_of_expenses = expense_file_reader(filename)
    # get the index of the item
    index_found = index_finder(int(id))
    #if item exists delete the item in specified index then open file and save changes to the file
    if index_found is not None:
        del list_of_expenses[index_found]
        with open(filename, "w") as f:
            json.dump(list_of_expenses, f, indent=4)
        return {"message":"Item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Expense not found")

    return {"message":"Item deleted successfully"}

