from yahooDownloader import YahooDownloader
import pandas as pd

TICKERDIR = ".tickerLists/"
df = pd.read_csv(TICKERDIR + "sp500.csv")
yd = YahooDownloader()

for idx, row in df.iterrows():
    print("Downloading : " + row["Symbol"])
    yd.getFinancials(row["Symbol"])