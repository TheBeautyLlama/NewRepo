#key d6b483fbdf547be34855aefc9f404b9e
#f"Clicks {clicks}"
import os
from urllib import response
import requests
import json
import re
from tkinter import * 
from tkinter import ttk

def api_key_check():
    global api_key
    #with open('api_key.txt', 'w') as f:

    try:
        file = open('api_key.txt')
    except IOError as e:
        with open("api_key.txt","w") as f:
            f.write(api_key_entry.get())
    else:
        with file:
            api_key_entry.insert(0, api_key)


    with open('api_key.txt', 'r') as f:
        api_key = f.read()

def click_button():
    global resp
    dataset_id = dataset_id_entry.get()
    global api_key
    #api_key = api_key_entry.get()
    print (f"https://apidata.mos.ru/v1/datasets/{dataset_id}")
    resp = requests.get(f"https://apidata.mos.ru/v1/datasets/{dataset_id}?api_key={api_key}")
    write_to_json(resp)

def write_to_json(resp):
    filename = "result.json"
    with open(filename, 'w') as f:
        json.dump(resp.text, f)
    print(resp.text)

def load_to_objects():
    global resp
    templates = json.loads(resp.text)
    print("\n" "\n" "\n" "\n")
    for section, commands in templates.items():
        with open('sw_templates.json', 'a') as f:
            if section == "FullDescription":
                with open("FullDescritpion.html","w") as i:
                    i.write(commands)
            f.write(f"\n")
            f.write(f"{section}: {commands} \n")
        print(f"{section}: {commands}")


#
global dataset_id
global api_key
global resp


root = Tk()
root.title("Some Programm :D")
root.geometry("300x200")

greeting = ttk.Label(text="Enter article ID")
greeting.pack(anchor=N)

dataset_id_entry = ttk.Entry()
dataset_id_entry.pack(anchor=N)

api_key_request = ttk.Label(text="Enter your API key")
api_key_request.pack(anchor=N)

api_key = str("")
api_key_entry = ttk.Entry()
api_key_entry.pack(anchor=N)
try:
    file = open('api_key.txt')
except IOError as e:
    print("")
else:
    with open('api_key.txt', 'r') as f:
        api_key = f.read()
        api_key_entry.insert(0, api_key)

find_button = ttk.Button(text="Find", command = click_button)
find_button.pack(anchor=N)

load_button = ttk.Button(text="Load", command = load_to_objects)
load_button.pack(anchor=N)

load_key_button = ttk.Button(text="Load API Key", command = api_key_check)
load_key_button.pack(anchor=N)
root.mainloop()

os.remove("sw_templates.json")



