import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    x_request_id = response.headers.get("X-Request-Id")
    if x_request_id is not None:
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
