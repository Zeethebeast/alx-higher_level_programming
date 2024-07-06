#!/usr/bin/python3
"""
Script to fetch and print the body response from specified URLs using the requests module.
"""
import requests

# Fetch data from https://alx-intranet.hbtn.io/status
url1 = 'https://alx-intranet.hbtn.io/status'
response1 = requests.get(url1)
html1 = response1.text

print('Body response:')
print(f'\t- type: {type(html1)}')
print(f'\t- content: {html1}')
