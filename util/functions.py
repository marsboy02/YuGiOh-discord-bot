import requests

default_url = 'http://localhost:3000'


def get(url, params):
    uri = url + params
    return requests.get(uri)


def backtick(string):
    return '```' + string + '```'


def addContent(key, value):
    if value != '':
        return key + ' : ' + value + '\n'
    else:
        return ''


def makeStringWithSpace(*args):
    string = ''
    for i in args:
        string += i + ' '
    return string
