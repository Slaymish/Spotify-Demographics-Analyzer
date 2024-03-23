from spotify_integration import authenticate_spotify, fetch_users_liked_songs
from web_scraping import get_wikipedia_for_demographic_data
from analysis import analyze_demographics
from AI import get_formatted_demographic_data
from visualise_data import visualise_demographic_data
import json
from tqdm import tqdm

# Function to load the cache, if it exists
def load_cache(cache_file):
    try:
        with open(cache_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save the updated cache
def save_cache(cache, cache_file):
    with open(cache_file, 'w') as file:
        json.dump(cache, file, indent=4)

def main():
    # Authenticate with Spotify and get access token
    token = authenticate_spotify()
    print("Authenticated with Spotify.")

    if not token:
        print("Failed to authenticate with Spotify. Exiting.")
        return
    
    # Fetch user's liked songs and artist information
    artist_song_count = fetch_users_liked_songs(token)
    print("Fetched user's liked songs and artist information.")

    if not artist_song_count:
        print("No data found. Exiting.")
        return
    
    # Path to the cache file
    cache_file = "artist_cache.json"
    artist_demographics = load_cache(cache_file)
    
    # For each artist in artist_song_count, scrape Wikipedia for demographic data
    for artist in tqdm(artist_song_count.keys(), desc="Processing artists", unit="artist"):
        # Check if artist data is not in cache
        if artist not in artist_demographics:
            tqdm.write(f"Fetching data for {artist}")
            wikipedia_text = get_wikipedia_for_demographic_data(artist)  # Get Wikipedia data
            formatted_data = get_formatted_demographic_data(wikipedia_text)  # Format the data
            
            # Check if the response contains an error before updating the cache
            if "error" not in formatted_data:
                artist_demographics[artist] = formatted_data  # Update cache with new data
                save_cache(artist_demographics, cache_file)  # Save updated cache
            else:
                tqdm.write(f"Error processing data for {artist}")
        else:
            formatted_data = artist_demographics[artist]

    # Perform demographic analysis on the collected data
    demographic_analysis_result = analyze_demographics(artist_demographics)
    
    visualise_demographic_data(demographic_analysis_result)



if __name__ == "__main__":
    main()