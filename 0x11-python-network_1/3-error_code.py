#!/usr/bin/python3
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode('utf-8')
            print(response_data)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print('Reason: ', e.reason)
        else:
            print('URLError occurred, reason not available.')
