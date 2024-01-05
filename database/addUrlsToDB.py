#import pymongo
from modules import DB, UrlList
import pandas as pd
## add a list of Urls to a database in the format {"url": "www.google.de"}

def addListToDbOnlyUrls(listOfUrls): # ToDo: replace the list with 
    dbOnlyUrls = DB("websites", "onlyUrls")
    urls= UrlList(listOfUrls)
    dbOnlyUrls.insertList(urls.getJson())
    dbOnlyUrls.printAllObjects() #prints all objects in the database

# adds the data of a csv file that lays in the folder urls_from_bachelor_thesis to the mongodb database "onlyUrls"
def addDataFromCsvFileToDbOnlyUrls(csvFileName):
    data = pd.read_csv (f'urls_from_bachelor_thesis\{csvFileName}.csv')
    df = pd.DataFrame(data, columns= ['urls']) # add 
    listOfUrls = df['urls'].tolist()
    addListToDbOnlyUrls(listOfUrls)
     

# addDataFromCsvFileToDbOnlyUrls("toAnalyze")
