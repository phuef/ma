# This file is adapted from my bachelor thesis, which can be found here:https://github.com/phuef/ba
# A published short paper of the thesis can be found here: https://agile-giss.copernicus.org/articles/4/27/2023/agile-giss-4-27-2023.pdf

#ToDo: Comment all the functions properly 

import json

def isAStringOfArray2InAStringOfArray1(array1, array2):
    '''
    returns if any string of an array is in any of the strings of another array
    '''
    for a1 in array1:
        for a2 in array2:
            if a2 in a1:
                return True
    return False

# C4
def includesIVFrameworkName(array):
    '''
    Returns whether any of the strings in an array 
    is similar to any of the strings which are associated with IV frameworks
    '''
    ivFrameworkNames =['highcharts', 'recharts', 'tableau', 'd3', 'apexcharts', 'chartkick', 'amcharts', 'dataviz']
    return isAStringOfArray2InAStringOfArray1(array, ivFrameworkNames)
# C5
def includesIGVFrameworkName(array):
    '''
    Returns whether any of the strings in an array 
    is similar to any of the strings which are associated with IGV frameworks
    '''
    igvFrameworkNames =['leaflet', 'cartodb', 'earth-js', 'earth.js', 'esri', 'mapboxgl', 'cartovista', 'strava', 'mangomap', 'amcharts', 'maptiler']
    return isAStringOfArray2InAStringOfArray1(array, igvFrameworkNames)
# C6
def containsPhraseWhichIndicatesItIsAnIV(description, title):
    phrases=['interactive', 'interactive visualisierung', 'Datenvisualisierung']
    db=isAStringOfArray2InAStringOfArray1(description, phrases)
    tb=isAStringOfArray2InAStringOfArray1(title, phrases)
    return db or tb
# C7
def containsPhraseWhichIndicatesItIsAnIGV(description, title):
    phrases=['map', 'interactive', 'geovisualisierung', 'geovisualization']
    db=isAStringOfArray2InAStringOfArray1(description, phrases)
    tb=isAStringOfArray2InAStringOfArray1(title, phrases)
    return db or tb
# C8
def containsElementWithIdWhichIndicatesItIsAnIV(elementIds):
    ids=['apexcharts', 'highchart', 'viz', 'viz-client-container'] # viz mit reinnehmen?
    return isAStringOfArray2InAStringOfArray1(elementIds, ids)
# C9
def containsElementWithIdWhichIndicatesItIsAnIGV(elementIds):
    ids=['map', 'globe', 'county-map', 'cartoVistaDiv', 'mapholder']
    return isAStringOfArray2InAStringOfArray1(elementIds, ids)
# C10
def containsElementWithClassWhichIndicatesItIsAnIV(classNames):
    classIds=['apexcharts', 'tableau','highchart', 'recharts', 'VictoryContainer', 'rv-xy-plot', 'v-charts', 'map']
    return isAStringOfArray2InAStringOfArray1(classNames, classIds)
# C11
def containsElementWithClassWhichIndicatesItIsAnIGV(classNames):
    classIds=['esri', 'esri-map', 'mapboxgl', 'cortoVista', 'leaflet']
    return isAStringOfArray2InAStringOfArray1(classNames, classIds)

# helpfunction two of {C7,C9,C11}
def areTwoOfC7C9C11True(description, title, elementIds, classNames):
    phrase=containsPhraseWhichIndicatesItIsAnIGV(description, title)
    id=containsElementWithIdWhichIndicatesItIsAnIGV(elementIds)
    clas=containsElementWithClassWhichIndicatesItIsAnIGV(classNames)
    if clas and phrase:
        return True
    elif clas and id:
        return True
    elif phrase and id:
        return True
    else:
        return False

# helpfunction two of {C6,C8,C10}
# ToDo: 
def areTwoOfC6C8C10True(description, title, elementIds, classNames):
    phrase=containsPhraseWhichIndicatesItIsAnIV(description, title)
    id=containsElementWithIdWhichIndicatesItIsAnIV(elementIds)
    clas=containsElementWithClassWhichIndicatesItIsAnIV(classNames)
    if clas and phrase:
        return True
    elif clas and id:
        return True
    elif phrase and id:
        return True
    else:
        return False

# C1 is true if C4 or two of {C6, C8, C10} are true 
def isIV(external_links, external_scripts, description, content, elementIds, classNames):
    if includesIVFrameworkName(external_links) or includesIVFrameworkName(external_scripts):
        return True
    elif areTwoOfC6C8C10True(description, content, elementIds, classNames):
        return True
    else:
        return False
    
# C2 is true if C5 or two of {C7, C9, C11} are true 
def isIGV(external_links, external_scripts, description, content, elementIds, classNames):
    '''
    Decides, based on a set of feature information, whether a website is an IGV or not. 
    The classification is done accordingly to this short paper:    
    https://agile-giss.copernicus.org/articles/4/27/2023/agile-giss-4-27-2023.pdf
    '''
    if includesIGVFrameworkName(external_links) or includesIGVFrameworkName(external_scripts):
        return True
    elif areTwoOfC7C9C11True(description, content, elementIds, classNames):
        return True
    else:
        return False


    
def classify(featureInformation): #ToMaDo: add a function, that classifies a website only with the url
    '''
    Classifies the type of a website through a set of feature information.
    The syntax of the feature information has to be a json with the following attributes:

    {   
        url: String,
        content: String,
        description: String,
        external_links: Array,
        external_scripts:Array,
        div_ids: Array,
        div_classes: Array
    }

    '''
    #print(featureInformation)
    fi=featureInformation
    if isIGV(fi['external_links'],fi['external_scripts'], fi['description'], fi['content'], fi['div_ids'], fi['div_classes']):
        return('IGV')
    elif isIV(fi['external_links'],fi['external_scripts'], fi['description'], fi['content'], fi['div_ids'], fi['div_classes']):
        return('IV')
    else:
        return('noIV')
    

def classifyUrl(url):
    classify(
        {   
        'url': url,
        'content': String,
        'description': String,
        'external_links': Array,
        'external_scripts':Array,
        'div_ids': Array,
        'div_classes': Array
    }
    )