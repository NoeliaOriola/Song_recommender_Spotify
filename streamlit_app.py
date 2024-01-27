import sys
import streamlit as st
import config
from config import *
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import numpy as np
import pickle
from IPython.display import HTML

st.markdown(
    """
    <style>
    body {
        background-color: #add8e6;  /* Light Blue color */
    }
    </style>
    """,
    unsafe_allow_html=True
)


data = pd.read_csv('data_clusters.csv')

from config import *
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

def search_song(title, artist, limit):
    try:
        results = sp.search(q=f"{title} {artist}", type='track', limit=limit)
        song_id = results['tracks']['items'][0]['id']
        return song_id
    except IndexError:
        print("Song not found!")
        return ""

def create_link(url:str) -> str:
    return f'''<a href="{url}">🔗</a>'''

st.title("Song Recommender App")

st.sidebar.header("What do you want to listen to?")
artist = st.sidebar.text_input("Type in the artist:")
title = st.sidebar.text_input("Type in the song name:")
limit = 5

# Load scaler
scaler_filename = "./feature_scaler.pickle"
with open(scaler_filename, "rb") as file:
	scaler = pickle.load(file)

# Load UMAP model
umap_filename = "./umap.pickle"
with open(umap_filename, "rb") as file:
	umap = pickle.load(file)

# Load KMeans model
cluster_model_filename = "./kmeans.pickle"
with open(cluster_model_filename, "rb") as file:
	model = pickle.load(file)

if st.sidebar.button("Next"):

	# Search for the song
    song_id = search_song(title, artist, 5)
    
    # Get audio features
    audio_features = sp.audio_features([song_id])
    song = pd.DataFrame(audio_features)

    # Data preprocessing
    features = song.select_dtypes(exclude=[object])
    columns_to_drop = ['liveness', 'duration_ms', 'time_signature']
    features.drop(columns=columns_to_drop, inplace=True)

    # Transform audio features
    user_song_audio_features = scaler.transform(features)
    user_song_audio_features_df = pd.DataFrame(user_song_audio_features, columns=features.columns)

    # Transform with UMAP
    user_song_umap = umap.transform(user_song_audio_features_df)
    user_song_umap_df = pd.DataFrame(user_song_umap, columns=["UMAP_1", "UMAP_2"])

    # Predict cluster
    user_song_cluster = model.predict(user_song_umap_df)[0]
    
    if song_id in data[data['hot_song'] == 1]['id'].tolist():
        result = data[(data['hot_song'] == 1) & (data['cluster'] == user_song_cluster)].sample(5)
    else:
        result = data[(data['hot_song'] != 1) & (data['cluster'] == user_song_cluster)].sample(5)
    

    result['play this song on Spotify'] = 'https://open.spotify.com/track/' + result['id']
   
    output = result[['Title', 'Artists', 'play this song on Spotify']].reset_index(drop=True)

    pd.set_option('display.max_colwidth', None)
    print( )
    print('Here are songs you may like:')



    st.dataframe(output)
