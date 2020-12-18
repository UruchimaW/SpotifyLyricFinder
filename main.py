import config
import pprint
import lyricsgenius
import spotipy
from spotipy.oauth2 import SpotifyOAuth


scope = "user-library-read, user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth( scope=scope,
                                                client_id=config.SPOTIPY_CLIENT_ID,
                                                client_secret=config.SPOTIPY_CLIENT_SECRET,
                                                redirect_uri=config.SPOTIPY_REDIRECT_URI))

info = sp.current_playback()
# playback_state = info["is_playing"]
# if playback_state == True:
# print(info)
pprint.pprint(info)
spotify_artist = info["item"]["album"]["artists"][0]["name"]
spotify_song = info["item"]["name"]
genius = lyricsgenius.Genius(config.genius_token)
# user_artist = spotify_artist
song = genius.search_song(spotify_song, spotify_artist)
print(song.lyrics)

# else:
#     print("Nothing playing")

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

# artist = genius.search_artist(""+ user_artist +"", max_songs=3, sort="title")

# print(artist.songs)
# song = artist.song(spotify_song)
# or: