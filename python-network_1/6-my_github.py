import requests
import sys


def fetch_github_user_id(username, password):
    """
    Fetches the user ID using the GitHub API with provided credentials.

    Args:
        username (str): GitHub username.
        password (str): Personal access token (password) for GitHub API.

    Returns:
        str: The user ID if successful, or "None" if credentials are invalid.
    """
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 401:
        return None

    try:
        data = response.json()
        user_id = data["id"]
        return user_id
    except ValueError:
        return None


if __name__ == "__main__":
    # Get username and password from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    user_id = fetch_github_user_id(username, password)
    if user_id is not None:
        print(user_id)
    else:
        print("None")
