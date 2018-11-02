import requests #importing the requests library

#ask for what to query
queryhere=input("What would you like to search for?")

#send a request for the search results to the google custom search api
linkhere="https://www.googleapis.com/customsearch/v1?key=AIzaSyCSISSUjHuG4ToMOfEiZ2I5TkBCFBc9-6g&cx=011892775337292349585:w-jjunqmf6a&q="+queryhere
response=requests.get(linkhere)

#print results in a readable manner
for i in range(len(response.json()["items"])):
    print("Title: "+response.json()["items"][i]["title"]) #print the result title
    print("Link: "+response.json()["items"][i]["link"])#print the result link
    print("More info: "+response.json()["items"][i]["snippet"]+"\n")#print more info about the result
    
