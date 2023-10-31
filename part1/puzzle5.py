import requests



# API URL
url = 'https://api.codehunt.nl/categories/clnx6wdxc0004od0uemi4n473/exercises/clnyhzo5p000kod0uqgornh1i'

# Headers
headers = {
    'authority': 'api.codehunt.nl',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,nl-NL;q=0.8,nl;q=0.7',
    'authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjbG9lNmN5cmtoMmYwcXkwdDI1MHd4emFlIiwidXNlciI6eyJpZCI6ImNsb2U2Y3lya2gyZjBxeTB0MjUwd3h6YWUiLCJuYW1lIjoiTmF0aGFuIERyaWVzcHJvbmciLCJtaWNyb3NvZnRJZCI6ImE2NDYyNWNlLTQ1ZWUtNGZmNi05ZTMyLWJiMDBiYzhiYTdiYyIsInN0dWRlbnRJZCI6IjEwNzY3NzEiLCJ0eXBlIjoiU1RVREVOVCJ9LCJpYXQiOjE2OTg3NDc0MzEsImV4cCI6MTY5OTAwNjYzMX0.K-ZJj3Z3nL3pRQpFNJREgyKj1Vnrr7BdzeNQ8MR1AWs', # Replace with your actual authorization token
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://codehunt.nl',
    'referer': 'https://codehunt.nl/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Linux',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

# Iterate through all possible 8-digit binary numbers
for i in range(256):
    binary_number = format(i, '08b')  # Format as 8-digit binary

    # Data with the binary number
    data = {
        "answer": binary_number
    }

    # Send the request
    response = requests.post(url, headers=headers, json=data)
    
    # Check if the response does not include "Wrong" and print it
    if "Wrong" not in response.text:
        print(f"Binary Number: {binary_number}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")
        print("\n---\n")
