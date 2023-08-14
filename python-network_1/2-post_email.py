def extract_email_from_url(url):
    """
    Extracts the email address from the URL and returns it in a specific format.

    Args:
        url (str): The URL containing the email parameter.

    Returns:
        str: The extracted email address or an error message.
    """
    # Split the URL by "?"
    url_parts = url.split("?")

    if len(url_parts) != 2:
        return "Invalid URL format"

    # Get the parameters after the "?"
    params = url_parts[1]

    # Split the parameters by "&"
    param_pairs = params.split("&")

    for param in param_pairs:
        key_value = param.split("=")
        if len(key_value) == 2 and key_value[0] == "withemail":
            email = key_value[1]
            return f"Email: {email}"

    return "Email parameter not found"


if __name__ == "__main__":
    url = "http://0.0.0.0:5050?withemail=test@test.com"
    result = extract_email_from_url(url)
    print(result)
