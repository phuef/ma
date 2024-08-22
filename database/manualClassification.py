from modules import DB
import webbrowser

'''initialize databases'''
dbWithInformation = DB('websites', 'withInformation')
dbWithClassification = DB('websites', 'withClassification')
dbUrlsGottenByGooglesearchIGV = DB('websites', 'urlsGottenByGooglesearchIGV')
dbUrlsFromDashboards =DB('websites', 'urlsFromDashboards')
dbUrlsGottenByGooglesearchIGV_2 = DB('websites', 'urlsGottenByGooglesearchIGV_2')
dbTest=DB('websites', 'test')

'''
class DBWithInformation(DB('websites', 'withInformation')):
    def __init__(self):
        print("Ich bin eine Subklasse")
'''

def getUnclassifiedWebsites(db):
    '''returns all websites, from the mongodb database websites.withInformation, that haven't been classified with a "real_type" yet'''
    unclassifiedWebsites=[]
    for x in db.find({'real_type': ''}):
        unclassifiedWebsites.append({'url':x['url'], 'estimated_type':x['estimated_type'], 'real_type':x['real_type']})
    return unclassifiedWebsites

def getWebsitesWithoutFieldRealType(db):
    '''returns all websites, from the mongodb database websites.withInformation, that haven't been classified with a "real_type" yet'''
    websites=[]
    for x in db.find({'real_type': {'$exists': False}}):
        websites.append({'url':x['url']})
    return websites

def updateRealType(url, newClassification, db):
    '''updates the "real_type" field of a specific url in the mongodb database websites.withInformation'''
    db.update_one({'url': url}, {"$set":{'real_type': newClassification}})

def deleteUrlFromDatabase(url, db):
    # delete url from database
    print(db.find_one({'url':url}))
    db.delete_one({'url':url})
    

def getType(string):
    '''returns the type for a set of predefined strings, 
    to make the input faster and more convenient
    '''
    match string:
        case 'g' | 'igv' |'IGV':
            return 'IGV'
        case 'i' | 'iv' | 'IV':
            return 'IV'
        case 'n' | 'noiv' | 'noIV':
             return 'noIV'
        case 'd' | 'delete':
            return 'delete'
        case _:
            return 'a wrong input. Please try again :)'
         
def classifyManually(db, websitesToCLassify):
    '''Lets you interactively classify websites in the command line.
     A website from the database  will be opened automatically in your browser and you will be asked to determine a website type. As options you can answer with "g", "igv" or "IGV", if the website contains a geovisualisation, with "i", "iv" or "IV", if the website contains an interactive visualisation, with "n", "noiv" or "noIV" if the website doesn't contain an interactive visualisation and interactive geovisualisation or with "d" or "delete", to delete the website from the database.
     '''
    for x in websitesToCLassify:
        webbrowser.open(x['url'], new=0, autoraise=False)
        var = input(f"Please classify the website {x['url']}: ")
            
        while (getType(var)=="a wrong input. Please try again :)"):
            print("You entered " +getType(var))
            var = input(f"Please classify the website {x['url']}: ")

        print("You entered: " +getType(var))
        if getType(var) != 'delete': 
            updateRealType(x['url'], getType(var), db) # updates the database entry with the user input
        else:
            deleteUrlFromDatabase(x['url'], db)
            ## todo: check if the url was really deleted
            print('Url ' +x['url'] +' was deleted from the database')
    
    print("All websites have been classified :)")

def printProgress(db):
    '''
    Prints the classification progress of a given database.'''

    amountOfWebsitesInDB=db.count_documents({})
    notClassified=db.count_documents({'real_type': {'$exists': False}})
    classified=db.count_documents({'real_type': {'$exists': True}})
    classifiedIvs=db.count_documents({"real_type": "IV"})
    classifiedIgvs=db.count_documents({"real_type": "IGV"})
    classifiedNoivs=db.count_documents({"real_type": "noIV"})

    print(f'Websites in DB: {amountOfWebsitesInDB}')
    print(f'Not Classified: {notClassified}')
    print(f'Classified: {classified}')
    if classified!=0:
        print(f'{classifiedIvs} IV`s, {classifiedIgvs} IGV`s and {classifiedNoivs} noIV`s')
        print(f'{round((classifiedIvs/classified*100), 1)}% IV`s, {round((classifiedIgvs/classified*100), 1)}% IGV`s and {round((classifiedNoivs/classified*100), 1)}% noIV`s')


# Uncomment the next lines, to classify websites in the database "withInformation" manually 
#unclassifiedWebsites = getUnclassifiedWebsites(dbWithInformation)
#classifyManually(dbWithInformation, unclassifiedWebsites)
'''
printProgress(dbUrlsGottenByGooglesearchIGV)
websitesToClassify = getWebsitesWithoutFieldRealType(dbUrlsGottenByGooglesearchIGV)
classifyManually(dbUrlsGottenByGooglesearchIGV, websitesToClassify)

'''
def classify(db):
    printProgress(db)
    websitesToClassify_dashboards= getWebsitesWithoutFieldRealType(db)
    classifyManually(db, websitesToClassify_dashboards)

#classify(dbUrlsFromDashboards)
classify(dbUrlsGottenByGooglesearchIGV_2)
#classify(dbTest)
