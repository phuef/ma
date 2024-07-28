from modules import DB
import webbrowser

'''initialize databases'''
dbWithInformation = DB('websites', 'withInformation')
dbWithClassification = DB('websites', 'withClassification')
dbUrlsGottenByGooglesearchIGV = DB('websites', 'urlsGottenByGooglesearchIGV')
dbUrlsFromDashboards =DB('websites', 'urlsFromDashboards')

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
        case _:
            return 'a wrong input. Please try again :)'
         
def classifyManually(db, websitesToCLassify):
    '''Lets you interactively classify websites in the command line.
     A website from the database  will be opened automatically in your browser and you will be asked to 
     determine a website type. As options you can answer with "g", "igv" or "IGV", if the website
     contains a geovisualisation, with "i", "iv" or "IV", if the website contains an interactive 
     visualisation and with "n", "noiv" or "noIV" if the website doesn't contain an interactive
     visaualisation and interactive geovisualisation.
     '''
    for x in websitesToCLassify:
        webbrowser.open(x['url'], new=0, autoraise=False)
        var = input(f"Please classify the website {x['url']}: ")
            
        while (getType(var)=="a wrong input. Please try again :)"):
            print("You entered " +getType(var))
            var = input(f"Please classify the website {x['url']}: ")

        print("You entered: " +getType(var))
        updateRealType(x['url'], getType(var), db) # updates the database entry with the user input
    
    print("All websites have been classified :)")

def printProgress(db):
    amountOfWebsitesInDB=db.count_documents({})
    notClassified=db.count_documents({'real_type': {'$exists': False}})
    classified=db.count_documents({'real_type': {'$exists': True}})
    classifiedIvs=db.count_documents({"real_type": "IV"})
    classifiedIgvs=db.count_documents({"real_type": "IGV"})
    classifiedNoivs=db.count_documents({"real_type": "noIV"})
    
    print(f'Websites in DB: {amountOfWebsitesInDB}')
    print(f'Not Classified: {notClassified}')
    print(f'Classified: {classified}')
    print(f'{classifiedIvs} IV`s, {classifiedIgvs} IGV`s and {classifiedNoivs} noIV`s')
    print(f'{round((classifiedIvs/classified*100), 1)}% IV`s, {round((classifiedIgvs/classified*100), 1)}% IGV`s and {round((classifiedNoivs/classified*100), 1)}% noIV`s')

# -------- the following lines print the current progress of the classifying in the db withInformation -------- 
'''
print('<------------------Not classified yet - DB withInformation ---------------------->')
print(f'{len(unclassifiedWebsites)} websites have not been classified yet')
print('<------------------Already classified---------------------->')
print(f'{dbWithInformation.count_documents({"real_type": "IV"})+dbWithInformation.count_documents({"real_type": "IGV"})+dbWithInformation.count_documents({"real_type": "noIV"})} websites in total')
print(f'{dbWithInformation.count_documents({"real_type": "IV"})} IV`s, {dbWithInformation.count_documents({"real_type": "IGV"})} IGV`s and {dbWithInformation.count_documents({"real_type": "noIV"})} noIV`s')
print(f'{dbWithInformation.count_documents({"real_type": "IV"})/25}% IV`s, {dbWithInformation.count_documents({"real_type": "IGV"})/25}% IGV`s and {dbWithInformation.count_documents({"real_type": "noIV"})/25}% noIV`s')

'''
'''
#  -------- the following lines print the current progress o    f the classifying in the db urlsGottenByGooglesearchIGV --------
print(f'Websites in DB: {dbUrlsGottenByGooglesearchIGV.count_documents({})}')
#print(getWebsitesWithoutFieldRealType(dbUrlsGottenByGooglesearchIGV))
print('Not Classified: ', end='')
print(dbUrlsGottenByGooglesearchIGV.count_documents({'real_type': {'$exists': False}}))
print('Classified: ', end='')
print(dbUrlsGottenByGooglesearchIGV.count_documents({'real_type': {'$exists': True}}))
print(f'{dbUrlsGottenByGooglesearchIGV.count_documents({"real_type": "IV"})} IV`s, {dbUrlsGottenByGooglesearchIGV.count_documents({"real_type": "IGV"})} IGV`s and {dbUrlsGottenByGooglesearchIGV.count_documents({"real_type": "noIV"})} noIV`s')
print(f'{dbUrlsGottenByGooglesearchIGV.count_documents({"real_type": "IV"})/25}% IV`s, {dbUrlsGottenByGooglesearchIGV.count_documents({"real_type": "IGV"})/25}% IGV`s and {dbUrlsGottenByGooglesearchIGV.count_documents({"real_type": "noIV"})/25}% noIV`s')
'''
# Uncomment the next lines, to classify websites in the database "withInformation" manually 
#unclassifiedWebsites = getUnclassifiedWebsites(dbWithInformation)
#classifyManually(dbWithInformation, unclassifiedWebsites)
'''
printProgress(dbUrlsGottenByGooglesearchIGV)
websitesToClassify = getWebsitesWithoutFieldRealType(dbUrlsGottenByGooglesearchIGV)
classifyManually(dbUrlsGottenByGooglesearchIGV, websitesToClassify)

'''
printProgress(dbUrlsFromDashboards)
websitesToClassify_dashboards= getWebsitesWithoutFieldRealType(dbUrlsFromDashboards)
classifyManually(dbUrlsFromDashboards, websitesToClassify_dashboards)
