# from estimation import includesIVFrameworkName, includesIGVFrameworkName, containsPhraseWhichIndicatesItIsAnIGV, containsPhraseWhichIndicatesItIsAnIV, containsElementWithClassWhichIndicatesItIsAnIGV, containsElementWithClassWhichIndicatesItIsAnIV, containsElementWithIdWhichIndicatesItIsAnIGV, containsElementWithIdWhichIndicatesItIsAnIV, isAStringOfArray2InAStringOfArray1 # not used anymore. Was part of the feature input only using the conditions

ivFrameworkNames =['highcharts', 'recharts', 'tableau', 'd3', 'apexcharts', 'chartkick', 'amcharts', 'dataviz']
igvFrameworkNames =['leaflet', 'cartodb', 'earth-js', 'earth.js', 'esri', 'mapboxgl', 'cartovista', 'strava', 'mangomap', 'amcharts', 'maptiler']
ivPhrases=['interactive', 'interactive visualisierung', 'Datenvisualisierung']
igvPhrases=['map', 'interactive', 'geovisualisierung', 'geovisualization']
ivIds=['apexcharts', 'highchart', 'viz', 'viz-client-container']
igvIds=['map', 'globe', 'county-map', 'cartoVistaDiv', 'mapholder']
ivClassIds=['apexcharts', 'tableau','highchart', 'recharts', 'VictoryContainer', 'rv-xy-plot', 'v-charts', 'map']
igvClassIds=['esri', 'esri-map', 'mapboxgl', 'cortoVista', 'leaflet']

''' #first idea of using the conditions as input
def generateFeatureInput_withConditions(featureInformation):

    fi=featureInformation
    featureInput=[]
    #C4
    featureInput.append(1 if includesIVFrameworkName(fi['external_links']) or includesIVFrameworkName(fi['external_scripts']) else 0) 
    #C5
    featureInput.append(1 if includesIGVFrameworkName(fi['external_links']) or includesIGVFrameworkName(fi['external_scripts']) else 0)
    #C6
    featureInput.append(1 if containsPhraseWhichIndicatesItIsAnIV(fi['description'], fi['content']) else 0)
    #C7
    featureInput.append(1 if containsPhraseWhichIndicatesItIsAnIGV(fi['description'], fi['content']) else 0)
    #C8
    featureInput.append(1 if containsElementWithIdWhichIndicatesItIsAnIV(fi['div_ids']) else 0)
    #C9
    featureInput.append(1 if containsElementWithIdWhichIndicatesItIsAnIGV(fi['div_ids']) else 0)
    #C10
    featureInput.append(1 if containsElementWithClassWhichIndicatesItIsAnIV(fi['div_classes']) else 0)
    #C11
    featureInput.append(1 if containsElementWithClassWhichIndicatesItIsAnIGV(fi['div_classes']) else 0)
    print('feature Input: ',featureInput)
    return featureInput
'''
def isStringInAnyStringsOfArray(string, arrayWithStrings):
    '''
    function that returns a boolean whether a string is inside any of the strings in an array'''
    for stringFromArray in arrayWithStrings:
        if string in stringFromArray:
            return True
    return False

def generateFeatureInput(featureInformation):
    '''
    generates a vector of the size 48 for a set of given feature information'''
    fi=featureInformation
    featureInput=[]
    for ivFrameworkName in ivFrameworkNames:
        featureInput.append(1 if isStringInAnyStringsOfArray(ivFrameworkName, fi['external_links']) else 0)
        featureInput.append(1 if isStringInAnyStringsOfArray(ivFrameworkName, fi['external_scripts']) else 0)
    for igvFrameworkName in igvFrameworkNames:
        featureInput.append(1 if isStringInAnyStringsOfArray(igvFrameworkName, fi['external_links']) else 0)
        featureInput.append(1 if isStringInAnyStringsOfArray(igvFrameworkName, fi['external_scripts']) else 0)
    for ivPhrase in ivPhrases:
        featureInput.append(1 if isStringInAnyStringsOfArray(ivPhrase, fi['description']) else 0)
        featureInput.append(1 if isStringInAnyStringsOfArray(ivPhrase, fi['content']) else 0)
    for igvPhrase in ivPhrases:
        featureInput.append(1 if isStringInAnyStringsOfArray(igvPhrase, fi['description']) else 0)
        featureInput.append(1 if isStringInAnyStringsOfArray(igvPhrase, fi['content']) else 0)
    for ivId in ivIds:
        featureInput.append(1 if isStringInAnyStringsOfArray(ivId, fi['div_ids']) else 0)
    for igvId in igvIds:
        featureInput.append(1 if isStringInAnyStringsOfArray(igvId, fi['div_ids']) else 0)
    for ivClassId in ivClassIds:
        featureInput.append(1 if isStringInAnyStringsOfArray(ivClassId, fi['div_classes']) else 0)
    for igvClassId in igvClassIds:
        featureInput.append(1 if isStringInAnyStringsOfArray(igvClassId, fi['div_classes']) else 0)
    #print('feature Input: ',featureInput)
    return featureInput