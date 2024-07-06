#!/usr/bin/python3
"""
Script to fetch and print the body response from specified URLs using the requests module.
"""
import requests

# Fetch data from https://alx-intranet.hbtn.io/status
url1 = 'https://alx-intranet.hbtn.io/status'
response1 = requests.get(url1)
html1 = response1.text

print('Body response from', url1)
print(f'\t- type: {type(html1)}')
print(f'\t- content: {html1}')

# Fetch data from http://0.0.0.0:5050/status
url2 = 'http://0.0.0.0:5050/status'
response2 = requests.get(url2)
html2 = response2.text

print('Body response from', url2)
print(f'\t- type: {type(html2)}')
print(f'\t- content: {html2}')
