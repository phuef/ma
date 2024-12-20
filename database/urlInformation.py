from modules import DB, UrlList, Url

dbOnlyUrls = DB("websites", "onlyUrls")
dbWithInformation = DB("websites", "withInformation")



def getWebsiteInformationForDb(db):
    # extracts website information for each website, that exist in the onlyUrls database. 
    Urls = []
    for x in db.find():
        print(x['url'])
        # Check whether a url is already added to the database 
        if db.find({ "url": x['url']}):
            print(f'url {x["url"]} is already in the database')            
        else:
            try:
                Urls.append(Url(x['url']).getWebsiteInformation())
                print(f'website {x["url"]} was added successfully to the database')
            except:
                print(f'website {x["url"]} could not be added, due to some mistake')
    return Urls


Urls=getWebsiteInformationForDb(dbOnlyUrls)

## adds these extracted information to the database
dbWithInformation.insertList(Urls)