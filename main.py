import requests
import config
import pprint
import lyricsgenius
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# from PIL import ImageTk,Image  

scope = "user-library-read, user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth( scope=scope,
                                                client_id=config.SPOTIPY_CLIENT_ID,
                                                client_secret=config.SPOTIPY_CLIENT_SECRET,
                                                redirect_uri=config.SPOTIPY_REDIRECT_URI))

info = sp.current_playback()
# playback_state = info["is_playing"]
# if playback_state == True:
# print(info)
# pprint.pprint(info["item"]["album"]["images"][0]["url"])
# spotify_artist = info["item"]["album"]["artists"][0]["name"]
spotify_artist = info["item"]["artists"][0]["name"]
spotify_album = info["item"]["album"]["name"]
spotify_song = info["item"]["name"]
genius = lyricsgenius.Genius(config.genius_token)
# print(info["item"]["artists"][0]["name"])
# user_artist = spotify_artist
song = genius.search_song(spotify_song, spotify_artist)

album_image = requests.get(info["item"]["album"]["images"][0]["url"])
with open( spotify_album+".jpg", "wb") as f:
    f.write(album_image.content)
print(song.lyrics)