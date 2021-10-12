import requests
import gi
from gi.repository import GTK
from bs4 import BeautifulSoup

forums = {
    "reddit": "http://libredd.it/search?q="
}

def find(search):
    response = requests.get(forums["reddit"]+search)
    soup = BeautifulSoup(response.content, "html.parser")
    for link in soup.find_all("a"):
        if "settings" in link.get("href") or "img" in link.get("href"):
            continue
        print(link.get("href"))

def main():
    pass

if __name__ == "__main__":
    main()
