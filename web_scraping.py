import requests

def get_wikipedia_for_demographic_data(artist: str) -> dict:
    """
    Fetch the main text summary for a given artist from Wikipedia.
    """
    # Use the Wikipedia API to search for a page matching the artist's name
    search_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": artist,
        "utf8": 1,
        "srlimit": 1
    }

    response = requests.get(search_url, params=params)
    search_results = response.json()
    
    # Check if there are results
    if search_results['query']['search']:
        pageid = search_results['query']['search'][0]['pageid']
        
        # Fetch the main text summary using the pageid
        content_url = "https://en.wikipedia.org/w/api.php"
        content_params = {
            "action": "query",
            "prop": "extracts",
            "format": "json",
            "pageids": pageid,
            "exintro": True,
            "explaintext": True,
        }
        
        content_response = requests.get(content_url, params=content_params)
        content_results = content_response.json()

        # Extract the main text
        main_text = content_results['query']['pages'][str(pageid)]['extract']

        # Return the main text in a structured format
        return {"main_text": main_text}
    else:
        # Return a message indicating no results were found
        return {"main_text": "No Wikipedia page found for this artist."}
