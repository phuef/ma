from modules import Url, DB, isAlreadyInDb
import winsound
from tqdm import tqdm




def addUrlsOfDbToAnotherDbWithEmbeddingsAndWebsiteInformations(dbUrls, dbWithEmbeddings):
    '''
    for each url in the database with an existing type:
    add it to database classified with the feature information and the url
    '''
    alreadyInDBCount=0
    added=0
    dbTest = DB('websites', dbUrls)
    dbClassified = DB('websites', dbWithEmbeddings)
    websites=dbTest.find({'real_type': {'$exists':True}})
    for website in tqdm(websites):
        urlList=[]
        url=Url(website['url'], website['real_type'])
        if isAlreadyInDb(website['url'], dbClassified):
            print(website['url'], ' is already in the database')
            alreadyInDBCount+=1
        else:
            try:
                print('getting information for url: ',website['url'])
                json=url.getWebsiteInformation()
                urlList.append(json)
                dbClassified.insertList(urlList)
                print(website['url'] ,' added')
                added+=1
            except:
                print('<-------- url ', website['url'] , 'could not be added ----------->')
                #print('\007')
    print('finished')
    print('Added to db: : ', added)
    print('Have been already in db: ', alreadyInDBCount)
    duration = 5000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)


#addUrlsOfDbToAnotherDbWithEmbeddingsAndWebsiteInformations('urlsGottenByGooglesearchIGV_2', 'embeddings')
#addUrlsOfDbToAnotherDbWithEmbeddingsAndWebsiteInformations('urlsFoundDuring', 'embeddings')
addUrlsOfDbToAnotherDbWithEmbeddingsAndWebsiteInformations('urlsFromDashboards', 'embeddings')
