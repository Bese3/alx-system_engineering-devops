#!/usr/bin/python3
"""exporting api from third party to a csv file"""
import json
import requests


"""
The code block starting with `if __name__ == '__main__':`
is the main entry point of the script. It is executed when
the script is run directly (not imported as a module).
"""
if __name__ == '__main__':
    url = F"https://jsonplaceholder.typicode.com/users/"
    to_do = "/todos"
    json_out = {}
    with requests.get(url) as response:
        for i in response.json():
            url = url + str(i['id']) + to_do
            with requests.get(url) as todo_response:
                todo_response = todo_response.json()
                for j in todo_response:
                    del j['userId']
                    del j['id']
                    j['task'] = j['title']
                    del j['title']
                    j['username'] = i['username']
                json_out[str(i['id'])] = todo_response
            url = F"https://jsonplaceholder.typicode.com/users/"
        with open("todo_all_employees.json", "w", encoding="utf-8") as file:
            json.dump(json_out, file)
