#!/usr/bin/python3
'''Get information about an employee's TODO list from a REST API
    (https://jsonplaceholder.typicode.com/), given the employee's ID,
    and export it in CSV format
'''
import csv
import requests
import sys


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    todos = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                employee_id))
    todos = todos.json()
    employees = requests.get('https://jsonplaceholder.typicode.com/users')
    employee_username = employees.json()[employee_id - 1].get('username')
    todos_list = []

    for todo in todos:
        inner_list = []
        inner_list.append(todo.get('userId'))
        inner_list.append(employee_username)
        inner_list.append(todo.get('completed'))
        inner_list.append(todo.get('title'))
        todos_list.append(inner_list)

    with open('{}.csv'.format(employee_id), mode='w') as employee_file:
        employee_writer = csv.writer(
                employee_file, delimiter=',', quotechar='"',
                quoting=csv.QUOTE_ALL)

        for item in todos_list:
            employee_writer.writerow(item)
