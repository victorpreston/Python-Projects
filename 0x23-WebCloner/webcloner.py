import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class CloneWebsite:
    def __init__(self, website_url):
        self.website_url = website_url
        self.domain_name = urlparse(website_url).netloc
        self.visited_urls = set()

    def get_full_url(self, path):
        return urljoin(self.website_url, path)

    def valid_url(self, url):
        return urlparse(url).netloc == self.domain_name

    def save_content(self, url, path):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
        except Exception as e:
            print(f"Error saving {url}: {e}")

    def crawl_website(self, url=None):
        if url is None:
            url = self.website_url

        if url in self.visited_urls:
            return
        self.visited_urls.add(url)

        try:
            response = requests.get(url)
            if response.status_code != 200:
                return
        except Exception as e:
            print(f"Error accessing {url}: {e}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')

        # Save the current page
        path = urlparse(url).path
        if not path.endswith('.html'):
            path = os.path.join(path, 'index.html')
        self.save_content(url, os.path.join(self.domain_name, path.lstrip('/')))

        # Extract and save all linked resources
        for tag, attribute in [('img', 'src'), ('script', 'src'), ('link', 'href'), ('a', 'href')]:
            for resource in soup.find_all(tag):
                if attribute in resource.attrs:
                    resource_url = self.get_full_url(resource[attribute])
                    if self.valid_url(resource_url):
                        file_path = os.path.join(self.domain_name, urlparse(resource_url).path.lstrip('/'))
                        if resource_url.endswith('.html'):
                            self.crawl_website(resource_url)
                        else:
                            self.save_content(resource_url, file_path)

if __name__ == "__main__":
    website_url = sys.argv[1]
    clone = CloneWebsite(website_url)
    clone.crawl_website()