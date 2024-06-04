#import pymongo
from modules import DB, UrlList
import pandas as pd

def addListToDbOnlyUrls(listOfUrls):
    ''' add a list of Urls to the mongodb database websites.onlyUrls in the format {"url": "www.example-url.com"}'''
    dbOnlyUrls = DB("websites", "onlyUrls")
    urls= UrlList(listOfUrls)
    dbOnlyUrls.insertList(urls.getJson())
    dbOnlyUrls.printAllObjects() #prints all objects in the database

def addDataFromCsvFileToDbOnlyUrls(folderName,csvFileName):
    '''add the data of a csv file to the mongodb database websites.onlyUrls'''
    data = pd.read_csv (f'{folderName}\{csvFileName}.csv')
    df = pd.DataFrame(data, columns= ['urls'])
    listOfUrls = df['urls'].tolist()
    addListToDbOnlyUrls(listOfUrls)
     
# the following line adds the websites from my bachelor thesis (see github.com/phuef/ba) to mongoDB
# addDataFromCsvFileToDbOnlyUrls("urls_from_bachelor_thesis","toAnalyze")
