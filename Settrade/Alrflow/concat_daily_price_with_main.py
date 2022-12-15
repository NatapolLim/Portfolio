import pandas as pd
import logging
import datetime
logging.basicConfig(level=logging.INFO, filename="Settrade/Alrflow/scrape_price_dialy.log", filemode='w')

def concat():
    df_all = pd.read_csv("Settrade/Dataset/SET_index_historical_price.csv")
    df_daily = pd.read_csv("Settrade/Alrflow/daily_scrape.csv")
    df_all = pd.concat([df_all,df_daily])
    df_all.to_csv("Settrade/Dataset/SET_index_historical_price.csv")
    logging.info(f"Update daily price {datetime.datetime.now()} pass")