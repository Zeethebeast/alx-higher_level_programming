#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a Python script that takes in a URL and an email address,
encodes the email as data, sends a request, and displays the response."""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Check if enough arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    # Create the data dictionary with 'email' key from command-line arguments
    data = {'email': sys.argv[2]}

    # Encode the data to be sent over to the server
    encoded_data = urllib.parse.urlencode(data)
    encoded_data = encoded_data.encode('ascii')  # Encode as ASCII

    # Create a request using the URL and the intended data
    url = sys.argv[1]
    request = urllib.request.Request(url, encoded_data)

    # Send the request and print the response
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
