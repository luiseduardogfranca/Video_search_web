import re
import requests
from bs4 import BeautifulSoup

from ..settings import MAX_SHOW_VIDEOS

GOOGLE_URL_SEARCH="https://www.google.com/search?q="

GET_HEADER = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,charset=UTF-8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'close'}

SESSION = requests.Session()
SESSION.trust_env = False

class Page_video():
    def __init__(self, url, title):
        self.title = title
        self.url = url
    
    def __str__(self):
        return self.url

    @classmethod
    def get_page_videos(cls, url):
        html = get_html(url)
        soup = BeautifulSoup(html, "html.parser")
        page_videos = [Page_video(tag.source["src"], soup.title.string) for tag in soup.find_all("video")]
        
        return page_videos
    
    @classmethod
    def search_videos(cls, seach_text, max_videos = MAX_SHOW_VIDEOS):
        links = get_google_links(seach_text)
        videos = []
        for link in links:
            _videos = cls.get_page_videos(link)
            videos = videos + _videos
            if max_videos!=None and len(videos) >= max_videos:
                break
        
        return videos


def get_html(url, headers = GET_HEADER):
    response = SESSION.get(url, headers = headers)
    html = response.text
    return html.encode("utf-8")

def get_google_links(search_text):
    html = get_html(GOOGLE_URL_SEARCH+search_text)
    soup = BeautifulSoup(html, "html.parser")
    links = [tag.a["href"]  for tag in soup.find_all("h3", "r")]
    return links


if __name__ == "__main__":
    print(Page_video.search_videos("overlord ep 1")[0])