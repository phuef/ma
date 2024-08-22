# The synonyms and topics were gathered with the help of the large language model (LLM) ChatGPT (https://chat.openai.com/)

from modules import DB, QueryList

synonymsForIV = [
  "Interactive visualization",
  "Data visualization tool",
  "Web-based data visualization",
  "Interactive chart and graph",
  "Visual analytics",
  "Dynamic data presentation",
  "Online interactive dashboard",
  "Interactive map",
  "Real-time data visualization",
  "Data-driven storytelling",
  "Infographic tool",
  "Graphical data exploration",
  "Interactive data representation",
  "Multimedia data visualization",
  "User-friendly data visualization"
]

synonymsForIGV = [
  "Interactive geovisualizations",
  "Geospatial data visualization",
  "Interactive map",
  "map",
  "Map-based data exploration",
  "Dynamic geographic visualizations",
  "Interactive GIS",
  "Geospatial analytics",
  "Real-time map visualizations",
  "Interactive cartography",
  "Web-based geovisualization",
  "Location-based data visualization",
  "Spatial data exploration",
  "Interactive mapping tool",
  "GIS",
  "Geographic data storytelling"
]

current_topics = [
    "Climate change",
    "global warming",
    "COVID-19 pandemic",
    "Renewable energy solutions",
    "Artificial intelligence and machine learning",
    "Cybersecurity threats",
    "Space exploration and colonization",
    "Sustainable agriculture",
    "Vaccination debates",
    "Political polarization",
    "Economic inequality",
    "5G technology deployment",
    "Mental health awareness",
    "Social media impact on society",
    "Rise of digital currencies",
    "Global refugee crisis",
    "LGBTQ+ rights",
    "Gender equality",
    "Remote work trends",
    "Sustainable fashion",
    "Advances in medical research",
    "Geopolitical tensions",
    "Automation and job displacement",
    "Water scarcity and conservation",
    "Biotechnology breakthroughs",
    "Rise of populism",
    "Education reform",
    "Infrastructure development",
    "Environmental conservation efforts",
    "Genomic editing",
    "Aging population challenges",
    "Mental health impacts of social media",
    "Ongoing conflicts in the Middle East",
    "Clean energy policies",
    "Wildlife conservation",
    "Nuclear disarmament efforts",
    "Drug legalization debates",
    "3D printing advancements",
    "Rise of electric vehicles",
    "Global health crises beyond COVID-19",
    "Cultural appropriation discussions",
    "Quantum computing developments",
    "plant-based diets",
    "Plastic waste reduction initiatives",
    "Internet censorship",
    "Indigenous rights movements",
    "Emerging technologies in healthcare",
    "Antibiotic resistance",
    "Universal basic income discussions",
    "National and international responses to natural disasters"
]

past_topics = [
    "Y2K Bug",
    "The Cold War",
    "Dot-com bubble",
    "Napster and the file-sharing era",
    "The Great Depression",
    "Prohibition",
    "Moon landing (Apollo missions)",
    "Vietnam War protests",
    "Berlin Wall fall",
    "Disco era",
    "The Watergate scandal",
    "Woodstock Festival",
    "The Roaring Twenties",
    "Hula Hoop craze",
    "Cuban Missile Crisis",
    "Breakup of the Soviet Union",
    "The Space Race",
    "Beatniks and counterculture",
    "The Jazz Age",
    "Civil Rights Movement",
    "The Salem Witch Trials",
    "Titanic sinking",
    "World War I",
    "Spanish Flu pandemic (1918)",
    "Women's suffrage movement",
    "Great Fire of London (1666)",
    "Renaissance era",
    "Black Plague",
    "The Industrial Revolution",
    "Salem Witch Trials",
    "Mayan civilization",
    "Greek mythology",
    "The Renaissance",
    "The Enlightenment",
    "The Great Wall of China construction",
    "Ancient Egyptian civilization",
    "Sinking of the Titanic",
    "Spanish Inquisition",
    "Aztec civilization",
    "Roman Empire",
    "Mongol Empire",
    "The Age of Exploration",
    "The Black Death",
    "The Crusades",
    "Ancient Greece",
    "Mesopotamian civilizations"
]

current_spatial_topics = [
    "Urbanization trends",
    "Smart cities development",
    "Climate change impact on sea levels",
    "Deforestation in the Amazon rainforest",
    "Arctic melting",
    "Rising sea temperatures",
    "coral bleaching",
    "Global migration patterns",
    "City congestion and traffic management",
    "Renewable energy projects in specific regions",
    "Urban sprawl and its consequences",
    "Land use changes affecting biodiversity",
    "Natural disasters and spatial risk assessment",
    "GIS (Geographic Information System) applications",
    "Air pollution in metropolitan areas",
    "Coastal erosion and protection strategies",
    "Satellite technology for Earth observation",
    "Impact of climate change on agriculture zones",
    "Spatial distribution of wildlife habitats",
    "Transboundary water management",
    "Renewable energy potential in different regions",
    "Spatial planning for disaster resilience",
    "Biodiversity hotspots and conservation efforts",
    "Mapping and monitoring of invasive species",
    "Spatial analysis of disease outbreaks",
    "Migration routes of endangered species",
    "Spatial aspects of global trade routes",
    "Land reclamation projects",
    "Urban heat island effects",
    "Spatial aspects of renewable resource management",
    "Mapping of cultural heritage sites",
    "Spatial patterns of air quality",
    "Effects of urbanization on local ecosystems",
    "Spatial disparities in healthcare access",
    "Geopolitical borders and disputes",
    "Spatial patterns of deforestation and reforestation",
    "Impact of industrial zones on nearby communities",
    "Spatial dimensions of sustainable development goals",
    "Mapping of indigenous territories",
    "Spatial considerations in disaster response",
    "Aquifer depletion and groundwater management",
    "Spatial planning for renewable energy installations",
    "Mapping of food deserts in urban areas",
    "Spatial aspects of infrastructure development",
    "Border security and surveillance technology",
    "Spatial analysis of crime patterns",
    "Urban green spaces and their distribution"
]

# ToDo: past_spatial_topics = []


synonymsForIGV_SecondTry = [
  "interactive map",
  "dynamic map",
  "online map",
  "web map",
  "map"
]

topicsIGV_SecondTry=[
    'weather',
    'radar',
    'satellite',
    'forecast',
    'air pollution',
    'borders',
    'city',
    'heritage',
    'tracking',
    'sustainability',
    'transport',
    'patterns',
    'tracking',
    'animals',
    'territories',
    'earthquake',
    'analysis',


]
def createIVSearchQueries():
    '''Creates a list of search queries to find IV's in a search. 
    The search queries are combined with a set of synonyms for IV's and a set of topics.
    The topics are splitted into current and past topics, 
    which were generated through the large language model (LLM) ChatGPT.
    '''
    ivQueries=[]
    for iv in synonymsForIV:
        for current_topic in current_topics:
            ivQueries.append(f'{iv} {current_topic}')
        for past_topic in past_topics:
            ivQueries.append(f'{iv} {past_topic}')
    print(f'{len(ivQueries)} IV search queries were created')
    return(ivQueries)

def saveIVQueriesToDB():
    '''saves a set of generated search queries for interactive visualisations (IV) 
    in the mongodb database searchQueries.IV'''
    ivSearchQueries = createIVSearchQueries()
    dB = DB('searchQueries', 'IV')
    queries = QueryList(ivSearchQueries)
    dB.insertList(queries.getJson())
    dB.insertList(ivSearchQueries)

def createIGVSearchQueries():
    '''Creates a list of search queries to find IGV's in a search. 
    The search queries are combined with a set of synonyms for IGV's and a set of topics.
    The topics are splitted into current and past topics, spatial, 
    which were generated through the large language model (LLM) ChatGPT.
    '''
    igvQueries=[]
    for synonymForIGV in synonymsForIGV:
        for current_spatial_topic in current_spatial_topics:
            igvQueries.append(f'{synonymForIGV} {current_spatial_topic}')
        for past_spatial_topic in past_topics: #ToDo: gather spatial topics and replace pst topics with them
            igvQueries.append(f'{synonymForIGV} {past_spatial_topic}')
    print(f'{len(igvQueries)} IGV search queries were created')
    return igvQueries

def saveIGVQueriesToDB():
    '''saves a set of generated search queries for interactive geovisualisations (IGV) 
    in the mongodb database searchQueries.IGV'''
    igvSearchQueries = createIGVSearchQueries()
    dB = DB('searchQueries', 'IGV')
    queries = QueryList(igvSearchQueries)
    dB.insertList(queries.getJson())

def saveQueriesToDB(queries, dbName):
    '''saves a set of generated search queries into a mongodb database. 
    Takes a list of '''
    dB = DB('searchQueries', dbName)
    queries = QueryList(queries)
    print(queries.getJson())
    dB.insertList(queries.getJson())

def addQueriesToDB(queries, dbName):
    '''adds a set of generated search queries for interactive geovisualisations (IGV) 
    in the mongodb database searchQueries.IGV'''
    print(queries)
    dB = DB('searchQueries', dbName)
    queries = QueryList(queries)
    dB.insertList(queries.getJson())

#second try
def createIGVSearchQueries_secondTry():
    '''Creates a list of search queries to find IGV's in a search. 
    The search queries are combined with a set of synonyms for IGV's and a set of topics.
    The topics are splitted into current and past topics, spatial, 
    which were generated through the large language model (LLM) ChatGPT.
    '''
    igvQueries=[]
    for synonymForIGV in synonymsForIGV_SecondTry:
        for current_spatial_topic in topicsIGV_SecondTry:
            igvQueries.append(f'{synonymForIGV} {current_spatial_topic}')
    print(f'{len(igvQueries)} IGV search queries were created')
    return igvQueries

'''Step 1 - creating a set of search queries for IV's 
and saving them to the database searchQueries.IV'''
#saveIVQueriesToDB()

'''Step 2 - creating a set of search queries for IGV's 
and saving them to the database searchQueries.IGV'''
#saveIGVQueriesToDB()


# ToMaDo
'''Step 3 - creating a set of search queries for noIV's 
and saving them to the database searchQueries.noIV'''
# Only do this if not enough noIV's were collected in the steps before 

'''
Second Try with advanced queries to get better results'''

saveQueriesToDB(createIGVSearchQueries_secondTry(), 'IGV_2') # <- generalized function to get rid of unneccessary code junk
addQueriesToDB()