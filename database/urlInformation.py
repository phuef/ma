from modules import DB, UrlList, Url

dbOnlyUrls = DB("websites", "onlyUrls")
#dbAllWebsites = DB("websites", "allWebsites") is this db still needed?
dbWithInformation = DB("websites", "withInformation")

Urls = []

# extracts website information for each website, that exist in the onlyUrls database. 
for x in dbOnlyUrls.find():
    #print(x)
    print(x['url'])
    #print(Url(x['url']).getWebsiteInformation())
    # ToDo: Check whether a url is already added to the database 
    if dbOnlyUrls.find({ "url": x['url']}):
        print(f'url {x["url"]} is already in the database')
    else:
        try:
            Urls.append(Url(x['url']).getWebsiteInformation())
            print(f'website {x["url"]} was added successfully to the database')
        except:
            print(f'website {x["url"]} could not be added, due to some mistake')

    
## adds these extracted information to the database
dbWithInformation.insertList(Urls)
