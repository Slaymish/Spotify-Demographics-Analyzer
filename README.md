# Spotify Playlist Demographic Analyzer

Uses Spotify API, wikipedia API, OpenAI API (GPT-3.5-turbo)

1. **Fetch Artists**: Extracts artist names from the given Spotify playlist.
2. **Demographic Information**:
   - Cached Data: Uses stored demographic information if available.
   - Wikipedia and GPT-3.5-turbo: If no cache data is available, the tool queries Wikipedia for the artist's bio, then uses GPT-3.5-turbo to extract demographic information and formats it as JSON.
3. **Visualization**: Uses matplotlib to create a visual representation of the playlist's artist demographic information.

## To use

### Prerequisites

A Spotify Developer account to access the Spotify API.
An OpenAI account for access to the GPT-3.5-turbo API.

### Setup

1. **Create a Spotify app**:
   - Visit [Spotify Dashboard](https://developer.spotify.com/dashboard)
   - Note down the Client ID and Secret.
2. **Environment Setup**:

   - Clone or download this repository to your local machine.
   - Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   - Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration**:
   - Copy your Spotify Client ID, Client Secret, and OpenAI API Key into the .env file in the root directory of the project.
4. **Usage**:

   - Run the script and input the Spotify playlist URL when prompted:

   ```bash
   python3 main.py
   ```
