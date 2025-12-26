import requests


def main():
    siteget = requests.get("https://www.reddit.com/r/TwoSentenceHorror/").text
    print(siteget)



if __name__ == "__main__":
    main()
