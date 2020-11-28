import config
import pprint
import lyricsgenius
import spotipy
from spotipy.oauth2 import SpotifyOAuth


scope = "user-library-read, user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

info = sp.current_playback()
# pprint.clea(info)
pprint.pprint(info["item"]["album"]["artists"][0]["name"])
spotify_artist = info["item"]["album"]["artists"][0]["name"]
spotify_song = info["item"]["album"]["name"]
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

# sp.current_playback(market=None, additional_types=None)

genius = lyricsgenius.Genius(config.genius_token)
user_artist = spotify_artist

artist = genius.search_artist(""+ user_artist +"", max_songs=3, sort="title")

# print(artist.songs)
song = artist.song(spotify_song)
# or:
# song = genius.search_song("To You", artist.name)
print(song.lyrics)

