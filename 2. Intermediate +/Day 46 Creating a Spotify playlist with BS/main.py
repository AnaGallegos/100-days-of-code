from datetime import datetime
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import requests, spotipy

def make_soup(billboard_url):
    response = requests.get(website)
    music_site = response.text
    soup = BeautifulSoup(music_site, 'html.parser')
    # Get all titles (nested in a h3 tag)
    song_tags = soup.find_all(name='h3', class_="a-no-trucate")
    #  Iterate through tags and put it in a list
    song_names = [song.getText().strip() for song in song_tags]
    return(song_names)

def create_playlist():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://localhost:8888/callback",
            client_id='ac9c0b8a69454c049e1d59adc9fccf91',
            client_secret='759ad10821584bd6952234b285c078fa',
            username='kagurart',
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]

    # Searching Spotify for songs by title
    song_uris = []
    year = date.split("-")[0]
    for song in song_list:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    # Creating a new private playlist in Spotify
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    print(playlist)

    # Adding songs found into the new playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


# while True:
#     date = input('Wich year do you want to traveel to? Type the date in this format YYYY-MM-DD: ')
#     try:
#         datetime.strptime(date, '%Y-%m-%d')
#         break
#     except ValueError:
#         print("Error: Date format invalid")


date = '2017-11-09'
website = f'https://www.billboard.com/charts/hot-100/{date}'
song_list = make_soup(website)
create_playlist()