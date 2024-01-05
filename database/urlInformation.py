from modules import DB, UrlList, Url

dbOnlyUrls = DB("websites", "onlyUrls")
dbAllWebsites = DB("websites", "allWebsites")
dbWithInformation = DB("websites", "withInformation")

Urls = []
for x in dbOnlyUrls.find():
    print(x)
    print(x['url'])
    #print(Url(x['url']).getWebsiteInformation())
    try:
        Urls.append(Url(x['url']).getWebsiteInformation())
    except:
        print(f'website {x["url"]} could not be added')

    
dbWithInformation.insertList(Urls)
