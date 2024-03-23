import requests
import base64
from urllib.parse import urlparse
import os
from dotenv import load_dotenv


load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID") 
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

def authenticate_spotify():
    # Spotify URL for authentication
    auth_url = "https://accounts.spotify.com/api/token"
    
    # Encode Client ID and Client Secret
    client_creds = f"{client_id}:{client_secret}"
    client_creds_b64 = base64.b64encode(client_creds.encode())
    
    # Header for the POST request
    headers = {
        "Authorization": f"Basic {client_creds_b64.decode()}"  # Basic <base64 encoded client_id:client_secret>
    }
    
    # Data to be sent in the POST request
    data = {
        "grant_type": "client_credentials"
    }
    
    # Make the POST request to get the access token
    response = requests.post(auth_url, headers=headers, data=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the access token from the response
        token = response.json().get('access_token')
        return token
    else:
        # Handle errors (e.g., print error message)
        print("Failed to authenticate with Spotify")
        return None

def fetch_users_liked_songs(token) -> dict:
    # Spotify URL to fetch a playlist's tracks

    playlist_url = input("Enter the playlist url: ")
    playlist_id = ""

    if playlist_url == "":
        playlist_id = "7IjtBWDXaRs8XbCm4QPCld"
    else: 
        path = urlparse(playlist_url).path
    playlist_id = path.split("/")[-1]

    
    playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    
    # Header including the OAuth token
    headers = {
        "Authorization": f"Bearer {token}"  # Bearer <access_token>
    }
    
    # Make the GET request to fetch the playlist's tracks
    response = requests.get(playlist_url, headers=headers)
    
    # Initialize the dictionary to store liked songs
    liked_songs = {}
    
    # Check if the request was successful
    if response.status_code == 200:
        tracks = response.json().get('items', [])
        for item in tracks:
            # Assuming each item has track which has artists
            artist_info = item.get('track', {}).get('artists', [])
            for artist in artist_info:
                artist_name = artist.get('name')
                if artist_name in liked_songs:
                    liked_songs[artist_name] += 1
                else:
                    liked_songs[artist_name] = 1
    else:
        # Handle errors (e.g., print error message)
        print("Failed to fetch user's liked songs")
    
    return liked_songs