import requests
#import gi
#gi.require_version("Gtk", "4.0")
#from gi.repository import Gtk
from bs4 import BeautifulSoup

forums = {
    "reddit": "http://libredd.it/search?q="
}

def find(search):
    response = requests.get(forums["reddit"]+search)
    soup = BeautifulSoup(response.content, "html.parser")
    for link in soup.find_all("a"):
        if "settings" in link.get("href") or "img" in link.get("href") or "github.com/" in link.get("href"):
            continue
        print(link.get("href"))

def main():
    while True:
        search = input("What do you want to find: ")
        if search in ("quit", "exit"):
            break
        find(search)

if __name__ == "__main__":
    main()
