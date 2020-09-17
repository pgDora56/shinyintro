import os
import pprint
import json
import random

accept = False

colors = {
    "Vo": "#e05ab4",
    "Da": "#59afe1",
    "Vi": "#e0e05a"
}

with open('idols.json') as f:
    idols = (json.load(f))["idols"] # Insert 23 data

def pick(msg):
    global accept
    if not accept: 
        print("Not accept")
        return
    for i in range(5):
        pick_one(msg)
    accept = False

def pick_one(msg):
    global idols

    idolno = random.randrange(len(idols))
    idol = idols[idolno]

    print(f"{msg.user['real_name']} gets {idol['unit']} {idol['name']}")

    attachments = [
    {
        'title': idol['name'],
        'text': f"所属ユニット: {idol['unit']}",
        'color': colors[idol["type"]],
        'image_url': idol["url"]
    }]
    msg.send_webapi('', json.dumps(attachments))

def command():
    global accept
    ipt = input()
    print(f"Get input: {ipt}")
    if ipt == "a":
        accept = True
        print("Set accept")
    elif ipt == "d":
        accept = False
        print("Set deny")

