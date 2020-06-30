#!/usr/local/opt/python/bin/python3.7

import sys, os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SCOPES = 'user-read-playback-state,user-modify-playback-state'
REDIRECT_URI = 'http://localhost:8888/callback'
CONFIG_PATH = os.getenv("HOME") + '/.config/ax/config.txt'
CACHE_PATH = os.getenv("HOME") + '/.config/ax/cache.json'

def auth_sp():
    try:
        client_id, client_secret, username = [x.rstrip() for x in open(CONFIG_PATH, 'r').readlines()]
    except:
        print("Please run `ax auth` to setup authentication")
        sys.exit()
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id,
            client_secret,
            REDIRECT_URI,
            scope=SCOPES,
            cache_path=CACHE_PATH
        )
    )
    return sp

def setup_auth():
    print("Welcome to AX!")
    print("You can find your Spotify username at https://www.spotify.com/us/account/overview/")
    print("You can set up a Spotify app at https://developer.spotify.com/dashboard/applications")
    print("Add `http://localhost:8888/callback` as a callback to the app.")
    print("If you've setup https://github.com/Rigellute/spotify-tui before, you can use credentials and the callback from that app")
    print("Your secrets will be stored in " + CONFIG_PATH)
    username = input("Spotify Username: ")
    client_id = input("Spotify App Client ID: ")
    client_secret = input("Spotify App Client Secret: ")

    try:
        os.mkdir("/".join(CONFIG_PATH.split("/")[:-1]))
    except FileExistsError:
        pass
    f = open(CONFIG_PATH, "w+")
    f.write("{}\n".format(client_id))
    f.write("{}\n".format(client_secret))
    f.write("{}\n".format(username))
    f.close()

if len(sys.argv) > 1:
    if sys.argv[1] == "auth":
        setup_auth()
    else:
        sp = auth_sp()
        os.system(" ".join(sys.argv[1:]))
        if sp.current_playback() == None or sp.current_playback()['is_playing'] == False:
            sp.start_playback()
        else:
            sp.pause_playback()
else:
    print("Usage: ax {{COMMAND}}")
    sys.exit()
