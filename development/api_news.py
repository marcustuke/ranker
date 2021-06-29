import requests

url = "https://google-news1.p.rapidapi.com/topic-headlines"

querystring = {"topic":"WORLD","country":"US","lang":"en"}

headers = {
    'x-rapidapi-key': "65d14ca226msh3d214dd3211828ap12c985jsnca370da08070",
    'x-rapidapi-host': "google-news1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
