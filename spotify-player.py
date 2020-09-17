import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import pprint

with open('settings.json') as f:
    js = json.load(f)

client_id = js["ID"]
client_secret = js["SECRET"]
play_auth = js["AUTH"]
play_device_id = js["DEVICE"]

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp2 = spotipy.Spotify(auth=play_auth)


while True:
    search_word = input("Word > ")

    songs = []
    for i in range(20):
        res = sp.search(q=search_word, limit=50, offset=50*i, type='track', market='JP')
        # pprint.pprint(res['tracks']['items'][0])

        for track in res['tracks']['items']:
            al = track['album']['name']
            ar =  ""
            for art in track['artists']:
                ar += art['name']
            tr = track['name']
            songs.append((f"{tr} / {ar} - {al}", track["popularity"], track["uri"]))

    songs.sort(key=lambda x : x[1] * -1)

    for i in range(200):
        print(f"{i}:{songs[i]}")



    ipt = ""
    while ipt != "exit":
        ipt = input("No > ")
        try:
            no = int(ipt)
        except:
            continue
        print(f"{songs[no][0]} URI: {songs[no][2]}")
        sp2.start_playback(device_id = play_device_id, uris = [songs[no][2]])

