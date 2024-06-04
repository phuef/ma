from googleSearch import google_search
from addUrlsToDB import addListToDbOnlyUrls
from modules import DB, Url
import random

dbSearchQueriesIV=DB("searchQueries", "testIV")
dbOnlyUrls=DB("websites","onlyUrls")


def isAlreadyInDb(url):
    '''returns True if the url is already in the mongodb database websites.onlyUrls '''
    return True if dbOnlyUrls.find_one({"url": url}) else False

def addUrlToDb(url):
    '''adds a url to the mongodb database websites.dbOnlyUrls'''
    dbOnlyUrls.insertObject(Url(url).getJsonToAddToDb())

# todo: do the same for the other types
def searchForWebsites(amountOfQueries): 
    ''' Initiates a google search for a sepecified amount of queries for IV's.
    Out of the search results, 5 random websites will be picked and added to the mongodb
    websites.onlyUrls '''
    queriesToSearchFor=dbSearchQueriesIV.find({ "alreadySearchedFor" : { "$exists" : False } })
    i=0
    for query in queriesToSearchFor:
        if i==amountOfQueries:
            break
        else:
            i+=1
        results = google_search(query['query'])
        randomResults = random.sample(results, 5)#choose 5 random results
        for randomResult in randomResults:
            print(f'<<<<<<-------- website {i} --------->>>>>>')
            #print(randomResult)
            print(randomResult['link'])
            if isAlreadyInDb(randomResult['link']):
                print("in already in DB")
                # todo: choose another result <- is that really neccessary?
            else:
                addUrlToDb(randomResult['link'])
                print("added to db")
        dbSearchQueriesIV.update_one({"query": query}, {"alreadySearchedFor": True})
    
searchForWebsites(1)