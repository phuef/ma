import pymongo
from lxml import html
import requests
from estimation import classify

# DB Class enables the access to mongodb and provides multiple functions to engage with the database
class DB:
  def __init__(self, clientName, dBname):
    self.name = dBname
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[clientName]
    self.db = mydb[dBname]
    
  def printName(self):
    print(self.name)

  def find(self):
    return self.db.find()

  def printAllObjects(self):
    for x in self.db.find():
      print(x)

  def insertObject(self, jsonObject):
    self.db.insert_one(jsonObject)
  
  # inserts a list of  
  def insertList(self, jsonObjects):
    for jsonObject in jsonObjects:
      self.db.insert_one(jsonObject)

# takes a list of urls ([url1, url2, url3]) as input and transforms it with the  
class UrlList: 
  def __init__(self, listOfUrls):
    self.list=listOfUrls
  
  def getJson(self):
    array= []
    for x in self.list:
      array.append({"url":x})
    return array

class Url:
  def __init__(self, url):
    self.url=url
    #self.estimated_type= classify(url) # ToDo: add the estimated type as done in the bachelor thesis
    self.real_type= "" # has to be added later manually, after annotating
    self.feature_information= {
    
    }
  # returns the HTML information for a 
  def getHtmlInformationForXpathString0(self, tree, string):
    return tree.xpath(string)[0] if tree.xpath(string) !=[] else ''
  
  def getHtmlInformationForXpathString(self, tree, string):
    return tree.xpath(string) if tree.xpath(string) !=[] else ''
  
  def getFeatureInformation(self):
    
    page = requests.get(self.url)
    tree = html.fromstring(page.content)
    # fill the array with the feature information, which are extracted via xpath
    content = self.getHtmlInformationForXpathString0(tree, "//meta[@name='keywords']/@content")
    description = self.getHtmlInformationForXpathString0(tree, "//meta[@name='description']/@content")
    #keywords = tree.xpath("//meta[@name='keywords']/@content")[0] if tree.xpath("//meta[@name='keywords']/@content") !=[] else ''
    external_links = self.getHtmlInformationForXpathString(tree, "//link/@href")
    external_scripts = self.getHtmlInformationForXpathString(tree, "//script/@src")
    div_ids = self.getHtmlInformationForXpathString(tree, "//div/@id")
    div_classes = self.getHtmlInformationForXpathString(tree, "//div/@class")
    return {
      "url": self.url, 
      "content": content,
      "description": description,
      "external_links": external_links,
      "external_scripts": external_scripts,
      "div_ids": div_ids,
      "div_classes": div_classes
    }
  
  def getWebsiteInformation(self):
    featureInformation=self.getFeatureInformation()
    return {
      "url": self.url,
      "estimated_type": classify(featureInformation),
      "real_type": "",
      "feature_information": featureInformation,
    }

'''
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["websites"]

# creation of the  collections
#Collection_noIV = mydb["noIV"]
#Collection_IV = mydb["IV"]
#Collection_IGV = mydb["IGV"]
Collection_allWebsites=mydb["allWebsites"]

mydict = { "id": 0, "url": "www.google.de","estimated_type": "noIV", "real_type": ""}
mydict2 = { "id": 1, "url": "https://wiediversistmeingarten.org/view/","estimated_type": "IGV", "real_type": "IGV"}

mylist = [mydict, mydict2]

Collection_allWebsites.insert_many(mylist)


for x in Collection_allWebsites.find():
  print(x)



#def createNewEntryForDB(id, url, estimated_type, real_type, )

'''

# for each