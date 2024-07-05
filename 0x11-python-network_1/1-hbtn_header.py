#!/usr/bin/env python3
import urllib.request
import sys

if len(sys.argv) < 2:
    print("Usage: script.py <url>")
    sys.exit(1)

url = sys.argv[1]
header_name = 'X-Request-Id'

with urllib.request.urlopen(url) as response:
    print(response.headers.get(header_name))

