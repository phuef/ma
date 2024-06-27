from googleSearch import google_search
from addUrlsToDB import addListToDbOnlyUrls
from modules import DB, Url
import random

dbSearchQueriesIV=DB("searchQueries", "IV")
dbSearchQueriesIGV=DB("searchQueries", "IGV")
dbUrlsGottenByGooglesearchIGV=DB("websites","urlsGottenByGooglesearchIGV")
dbUrlsGottenByGooglesearchIV=DB("websites","urlsGottenByGooglesearchIV")


def isAlreadyInDb(url, database):
    '''returns True if the url is already in the database. Takes an url as String and a mongodb database as input '''
    return True if database.find_one({"url": url}) else False

def addUrlToDb(url, database):
    '''adds a url to the mongodb database websites.dbOnlyUrls'''
    database.insertObject(Url(url).getJsonToAddToDb())

# todo: do the same for the other types
def searchForWebsites(amountOfQueries, database, dbSearchqueries): 
    ''' Initiates a google search for a sepecified amount of queries for IV's.
    Out of the search results, 5 random websites will be picked and added to the mongodb
    websites.onlyUrls '''
    queriesToSearchFor=dbSearchqueries.find({ "alreadySearchedFor" : { "$exists" : False } })
    print(f'<<<<<<-------- queries to search for: --------->>>>>>')
    print(queriesToSearchFor)
    i=0
    for query in queriesToSearchFor:
        #print(query) <-- prints the 
        if i==(amountOfQueries +900):
            break
        else:
            i+=1
        if i>900:
            results = google_search(query['query'])
            print(f'<<<<<<-------- results: --------->>>>>>')
            for res in results:
                print(res['link'])

            randomResults = random.sample(results, 5)#choose 5 random results
            for randomResult in randomResults:
                print(f'<<<<<<-------- website for query  --------->>>>>>')
                #print(randomResult)
                print(randomResult['link'])
                if isAlreadyInDb(randomResult['link'], database):
                    print("is already in DB")
                    # todo: choose another result <- is that really neccessary?
                else:
                    addUrlToDb(randomResult['link'], database)
                    print("added to db")
            dbSearchqueries.update_one({"query": query}, {"$set":{"alreadySearchedFor": True}})


#searches for a certain amount of queries
#searchForWebsites(100, dbUrlsGottenByGooglesearchIGV,  dbSearchQueriesIGV)
#searchForWebsites(50, dbUrlsGottenByGooglesearchIV,  dbSearchQueriesIV) 