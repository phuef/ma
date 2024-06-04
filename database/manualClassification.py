from modules import DB
import webbrowser


dbWithInformation = DB('websites', 'withInformation')

'''
class DBWithInformation(DB('websites', 'withInformation')):
    def __init__(self):
        print("Ich bin eine Subklasse")
'''

def getUnclassifiedWebsites():
    '''returns all websites, from the mongodb database websites.withInformation, that haven't been classified with a "real_type" yet'''
    unclassifiedWebsites=[]
    for x in dbWithInformation.find({'real_type': ''}):
        unclassifiedWebsites.append({'url':x['url'], 'estimated_type':x['estimated_type'], 'real_type':x['real_type']})
    return unclassifiedWebsites

def updateRealType(url, newClassification):
    '''updates the "real_type" field of a specific url in the mongodb database websites.withInformation'''
    dbWithInformation.update_one({'url': url}, {"$set":{'real_type': newClassification}})

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
         
def classifyManually():
    '''Lets you interactively classify websites in the command line.
     A website from the database  will be opened automatically in your browser and you will be asked to 
     determine a website type. As options you can answer with "g", "igv" or "IGV", if the website
     contains a geovisualisation, with "i", "iv" or "IV", if the website contains an interactive 
     visualisation and with "n", "noiv" or "noIV" if the website doesn't contain an interactive
     visaualisation and interactive geovisualisation.
     '''
    for x in unclassifiedWebsites:
        webbrowser.open(x['url'], new=0, autoraise=False)
        var = input(f"Please classify the website {x['url']}: ")
            
        while (getType(var)=="a wrong input. Please try again :)"):
            print("You entered " +getType(var))
            var = input(f"Please classify the website {x['url']}: ")

        print("You entered: " +getType(var))
        updateRealType(x['url'], getType(var)) # updates the database entry with the user input
    
    print("All websites have been classified :)")

unclassifiedWebsites = getUnclassifiedWebsites()
#print(unclassifiedWebsites)

# -------- the following lines print the current progress of the classifying -------- 
print('<------------------Not classified yet---------------------->')
print(f'{len(unclassifiedWebsites)} websites have not been classified yet')
print('<------------------Already classified---------------------->')
print(f'{dbWithInformation.count_documents({"real_type": "IV"})+dbWithInformation.count_documents({"real_type": "IGV"})+dbWithInformation.count_documents({"real_type": "noIV"})} websites in total')
print(f'{dbWithInformation.count_documents({"real_type": "IV"})} IV`s, {dbWithInformation.count_documents({"real_type": "IGV"})} IGV`s and {dbWithInformation.count_documents({"real_type": "noIV"})} noIV`s')
print(f'{dbWithInformation.count_documents({"real_type": "IV"})/25}% IV`s, {dbWithInformation.count_documents({"real_type": "IGV"})/25}% IGV`s and {dbWithInformation.count_documents({"real_type": "noIV"})/25}% noIV`s')

# Uncomment the next line, to classify websites manually 
classifyManually()