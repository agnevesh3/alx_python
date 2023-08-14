import requests
import sys


def fetch_x_request_id(url):
    """
    Fetches the value of the X-Request-Id header from the response of the given URL.

    Args:
        url (str): The URL to fetch the response from.

    Returns:
        str: The value of the X-Request-Id header if found, else "X-Request-Id header not found in the response."
    """
    response = requests.get(url)

    x_request_id = response.headers.get("X-Request-Id")
    if x_request_id is not None:
        return x_request_id
    else:
        return "X-Request-Id header not found in the response."


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = fetch_x_request_id(url)
    print(x_request_id)
