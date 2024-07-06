#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read().decode('utf-8')

print('Body response:')
print(f'\t- type: {type(html)}')
print(f'\t- content: {html}')
