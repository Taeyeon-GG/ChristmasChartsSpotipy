import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

clientid = "22949a4241f04b96b18f30ac30cbe85e"
clientsecret = "b9c3dd783de149869963be243f3f8770" #developer.spotify.com

client_credentials_manager = SpotifyClientCredentials(clientid,clientsecret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = 'spotify:user:mbftvtzwr41ylpxadbipr7vo4:playlist:5Dy0JXCbGPQHQmgTkaT8s7'
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

results = sp.user_playlist(username, playlist_id)

x = json.loads(json.dumps(results))

for i in range(75):

    christmaswords = ["christmas","tree","snow","merry","xmas","cold","winter"]
    curstringprint = (str(i) + ". " + (x["tracks"]["items"][i]["track"]["name"]))
    curstringcompare = (x["tracks"]["items"][i]["track"]["name"]).lower()

    for j in christmaswords:
        if j in curstringcompare:
            print(curstringprint)
            break
