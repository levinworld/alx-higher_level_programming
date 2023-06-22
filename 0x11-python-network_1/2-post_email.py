#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
"""
import urllib.request
from sys import argv


def main(argv):
    """
    Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    url = argv[1]
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf8'))

if __name__ == "__main__":
    main(argv)
cript that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response, A header variable X-HolbertonSchool-User-Id must be sent with the value 98

