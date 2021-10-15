import requests
#import gi
#gi.require_version("Gtk", "4.0")
#from gi.repository import Gtk
from bs4 import BeautifulSoup

def find(search, filter):
    response = requests.get(f"http://libredd.it/search?q={search}&sort=relevance")
    soup = BeautifulSoup(response.content, "html.parser")
    for link in soup.find_all("a"):
        if "settings" in link.get("href") or "img" in link.get("href") or "github.com/" in link.get("href"):
            continue

        if filter in link.get("href"):
            print(link.get("href"))
        else:
            continue

def main():
    filter = ""
    while True:
        command = input("> ")
        if command in ("quit", "exit"):
            break
        elif command.split(" ")[0] == "search":
            find(command.replace("search ", ""), filter)
        elif command.split(" ")[0] == "filter":
            filter = "" if len(command.split(" ")) == 1 else command.split(" ")[1]

if __name__ == "__main__":
    main()
