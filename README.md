:information_source: This repository contains my master thesis. You can find some explanations about it in this README.  <span style="color:yellow"> TODO: Add a short summary about the thesis :exclamation: </span>

# :earth_africa: Topic of the thesis 

The thesis is about the findability and collection of geovisualisations and interactive visualisation on the web.

# Structure of the repository

In the 'harvesting' folder are files responsible for the data collection. Including scripts to scrape websites, process the data and save them in the 'database' folder.
The 'classification' folder contains files responsible for the classification of the websites. :exclamation:


## :open_file_folder: Files
### :snake: credentials.py 

Stores the credentials, necessary for the google search. If you want to use the search yourself, you need to create a *cse* (**c**ustom **s**earch **e**ngine) [here:link:](https://cse.google.com/) and get yourself an api key [here:link:](https://developers.google.com/custom-search/v1/introduction?hl=de). Create a file called **credentials.py** and insert the ids in the format as shown below.

<code>cse_id = 'insert_your_cse_id_here'
api_key = 'insert_your_api_key_here'
</code>

### :snake: manualClassification.py

Executing this file starts an interactive console, to classify websites of the mongodb database <span style="color:green"> websites.withInformation</span>. Database entry's that do not have a value for the field *"real_type"* 

### :snake: searchQueryBuilder.py

This File builds search queries used in the <span style="color:grey">automatedSearch.py</span>.  

#### Functions:
<span style="color:orange">createIVSearchQueries</span>

### :snake: automatedSearch.py

#### README legend 

<span style="color:green"> Everything related to mongodb is green</span>

<span style="color:orange">Functions: </span> are displayed in orange.

<span style="color:yellow"> Todos: </span>Tasks that still need to be done are displayed in yellow.