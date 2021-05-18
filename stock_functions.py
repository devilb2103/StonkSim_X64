import yfinance as yf
import time
import ui_functions
import requests

class stockFunctions():
    
    # def comp_summary(self, YFcursor):
    #     lst=(YFcursor.info['longBusinessSummary']).split('.')
    #     return ('.'.join(lst[:2]))

    # def full_info():
    #     return (cursor.info)

    # def reg_day_high():
    #     return (cursor.info['regularMarketDayHigh'])

    # def reg_day_low():
    #     return (cursor.info['regularMarketDayLow'])

    # def logo_return():
    #     return (cursor.info['logo_url'])

    # def week_low_52():
    #     return (cursor.info['fiftyTwoWeekLow'])

    # def week_high_52():
    #     return (cursor.info['fiftyTwoWeekHigh'])

    # WHAT WE NEED--------------------------------

    # GETS LATEST CHARE PRICE OF COMPANY
    def get_current_price(self, YFcursor):
        todays_data = YFcursor.history(period='max')
        return round((todays_data['Close'][-1]), 2)

    # GETS CHANGE IN PRICE 
    def get_price_change(self, YFcursor):
        todays_data = YFcursor.history(period='max')
        return round((todays_data['Close'][-1] - todays_data['Close'][-2]), 2)

    # GETS PERCENTAGE CHANGE IN PRICE 
    def get_price_change_percentage(self, YFcursor):
        todays_data = YFcursor.history(period='max')
        return round(((todays_data['Close'][-1] - todays_data['Close'][-2])/todays_data['Close'][-2])*100, 2)

    # GETS PREVIOUS SHARE CLOSE PRICE
    def get_previous_Close(self, YFcursor):
        return (YFcursor.info["previousClose"])

    # GETS COMPANY SHARE'S DAY'S OPEN PRICE
    def openPrice(self, YFcursor):
        return (YFcursor.info['open'])

    # RETURNS ALL THE REQUIRED OUTPUT OF THE FUNTIONS FOR WRITING TO THE DATABASE
    def returnCompanyDetails(self, Ticker, CompanyName):
        cursor = yf.Ticker(Ticker)
        company = str(CompanyName)
        currentPrice = str(stockFunctions.get_current_price(self, cursor)) + "$"
        change = str(stockFunctions.get_price_change(self, cursor))
        change_p = str(stockFunctions.get_price_change_percentage(self, cursor)) + "%"
        open_p = str(stockFunctions.openPrice(self, cursor))
        lastClose_p = str(stockFunctions.get_previous_Close(self, cursor))
        result = ((company, currentPrice, change, change_p, open_p, lastClose_p))
        print(result)
        ui_functions.UIFunctions.setDebugLine(self, result, ui_functions.debugGreen)
    
    #----------------------------------------------------------------------------------
    
    ## RAPID API - ALPHA VANTAGE
    # RETURNS ALL THE REQUIRED OUTPUT OF THE FUNTIONS FOR WRITING TO THE DATABASE
    def returnCompanyDetails2(self, Ticker, companyName):
        url = "https://alpha-vantage.p.rapidapi.com/query"
        querystring = {"function":"GLOBAL_QUOTE","symbol":str(Ticker)}
        headers = {
            'x-rapidapi-key': "b74bc782femsh2b453fc4f4a1d9ep14a862jsnf12343e8143e",
            'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        dictionary = response.json()["Global Quote"]
        
        result =  ((companyName, dictionary["05. price"], dictionary["09. change"], 
                    dictionary["10. change percent"], dictionary["02. open"], 
                    dictionary["08. previous close"]))
        
        print(result)
        ui_functions.UIFunctions.setDebugLine(self, result, ui_functions.debugGreen)

    #----------------------------------------------------------------------------------
    def returnTickerSymbol(self, CompanyName):
        url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=" + CompanyName + "&lang=en"
        r = requests.get(url)
        return r.json()["ResultSet"]["Result"][0]["symbol"]
    #----------------------------------------------