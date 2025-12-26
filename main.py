import requests
from bs4 import BeautifulSoup


def main():
    html_content = requests.get("https://www.reddit.com/r/TwoSentenceHorror/").text
    bodymap ={}

    soup = BeautifulSoup(html_content, 'html.parser')
    
    titles = soup.find_all('a', slot='title')
    bodies = soup.find_all('shreddit-post-text-body')
    
    for title in titles:
        t = (title.get_text(strip=True))

    for body in bodies:
        b = (body.get_text(strip=True))



if __name__ == "__main__":
    main()
