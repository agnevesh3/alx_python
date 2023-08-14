import requests


def fetch_and_print_status(url):
    """
    Fetches the status of a URL using an HTTP GET request and prints the response details.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        None
    """
    response = requests.get(url)

    print("Body response:")
    print(f"    - type: {type(response.text)}")
    print(f"    - content: {response.text}")


if __name__ == "__main__":
    # Define the URL to fetch data from
    target_url = "https://alu-intranet.hbtn.io/status"

    # Call the fetch_and_print_status function with the target URL
    fetch_and_print_status(target_url)
else:
    print("Error: This script should be run as the main program.")
