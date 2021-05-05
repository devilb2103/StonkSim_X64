import yfinance as yf
import time
import ui_functions

class stockFunctions():
    
    def comp_summary(self, YFcursor):
        lst=(YFcursor.info['longBusinessSummary']).split('.')
        return ('.'.join(lst[:2]))

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
    def returnCompanyDetails(self, companyName):
        cursor = yf.Ticker(companyName)
        company = str(companyName)
        currentPrice = str(stockFunctions.get_current_price(self, cursor)) + "$"
        change = str(stockFunctions.get_price_change(self, cursor))
        change_p = str(stockFunctions.get_price_change_percentage(self, cursor)) + "%"
        open_p = str(stockFunctions.openPrice(self, cursor))
        lastClose_p = str(stockFunctions.get_previous_Close(self, cursor))
        result = ((company, currentPrice, change, change_p, open_p, lastClose_p))
        print(result)
        ui_functions.UIFunctions.setDebugLine(self, result, ui_functions.debugGreen)
    #----------------------------------------------