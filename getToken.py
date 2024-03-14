#this whole module is needed to access the spotify api

from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization" : "Bearer " + token}

#searching for artist
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query  = f"?q={artist_name}&type=artist&limit=1"
    #type is what we are looking for, basically filters

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

#getting specified artist from api
def getArtist(token):
    url = "https://api.spotify.com/v1/artists/2h93pZq0e7k5yf4dywlkpM"
    headers = get_auth_header(token)

    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

#getting newReleases from api
def newReleases(token):
    url = "https://api.spotify.com/v1/browse/new-releases?limit=1"
    headers = get_auth_header(token)
    
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    artistName = json_result['albums']['items'][0]['artists'][0]['name']
    albumName = json_result['albums']['items'][0]['name']
    albumCoverURL = json_result['albums']['items'][0]['images'][0]['url']
    return artistName, albumName, albumCoverURL

if __name__ == "__main__":
    token = get_token()
    print(getArtist(token))
    print(newReleases(token))