import json
import random
from slackbot.bot import default_reply

cnt = 0

colors = {
    "Vo": "#e05ab4",
    "Da": "#59afe1",
    "Vi": "#e0e05a"
}

with open('idols.json') as f:
    idols = (json.load(f))["idols"]

@default_reply()
def default_func(msg):
    r = random.random()
    rare = "R"
    if r < 0.05:
        rare = "SSR"
    elif r < 0.21:
        rare = "SR"
    idol = random.choice(idols)

    print(f"Put [{rare}]{idol['name']}")

    attachments = [
    {
        'title': rare+idol["name"],
        'text': f'Unit: {idol["unit"]}, Type: {idol["type"]}',
        'color': colors[idol["type"]],
        'image_url': idol["url"]
    }]
    msg.send_webapi('', json.dumps(attachments))
