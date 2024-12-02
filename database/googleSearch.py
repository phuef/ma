from googleapiclient.discovery import build
from credentials import cse_id, api_key #credentials are private and not committed. See Readme, for more information 

def google_search(search_term):
    '''Does a google search for a specific search term. Returns the result of the search in a json format
    
    Example:
    google_search('interactive visualisation ')

    Explanation: Searches for the term 'interactive visualisation' and returns 10 results'
    '''
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, num=10).execute()
    return res['items']

#print(google_search("interactive visualisation"))