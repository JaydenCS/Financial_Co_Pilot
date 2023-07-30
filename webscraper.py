import requests
from bs4 import BeautifulSoup

def get_all_text_content(url):
    try:
        # Send an HTTP GET request to fetch the web page content
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the request

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract all the text content from the page
        text_content = soup.get_text(separator=" ")

        return text_content[:5000]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the web page: {e}")
        return ""