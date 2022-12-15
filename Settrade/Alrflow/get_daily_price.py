import yfinance as yf
import pandas as pd
import logging
import datetime
logging.basicConfig(level=logging.INFO, filename="Settrade/Alrflow/scrape_price_dialy.log", filemode='w')


def get_file():
    def get_price(df_all,name,period="1d", interval="1d"):
        name_bk = f"{name.upper()}.BK"
        stock = yf.Ticker(name_bk)
        df = stock.history(period=period, interval=interval)

        if df.shape[0] != 0:
            df['symbol'] = name_bk.split(".")[0]
            df_all = pd.concat([df_all,df])
            logging.info(f"{name} pass")
        else:
            logging.warn(f"{name} error")
        return df_all

    symbols = pd.read_csv("Settrade/company_name.csv",index_col=0)
    symbols = symbols[symbols.market=="SET"]["name"]
    n = len(symbols)
    df_all = pd.DataFrame()
    for i,name in enumerate(symbols):
        if i%50==0:
            print(f"Symbol {i}/{n}")
        df_all = get_price(df_all, name)
    df_all.to_csv(f'Settrade/Alrflow/daily_get_{datetime.datetime.date()}.csv')
    print('Finish!!')
    logging.info(f"Daily process {datetime.datetime.now()} pass")
    

def concat():
    df_all = pd.read_csv("Settrade/Dataset/SET_index_historical_price.csv")
    df_daily = pd.read_csv("Settrade/Alrflow/daily_scrape.csv")
    df_all = pd.concat([df_all,df_daily])
    df_all.to_csv("Settrade/Dataset/SET_index_historical_price.csv")
    logging.info(f"Update daily price {datetime.datetime.now()} pass")

    



