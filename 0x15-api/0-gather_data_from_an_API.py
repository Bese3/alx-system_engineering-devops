#!/usr/bin/python3
"""reading api from third party"""
import requests
from sys import argv

"""
The code block starting with `if __name__ == '__main__':`
is the main entry point of the script. It is executed when
the script is run directly (not imported as a module).
"""
if __name__ == '__main__':
    url = F"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    to_do = "/todos"
    name = ""
    with requests.get(url) as response:
        name = response.json()['name']
    url = url + to_do
    task_completed = 0
    with requests.get(url) as response:
        response = response.json()
        for i in response:
            if i['completed'] is True:
                task_completed += 1
        print("Employee {} is done with tasks({}/{}):"
              .format(name, task_completed, len(response)))
        for i in response:
            if i['completed'] is True:
                print(F"\t {i['title']}")
