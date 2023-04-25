#!/usr/bin/python3
'''Get information about an employee's TODO list from a REST API
    (https://jsonplaceholder.typicode.com/), given the employee's ID,
    and export it in JSON format
'''
import json
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
    todos_dict = {}
    inner_list = []

    for todo in todos:
        inner_dict = {}
        inner_dict['task'] = todo.get('title')
        inner_dict['completed'] = todo.get('completed')
        inner_dict['username'] = employee_username
        inner_list.append(inner_dict)

    todos_dict['{}'.format(employee_id)] = inner_list

    with open('{}.json'.format(employee_id), mode='w') as employee_file:
        json.dump(todos_dict, employee_file)
