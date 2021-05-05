import yfinance as yf

def comp_summary():
    lst=(cursor.info['longBusinessSummary']).split('.')
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
def get_current_price(ticker):
    todays_data = ticker.history(period='max')
    return round((todays_data['Close'][-1]), 2)

def get_price_change(ticker):
    todays_data = ticker.history(period='max')
    return round((todays_data['Close'][-1] - todays_data['Close'][-2]), 2)

def get_price_change_percentage(ticker):
    todays_data = ticker.history(period='max')
    return round(((todays_data['Close'][-1] - todays_data['Close'][-2])/todays_data['Close'][-2])*100, 2)

def get_previous_Close():
    return (cursor.info["previousClose"])

def openPrice():
    return (cursor.info['open'])

def returnCompanyDetails(ticker, companyName):
    company = str(companyName)
    currentPrice = str(get_current_price(cursor))
    change = str(get_price_change(cursor))
    change_p = str(get_price_change_percentage(cursor)) + "%"
    open_p = str(openPrice())
    lastClose_p = str(get_previous_Close())
    return((company, currentPrice, change, change_p, open_p, lastClose_p))
#----------------------------------------------



if __name__=='__main__':
    user_input=input('Please enter the name of the company:')
    cursor=yf.Ticker(user_input)
    print(returnCompanyDetails(cursor, user_input))