import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Horizontal(Colors.purple_to_blue, text, 1)

class crawler:
    def __init__(self, base_url, max_threads=10):
        self.base_url = base_url
        self.visited = set()
        self.lock = threading.Lock()
        self.executor = ThreadPoolExecutor(max_threads)
        self.futures = []

    def crawl(self, url):
        with self.lock:
            if url in self.visited:
                return
            self.visited.add(url)

        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            time = datetime.now().strftime("%H:%M:%S")
            print(f"{fade("[")}{time}{fade("]")} Failed to fetch {url}: {e}")
            return

        title = soup.title.string.strip() if soup.title else "No Title"
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Title: {title} > URL: {url}")

        self.handle_links(soup, url)

        self.handle_images(soup, url)

        self.handle_scripts(soup, url)

        self.handle_stylesheets(soup, url)

    def handle_links(self, soup, base_url):
        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(base_url, link['href'])
            if absolute_url.startswith(self.base_url) and absolute_url not in self.visited:
                future = self.executor.submit(self.crawl, absolute_url)
                self.futures.append(future)

    def handle_images(self, soup, base_url):
        for img in soup.find_all('img', src=True):
            absolute_url = urljoin(base_url, img['src'])
            if absolute_url.startswith(self.base_url) and absolute_url not in self.visited:
                time = datetime.now().strftime("%H:%M:%S")
                print(f"{fade("[")}{time}{fade("]")} Image: {absolute_url}")
                future = self.executor.submit(self.crawl, absolute_url)
                self.futures.append(future)

    def handle_scripts(self, soup, base_url):
        for script in soup.find_all('script', src=True):
            absolute_url = urljoin(base_url, script['src'])
            if absolute_url.startswith(self.base_url) and absolute_url not in self.visited:
                time = datetime.now().strftime("%H:%M:%S")
                print(f"{fade("[")}{time}{fade("]")} Script: {absolute_url}")
                future = self.executor.submit(self.crawl, absolute_url)
                self.futures.append(future)

    def handle_stylesheets(self, soup, base_url):
        for link in soup.find_all('link', href=True):
            if link.get('rel') == ['stylesheet']:
                absolute_url = urljoin(base_url, link['href'])
                if absolute_url.startswith(self.base_url) and absolute_url not in self.visited:
                    time = datetime.now().strftime("%H:%M:%S")
                    print(f"{fade("[")}{time}{fade("]")} Stylesheet: {absolute_url}")
                    future = self.executor.submit(self.crawl, absolute_url)
                    self.futures.append(future)

    def start(self):
        future = self.executor.submit(self.crawl, self.base_url)
        self.futures.append(future)

        for future in as_completed(self.futures):
            future.result()

        self.executor.shutdown()

if __name__ == "__main__":
    banner = r"""
  .  .
 .|  |.
 ||  ||
 \\()//
 .={}=.
/ /`'\ \
` \  / '
   `'
"""

    print(Colorate.Horizontal(Colors.purple_to_blue, banner, 1))
    time = datetime.now().strftime("%H:%M:%S")
    base_url = input(f"\n{fade("[")}{time}{fade("]")} > Enter URL: ")
    spider = crawler(base_url, max_threads=50)
    spider.start()

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python master.py")
