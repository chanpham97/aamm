import requests
import base64
import config
import path

def get_token():
    header = {'Authorization': 'Basic ' + base64.b64encode(config.SPOTIFY_CLIENT_ID + ':' + config.SPOTIFY_CLIENT_SECRET).encode('ascii')}
    r = requests.post(path.SPOTIFY_AUTH, data={'grant_type': 'client_credentials'}, headers=header)
    return r.json()["access_token"]


def get_id(name, typ):
    headers = {'Authorization': 'Bearer ' + get_token()}
    query = {'q': name, 'type': typ}
    r = requests.get(path.SPOTIFY_SEARCH, headers=headers, params=query)
    return r.json()[typ + 's']


print(get_id('instrumental study', 'playlist'))