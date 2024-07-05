#!/usr/bin/python3
import urllib.request
import sys

if len(sys.argv) < 2:
    print("Usage: script.py <url>")
    sys.exit(1)

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
