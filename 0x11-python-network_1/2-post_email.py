#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys


url = 'http://0.0.0.0:5000/post_email'
values = {'email': 'hr@holbertonschool.com'}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    response_data = response.read().decode('utf-8')

print(f'Your email is: {response_data}')
