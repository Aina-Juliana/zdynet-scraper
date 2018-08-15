from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getAllTitles(url):
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'html.parser')
    except (HTTPError, URLError) as e:
        print(e)
        return None
    
    titles = bs.find_all('',{'class':'title'})
    titleList = []
    for title in titles:
        titleList.append(title.get_text())
    return titleList

# Example usage
listOfAllCharacter = getAllTitles('http://marvelcinematicuniverse.wikia.com/wiki/Category:Organizations')
for character in listOfAllCharacter:
    print(character)


