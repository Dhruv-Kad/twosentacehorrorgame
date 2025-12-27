import requests
from bs4 import BeautifulSoup
import json


def makedict(file):
    try:
        with open(file, 'r') as target:
            return(json.load(target))
    except FileNotFoundError as e:
        return {}
# This next one should be able to get any page and then keep "scrolling down" and return the next post
# could just do it recursively though readfile
def makevalid(inlist: str):
    linknozelda = inlist
    while not linknozelda.endswith('/'):
        linkedlist = list(linknozelda)
        linkedlist.pop()
        linknozelda = "".join(linkedlist)
    return linknozelda 


def readfile(inlinker: str, timesrepeated=0):
    html_content = requests.get(inlinker).text
    bodymap = makedict("data.json")
    soup = BeautifulSoup(html_content, 'html.parser')
    n = timesrepeated
    titles = soup.find_all('a', slot='title')
    bodies = soup.find_all('shreddit-post-text-body')
    taglist = soup.find_all(attrs={"post-id": True})
    last = taglist.pop()['post-id']
    
    for title, body in zip(titles, bodies):
        t = (title.get_text(strip=True))
        b = (body.get_text(strip=True))
        bodymap[t] = b
        n += 1
    with open("data.json", 'w') as d:
        json.dump(bodymap,d,indent=3)
    #Setting this number very high, best to change it if you want less posts to be fetched
    if n < 123:
        base = makevalid(inlinker)
        base = f"{base}?after={last}"
        print(base)
        readfile(base, n)
    else:
        print(f"Found {n*3} posts")

if __name__ == "__main__":
    readfile("https://reddit.com/r/TwoSentenceHorror/new/")

