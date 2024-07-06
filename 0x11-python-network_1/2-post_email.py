#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a python script take in an url and displays"""
"""In the format or manner presented below"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    # create the data.
    data = {}
    data['email'] = sys.argv[2]

    # encode the values to be sent over to the server
    new = urllib.parse.urlencode(data)
    new = encoded_data.encode('ascii')

    # create a request using the url and the inteded data
    request = urllib.request.Request(sys.argv[1], new)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
