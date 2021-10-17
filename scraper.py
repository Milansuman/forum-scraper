import requests
from bs4 import BeautifulSoup

class Scraper:

    def __init__(self):
        self.command = ""
        self.filter = ""

    def prompt(self):
        self.command = input("> ")
        if self.command in ("quit", "exit"):
            exit()
        elif self.command.split(" ")[0] == "search":
            self.find(self.command.replace("search ", ""))
        elif self.command.split(" ")[0] == "filter":
            self.filter = "" if len(self.command.split(" ")) == 1 else self.command.split(" ")[1]

    def find(self, search):
        response = requests.get(f"http://libredd.it/search?q={search}&sort=relevance")
        soup = BeautifulSoup(response.content, "html.parser")
        for link in soup.find_all("a"):
            if "settings" in link.get("href") or "img" in link.get("href") or "github.com/" in link.get("href"):
                continue

            if self.filter in link.get("href"):
                print(link.get("href"))
            else:
                continue

def main():
    scraper = Scraper()
    while True:
        scraper.prompt()
        

if __name__ == "__main__":
    main()
