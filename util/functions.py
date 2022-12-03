import requests

default_url = 'http://localhost:3000'


def get(url, parmas):
    uri = url + parmas
    return requests.get(uri)


def backtick(string):
    return '```' + string + '```'


def addContent(key, value):
    if value != '':
        return key + ' : ' + value + '\n'
    else:
        return ''
