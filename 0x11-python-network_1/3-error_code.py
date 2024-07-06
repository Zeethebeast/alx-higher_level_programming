#!/usr/bin/python3
"""
Script to fetch data from a URL and print the response body,
handling HTTP errors gracefully.
"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                response_data = response.read().decode('utf-8')
                print(response_data)
            elif response.status == 401:
                print('Error code: 401 Unauthorized')
            elif response.status == 500:
                print('Error code: 500 Internal Server Error')
            else:
                print(f'Unhandled status code: {response.status}')
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print('Reason: ', e.reason)
        else:
            print('URLError occurred, reason not available.')

