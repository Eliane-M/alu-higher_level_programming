#!/usr/bin/python3
"""
fetches https://alu-intranet.hbtn.io/status
"""
import urllib.request


def main():
    """
    fetches the url
    """
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8"))

if __name__ == '__main__':
    main()
