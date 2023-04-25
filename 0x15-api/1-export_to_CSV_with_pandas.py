#!/usr/bin/python3
'''Get information about an employee's TODO list from a REST API
    (https://jsonplaceholder.typicode.com/), given the employee's ID
    and export it in CSV format
'''
import pandas
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
        todos_dict = {}
        todos_dict['user_id'] = todo.get('userId')
        todos_dict['username'] = employee_username
        todos_dict['task_completed'] = todo.get('completed')
        todos_dict['task_title'] = todo.get('title')
        todos_list.append(todos_list)

    columns = ['user_id', 'username', 'task_completed', 'task_title']
    employee_table = pandas.DataFrame(todos_list, columns=columns)

    employee_table.to_csv('{}.csv'.format(employee_id), index=False)
