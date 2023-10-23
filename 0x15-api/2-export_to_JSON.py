#!/usr/bin/python3
"""exporting api from third party to a csv file"""
import json
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
        name = response.json()['username']
    url = url + to_do
    task_completed = 0
    with requests.get(url) as response:
        response = response.json()
        for i in response:
            del i['userId']
            del i['id']
            i['task'] = i['title']
            del i['title']
            i['username'] = name
            if i['completed'] is True:
                task_completed += 1
        json_out = {argv[1]: response}
        # print(json_out)
        with open(argv[1] + ".json", "w", encoding="utf-8") as file:
            json.dump(json_out, file)
