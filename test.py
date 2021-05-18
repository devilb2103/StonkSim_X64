import requests

def returnCompanyDetails2(Ticker, companyName):
        url = "https://alpha-vantage.p.rapidapi.com/query"
        querystring = {"function":"GLOBAL_QUOTE","symbol":str(Ticker)}
        headers = {
            'x-rapidapi-key': "b74bc782femsh2b453fc4f4a1d9ep14a862jsnf12343e8143e",
            'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        dictionary = response.json()["Global Quote"]
        return [(companyName, dictionary["05. price"], dictionary["09. change"], 
                    dictionary["10. change percent"], dictionary["02. open"], 
                    dictionary["08. previous close"])]

print(returnCompanyDetails2("tsla", "tesla"))