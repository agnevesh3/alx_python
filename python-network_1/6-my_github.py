import requests
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    try:
        data = response.json()
        user_id = data["id"]
        print(user_id)
    except ValueError:
        print("Error: Unable to fetch user information")


if __name__ == "__main__":
    main()
