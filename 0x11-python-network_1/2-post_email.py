#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a python script take in an url and displays"""
"""In the format or manner presented below"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    
    url = 'http://0.0.0.0:5000/post_email'
    values = {'email': 'hr@holbertonschool.com'}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode('utf-8')
        print(f'Your email is: {response_data}')
