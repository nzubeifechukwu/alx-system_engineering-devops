#!/usr/bin/python3
'''Get information about all employees' TODO lists from a REST API
    (https://jsonplaceholder.typicode.com/) and export it in JSON format
'''
import json
import requests


if __name__ == '__main__':
    employee_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    employees = requests.get('https://jsonplaceholder.typicode.com/users')
    todos_dict = {}

    for i in employee_ids:
        todos = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                    i))
        username = employees.json()[i - 1].get('username')
        inner_list = []
        for todo in todos.json():
            inner_dict = {}
            inner_dict['username'] = username
            inner_dict['task'] = todo.get('title')
            inner_dict['completed'] = todo.get('completed')
            # inner_list = []
            inner_list.append(inner_dict)
        todos_dict[i] = inner_list

    with open('todo_all_employees.json', mode='w') as employee_file:
        json.dump(todos_dict, employee_file)
