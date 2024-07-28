import pymongo
from lxml import html
import requests
from estimation import classify

# DB Class enables the access to mongodb and provides multiple functions to interact with the database
class DB:
  def __init__(self, clientName, dBname):
    self.name = dBname
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[clientName]
    self.db = mydb[dBname]
    
  def printName(self):
    print(self.name)

  def find(self, query, *returnedFields):
    if query and returnedFields: 
      return self.db.find(query, returnedFields)
    elif query:
      return self.db.find(query)
    else:
      return self.db.find()
  
  def find_one(self, query):
    return self.db.find_one(query)
    
  def update_one(self, query, update):
    return self.db.update_one(query, update)
  
  def updateMany(self, filter, update):
    return self.db.update_many(filter, update)
  
  def count_documents(self, filter):
    return self.db.count_documents(filter)
  
  def printAllObjects(self):
    for x in self.db.find():
      print(x)

  def insertObject(self, jsonObject):
    self.db.insert_one(jsonObject)
  
  # inserts a list of Json Objects into the database
  def insertList(self, jsonObjects):
    for jsonObject in jsonObjects:
      self.db.insert_one(jsonObject)

# takes a list of urls ([url1, url2, url3]) as input and transforms it with the  
class UrlList: 
  def __init__(self, listOfUrls):
    self.list=listOfUrls

  def getJson(self):
    '''
    returns an array with json objects of the format {"url": url }
    '''
    array= []
    for x in self.list:
      array.append({"url":x})
    return array

class QueryList: 
  def __init__(self, listOfQueries):
    self.list=listOfQueries
  
  def getJson(self):
    '''
    returns an array with json objects of the format {"query": query }
    '''
    array= []
    for x in self.list:
      array.append({"query":x})
    return array

class Url:
  '''
  Represents an URL. Takes a url as string as input.
  '''
  def __init__(self, url):
    self.url=url
    self.real_type= "" # has to be added later manually, after annotating
    
  def getHtmlInformationForXpathString0(self, tree, string):
    '''
    returns HTML information for a xpath string
    '''
    return tree.xpath(string)[0] if tree.xpath(string) !=[] else ''
  
  def getHtmlInformationForXpathString(self, tree, string):
    '''
    returns HTML information for a xpath string
    '''
    return tree.xpath(string) if tree.xpath(string) !=[] else ''
  
  def getHtml(self):
    page = requests.get(self.url)
    return page.text

  def getFeatureInformation(self):
    '''
    get the feature information needed to classify websites
    @return JSON 
    '''
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
  
  def getLinks(self):
    page = requests.get(self.url)
    tree = html.fromstring(page.content)
    external_links = self.getHtmlInformationForXpathString(tree, "//a/@href")
    return external_links
  
  def getLinksWithPhrase(self, phrase):
    try:
      page = requests.get(self.url)
      tree = html.fromstring(page.content)
    except:
      print("error in getLinksWithPhrase()")
    external_links = self.getHtmlInformationForXpathString(tree, f"//a[contains(@href,'{phrase}')]/@href")
    return external_links
    
  def getWebsiteInformation(self):
    '''
    returns a json, with information about the website
    the returned Json looks like the following
    
    '''
    featureInformation=self.getFeatureInformation()
    return {
      "url": self.url,
      "estimated_type": classify(featureInformation),
      "real_type": "",
      "feature_information": featureInformation,
    }
  
  def getJsonToAddToDb(self):
    '''returns a json with only the url {"url": url}'''
    return {"url": self.url}
  
def isAlreadyInDb(url, database):
    '''returns True if the url is already in the database. Takes an url as String and a mongodb database as input '''
    return True if database.find_one({"url": url}) else False