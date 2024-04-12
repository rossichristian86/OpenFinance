import yfinance as yf
import json

class YahooDownloader():

    OUTDIR = ".out/"

    def __init__(self) -> None:
        pass

    def getFinancials(self, symbolStr:str):

        symbolStr.upper()


        symbol = yf.Ticker(symbolStr.upper())

        # get all stock info
        symbol.info

        # Percorso del file su cui salvare il JSON
        file_path = YahooDownloader.OUTDIR + symbolStr + '.json'

        # Conversione del dizionario in formato JSON
        json_string = json.dumps(symbol.info)

        # Salvataggio del JSON su file
        with open(file_path, 'w') as file:
            file.write(json_string)

        # get historical market data
        #hist = symbol.history(period="1mo")

        # show meta information about the history (requires history() to be called first)
        #symbol.history_metadata

        # show actions (dividends, splits, capital gains)
        #symbol.actions
        #symbol.dividends
        #symbol.splits
        #symbol.capital_gains  # only for mutual funds & etfs

        # show share count
        #symbol.get_shares_full(start="2022-01-01", end=None)

        # show financials:

        # - income statement
        symbol.income_stmt.to_csv(YahooDownloader.OUTDIR +symbolStr + "_IS.csv")
        #symbol.quarterly_income_stmt

        # - balance sheet
        symbol.balance_sheet.to_csv(YahooDownloader.OUTDIR +symbolStr + "_BS.csv")
        #symbol.quarterly_balance_sheet

        # - cash flow statement
        symbol.cashflow.to_csv(YahooDownloader.OUTDIR + symbolStr + "_CF.csv")

        #symbol.quarterly_cashflow
        # see `Ticker.get_income_stmt()` for more options

if __name__ == "__main__":
    yd = YahooDownloader()
    yd.getFinancials("002594.SZ")