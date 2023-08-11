import requests
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        return

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {"email": email}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Your email is:", response.text)
    else:
        print("Error:", response.status_code)
