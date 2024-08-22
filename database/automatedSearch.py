from googleSearch import google_search
from addUrlsToDB import addListToDbOnlyUrls
from modules import DB, Url, isAlreadyInDb
import random

dbSearchQueriesIV=DB("searchQueries", "IV")
dbSearchQueriesIGV=DB("searchQueries", "IGV")
dbSearchQueriesIGV_2=DB("searchQueries", "IGV_2")
dbUrlsGottenByGooglesearchIGV=DB("websites","urlsGottenByGooglesearchIGV")
dbUrlsGottenByGooglesearchIV=DB("websites","urlsGottenByGooglesearchIV")
dbUrlsGottenByGooglesearchIGV_2 =DB('websites', 'urlsGottenByGooglesearchIGV_2')



def addUrlToDb(url, database):
    '''adds a url to the mongodb database websites.dbOnlyUrls'''
    database.insertObject(Url(url).getJsonToAddToDb())

# todo: do the same for the other types
def searchForWebsitesWithRandomness(amountOfQueries, database, dbSearchqueries): 
    ''' Initiates a google search for a sepecified amount of queries.
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

def searchForWebsites(database, dbSearchqueries): 
    ''' Initiates a google search for a set of queries and saves the returned urls in a database. 
    '''
    queriesToSearchFor=dbSearchqueries.find({ "alreadySearchedFor" : { "$exists" : False } })
    print(f'<<<<<<-------- queries to search for: --------->>>>>>')
    print(queriesToSearchFor)
    for query in queriesToSearchFor:
        print(f'<<<<<<-------- query:  --------->>>>>>')
        print(query['query']) #<-- prints the query
        results = google_search(query['query'])
        print(f'<<<<<<-------- results: --------->>>>>>')
        for res in results:
            print(res['link'])
            if isAlreadyInDb(res['link'], database):
                print("is already in DB")
            else:
                addUrlToDb(res['link'], database)
                print("added to db")
        dbSearchqueries.update_one({"query": query['query']}, {"$set":{"alreadySearchedFor": True}})


#searches for a certain amount of queries
#searchForWebsites(dbUrlsGottenByGooglesearchIGV,  dbSearchQueriesIGV)
#searchForWebsites(dbUrlsGottenByGooglesearchIV,  dbSearchQueriesIV) 
#searchForWebsites(dbUrlsSearchQueriesIgvSecondTry)
searchForWebsites(dbUrlsGottenByGooglesearchIGV_2, dbSearchQueriesIGV_2)