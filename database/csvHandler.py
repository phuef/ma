from modules import DB, Url
import pandas as pd
from modules import isAlreadyInDb



def addUrlsOfCsvToDb(fileName, dbName, urlToAddInFront=""):
    '''
    Adds all urls of a csv file to a databse. Takes a filename and a database name as input. Both as Strings. Optional an urlToAddInFront can be set which is added infront of each entry. This is needed for routes that are unfinished 
    '''
    try:
        file = pd.read_csv(f'urls_from_dashboards/{fileName}.csv')
    except:
        print(f'The csv file {fileName}.csv doesn\'t exist')
        
    db = DB("websites", dbName)
    for index, row in file.iterrows():
        '''adds each url of a csv file to a database
        '''
        print(urlToAddInFront)
        url= urlToAddInFront +row["url"] #if urlToAddInFront else +row["url"]
        if isAlreadyInDb(url, db):
            print(url +' not added' )
        else:
            db.insertObject(Url(url).getJsonToAddToDb())
            print(url +' added' )


'''
adding the differnet csv files to the database "urlsFromDashboards"'''
#addUrlsOfCsvToDb('carto', 'urlsFromDashboards')
#addUrlsOfCsvToDb('esri', 'urlsFromDashboards')
#addUrlsOfCsvToDb('tableau', 'urlsFromDashboards', 'https://public.tableau.com')
#addUrlsOfCsvToDb('tableau2', 'urlsFromDashboards', 'https://public.tableau.com')
#addUrlsOfCsvToDb('plotly', 'urlsFromDashboards')
