#!/usr/bin/python3
'''Get information about an employee's TODO list from a REST API
    (https://jsonplaceholder.typicode.com/), given the employee's ID
'''
import requests
import sys


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    todos = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                employee_id))
    todos = todos.json()
    employees = requests.get('https://jsonplaceholder.typicode.com/users')
    employee_name = employees.json()[employee_id - 1].get('name')
    completed = 0
    total = len(todos)
    completed_tasks = []

    for todo in todos:
        if todo.get('completed'):
            completed += 1
            completed_tasks.append(todo.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
        employee_name, completed, total))

    for task in completed_tasks:
        print('\t {}'.format(task))
