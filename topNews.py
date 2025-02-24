import requests
from bs4 import BeautifulSoup

# makes link clickable
def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)

try:
    URL = "https://www.tagesschau.de/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    topNews = soup.find_all("ol", class_= "columns twelve numbered-labels")

    # gets the headlines
    headlines = topNews[0].find_all("span", class_= "teaser-xs__headline")
    
    # gets the links to the articles
    newsLink = topNews[0].find_all("a", class_= "teaser-xs__link")

    counter = 0
    for headline in headlines:
            href = newsLink[counter]['href']
            print(link("https://tagesschau.de"+ href, headline.text.strip()))
            counter = counter +1
except:
    print("There has been an error accessing the page. Make sure you're internet is connected!")