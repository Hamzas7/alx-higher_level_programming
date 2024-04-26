#!/usr/bin/python3
import requests

if __name__ == "__main__":
    # Define the URL to fetch
    url = 'https://alx-intranet.hbtn.io/status'

    # Send a GET request to the URL using the requests package
    response = requests.get(url)

    # Parse the response body as JSON
    body_dict = response.json()

    # Print the response body in the required format
    print("Body response:")

    # Print the type of the 'status' field in the response body
    print("\t- type:", type(body_dict['status']))

    # Print the content of the 'status' field in the response body
    print("\t- content:", body_dict['status'])

