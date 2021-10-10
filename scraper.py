import requests
from bs4 import BeautifulSoup

forums = {
    "reddit": "http://libredd.it/search?q="
}

def main():
    search = input("What do you want me to find: ")
    response = requests.get(forums["reddit"]+search)
    soup = BeautifulSoup(response.content, "html.parser")
    for link in soup.find_all("a"):
        if "settings" in link.get("href") or "img" in link.get("href"):
            continue
        print(link.get("href"))

if __name__ == "__main__":
    main()
