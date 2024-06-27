from modules import DB, Url
import pandas as pd
from automatedSearch import isAlreadyInDb



def addUrlsOfCsvToDb(fileName, dbName, urlToAddInFront):
    '''
    Adds all urls of a csv file to a databse. Takes a filename and a database name as input. Both as Strings.
    '''
    try:
        file = pd.read_csv(f'urls_from_dashboards/{fileName}.csv')
    except:
        print(f'The csv file {fileName}.csv doesn\'t exist')
        
    db = DB("websites", dbName)
    for index, row in file.iterrows():
        '''adds each url of a csv file to a database
        '''
        url= urlToAddInFront +row["url"] if urlToAddInFront else +row["url"]
        #print(url)
        if isAlreadyInDb(url, db):
            print(url +'not added' )
        else:
            db.insertObject(Url(url).getJsonToAddToDb())


'''
adding the differnet csv files to the database "urlsFromDashboards"'''
#addUrlsOfCsvToDb('carto', 'urlsFromDashboards')
#addUrlsOfCsvToDb('esri', 'urlsFromDashboards')
#addUrlsOfCsvToDb('tableau', 'urlsFromDashboards', 'https://public.tableau.com')
addUrlsOfCsvToDb('tableau2', 'urlsFromDashboards', 'https://public.tableau.com')

