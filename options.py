
import pandas_datareader.data as data
import yfinance as yf
import pandas as pd
import sys
import os
from datetime import date


yf.pdr_override()


sp_table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
sp_list = sp_table[0]['Symbol'].tolist()
if not sp_list[0] == 'MMM' or not sp_list[-1] == 'ZTS':
    print("Shit's fucked")


def unusual_activity(calls_or_puts, exp_date, stocklist):
    """
    unusualActivity scans yahoo finance for a list of stocks and returns contracts showing unusually high
    volume/open interest
    Args:
    calls_or_puts (str): do you want to return calls or puts?
    exp_date (str): date of contract expiry
    stocklist (list[str]): list of tickers to loop through
    """
    # We're going to suppress prints b/c datareader is annoying then restore printing so this helps
    old_stdout = sys.stdout
    finaldf = pd.DataFrame()
    for x in stocklist:
        ticker = yf.Ticker(x)
        try:
            opt = ticker.option_chain(exp_date)
            if calls_or_puts == 'calls':
                # Suppress prints
                sys.stdout = open(os.devnull, "w")
                # Add some info about ticker and UL price to our dataframe
                opt.calls.insert(0, 'Symbol', x)
                opt.calls.insert(3, 'stock_price', data.get_data_yahoo(x, end_date=date.today())['Close'][-1])
                # Calculate our volume/open interest, this is how we define unusual activity
                opt.calls['V/OI'] = (opt.calls['volume'].astype('float') / opt.calls['openInterest'])
                # Inside of the brackets is where we apply our filter to get the
                # unusual stuff. Feel free to mess with this in your own version
                finaldf = finaldf.append(opt.calls[(opt.calls['volume'].astype('float') / opt.calls[
                    'openInterest'] > .5) & (opt.calls['openInterest'] > 200)])
            elif calls_or_puts == 'puts':
                sys.stdout = open(os.devnull, "w")
                opt.puts.insert(0, 'Symbol', x)
                opt.puts.insert(3, 'stock_price', data.get_data_yahoo(x, end_date=date.today())['Close'][-1])
                opt.puts['stock_price'] = data.get_data_yahoo(x, end_date=date.today())['Close'][-1]
                opt.puts['V/OI'] = (opt.puts['volume'].astype('float') / opt.puts['openInterest'])
                finaldf = finaldf.append(opt.puts[(opt.puts['volume'].astype('float') / opt.puts[
                    'openInterest'] > .5) & (opt.puts['openInterest'] > 200)])
            else:
                print('set calls_or_puts equal to calls or puts retard')
                break
        except:
            pass
        break
    sys.stdout = old_stdout
    return finaldf


calls_or_puts = 'puts'
# year-month-day
exp_date = '2020-04-17'
returned = unusual_activity(calls_or_puts, exp_date, sp_list)
#Do some final formatting changes
returned = returned.drop(columns = ['contractSymbol', 'lastTradeDate', 'contractSize', 'currency'])
returned.insert(3, 'Distance OTM', returned['stock_price'] - returned['strike'])
returned['Value'] = returned['openInterest']*returned['lastPrice']*100
print returned
