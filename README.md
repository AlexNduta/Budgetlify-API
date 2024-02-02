# Budgetlify
- This is a budgeting app that enables you to track your regular spending, savings

Dir:
`API`: This is the backend section of the app
    - Queries  the DB and provides the
## Endpoints
    Expense management
| method | endpoint | purpose |
|--------| :-------:|--------:|
| POST | http://[endpoint]/api/v1.0/expense | create a new expense |
| GET | http://[endpoint]/api/v1.0/expense | get a list of all expenses |
| GET | http://[endpoint]/api/v1.0/expenses{expense ID} | get a specific expense |
| PUT | http://[endpoint]/api/v1.0/expenses{expense ID} |  update an existing expense|
| DELETE | http://[endpoint]/api/v1.0/expenses{expense ID} | delete a specific expense | 
|   category management |
| POST | http://[endpoint]/api/v1.0/categories | create categories |
| GET | http://[endpoint]/api/v1.0/categories | get a list of all categories
|      Monthly Report |
| GET | http://[endpoint]/api/v1.0/reports/{year}/{month} | Get reports for a specific month |
| User Management |
| GET | http://[endpoint]/api/v1.0/profile | Get info of an authenticated user |
| PUT | http://[endpoint]/api/v1.0/profile | update a user |

| PUT | http://[endpoint]/api/v1.0/user | creates a new user |
| POST | http://[endpoint]/api/v1.0/Login | login a user |

   
`APP`: frontend android app for the user 
        stack:
                - Android
                - Kotlin
                - JetpakCompose

