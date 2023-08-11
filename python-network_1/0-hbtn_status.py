import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print(f"    - type: {type(response.text)}")
    print(f"    - content: {response.text}")
else:
    print(f"Error: Unable to fetch data. Status code")
