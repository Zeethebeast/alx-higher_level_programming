#!/usr/bin/python3
"""
Script to fetch and print the body response from specified URLs using the requests module.
"""
import requests

# Fetch data from https://alx-intranet.hbtn.io/status
response1 = requests.get('http://0.0.0.0:5050/status')

if response1.status_code == 200:
    html1 = response1.text
    print('Body response:')
    print(f'\t- type: {type(html1)}')
    print(f'\t- content: {html1}')
else:
    print(f'Failed to fetch data from {url1}. Status code: {response1.status_code}')
