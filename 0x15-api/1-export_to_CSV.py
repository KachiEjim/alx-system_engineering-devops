#!/usr/bin/python3
""" Python script that, using this REST API, for
a given employee ID, returns
information about his/her TODO list progress."""

import csv
import json
from sys import argv
import urllib
import urllib.request


def get_employee_tasks(employeeId):
    """ Get employee tasks """
    url_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        employeeId)
    url_users_name = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employeeId)
    response_todos = urllib.request.urlopen(url_todos).read()
    response_user = urllib.request.urlopen(url_users_name).read()
    data_todos = json.loads(response_todos)
    data_user = json.loads(response_user)

    filename = f"{employeeId}.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

    # Write rows to the CSV file
    for task in data_todos:
        userId = task.get("userId")
        name = data_user.get("name")
        title = task.get("title")
        writer.writerow([userId, name, title])


if __name__ == "__main__":
    id = argv[1]
    get_employee_tasks(id)
