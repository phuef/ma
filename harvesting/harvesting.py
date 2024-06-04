from bs4 import BeautifulSoup
from ..database import googleSearch
#page = urllib.request.urlopen("https://www.google.dz/search?q=see")

#soup = BeautifulSoup(page.read())
#links = soup.findAll("a")
#for link in links:
 #   print link["href"]

# function that returns an array of URLs 
    # that were returned from a google search with a given query
def getURLsFromGoogleSearch(searchQuery):
    print(searchQuery)
    results= googleSearch.google_search(searchQuery)
    return results



a=getURLsFromGoogleSearch("maps covid")
print(a)