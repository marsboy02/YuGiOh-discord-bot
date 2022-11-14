from requests import *

default_url = 'http://localhost:3000'

def get(url, parmas=None):
    res = request('get', url, parmas = parmas)
    return res.json()
