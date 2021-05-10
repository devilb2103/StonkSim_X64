import requests
innput = str(input("Company:"))
url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=" + innput + "&region=1&lang=en"
r = requests.get(url)
print(r.json()["ResultSet"]["Result"][0]["symbol"])