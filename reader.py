import requests
from bs4 import BeautifulSoup
import json

def makedict(file):
    try:
        with open(file, 'r') as target:
            return(json.load(target))
    except FileNotFoundError as e:
        return {}
def readfile(inlinker):
    html_content = requests.get(inlinker).text
    bodymap = makedict("data.json")

    soup = BeautifulSoup(html_content, 'html.parser')
    
    titles = soup.find_all('a', slot='title')
    bodies = soup.find_all('shreddit-post-text-body')
    
    for title, body in zip(titles, bodies):
        t = (title.get_text(strip=True))
        b = (body.get_text(strip=True))
        bodymap[t] = b
    with open("data.json", 'w') as d:
        json.dump(bodymap,d,indent=3)



if __name__ == "__main__":
    readfile()
