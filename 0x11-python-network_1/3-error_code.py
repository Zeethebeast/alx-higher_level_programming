#!/usr/bin/python3
import sys
import urllib.request
import urllib.error
url = sys.argv[1]
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode('utf-8')
        print(response_data)
except urllib.error.HTTPError as e:
    print('Error code: ', e.code)
except urllib.error.URLError as e:
    print('Reason: ', e.reason)
