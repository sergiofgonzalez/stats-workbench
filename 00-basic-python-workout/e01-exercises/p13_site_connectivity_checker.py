from tabnanny import check
from urllib.request import urlopen


def check_site(url):
    print(f"Connecting to {url}")
    with urlopen(url) as response:
        http_response_code = response.getcode()
        print(f"site response was {http_response_code}")


print("== site connectivity checker ==")
input_url = input("Type the URL to check: ")

check_site(input_url)
