:information_source: This repository contains the code for the following work: Hüffer, P., Degbelo, A. and Risse, B. (2025) ‘Geovicla: automated classification of interactive web-based geovisualizations’, in 13th International Conference on Geographic Information Science (GIScience 2025), Christchurch, New Zealand.

# :earth_africa: Topic of the work 

For more details about the work, see Hüffer, P., Degbelo, A. and Risse, B. (2025) ‘Geovicla: automated classification of interactive web-based geovisualizations’, in 13th International Conference on Geographic Information Science (GIScience 2025), Christchurch, New Zealand.

# Structure of the repository

In the 'database' folder are all the files. Including scripts to harvest webpages, process the data and run the machine learning classifiers. 


## :open_file_folder: Files
### :snake: credentials.py 

Stores the credentials, necessary for the google search. If you want to use the search yourself, you need to create a *cse* (**c**ustom **s**earch **e**ngine) [here:link:](https://cse.google.com/) and get yourself an api key [here:link:](https://developers.google.com/custom-search/v1/introduction?hl=de). Create a file called **credentials.py** in the database folder and insert the ids in the format as shown below.

```python
cse_id = 'insert_your_cse_id_here'
api_key = 'insert_your_api_key_here'
```

### :snake: manualClassification.py

Executing this file starts an interactive console, to classify websites of a mongodb database <span style="color:green"> websites.\*dbName\*</span>. One database entry that do not have a value for the field <span style="color:green">*"real_type"*</span>, will be opened in the browser. The console asks then for a classification input and saves it in the database, after entered. After that the next webpage from the database is opened.

### :snake: searchQueryBuilder.py

This File builds search queries used in the <span style="color:grey">automatedSearch.py</span>.  

### :snake: automatedSearch.py

Provides a funtion that conducts an automated search for a given query. Returns search results for the query. 

### :snake: mlModules.py
In this file is the logic for the machine learning classifiers. The files mlp.py, svm.py, nb.py and rf.py use this module.



#### README legend 

Everything related to <span style="color:green"> mongodb</span> is green

<span style="color:grey">File names </span> are displayed in grey.



#### If you have any questions about this repository, don't hesitate to contact me.
