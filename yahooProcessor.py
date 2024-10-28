import pandas as pd
import json
import statistics

class YahooProcessor():

    OUTPUTDIR = ".out/"
    def __init__(self) -> None:
        pass

    def getRatio(self, num, den):

        out = []
        for i in range (0, len(num)):
            out.append(num[i] / den[i])

        return out
    
    def createData(self, symbol):

        hashmap = {}

        self.createDataBS(symbol, hashmap)
        self.createDataIS(symbol, hashmap)
        self.createDataInfo(symbol, hashmap)
        self.createAdditionalInfo(hashmap)

        print(hashmap)
        return hashmap

    def createAdditionalInfo(self, hashmap):

        # (LastRevenue*MedianMargin) / EnterpriseValue
        LastRevenue = hashmap["Total Revenue"][0]

        #print(hashmap["Dates"])
        #print(hashmap["Total Revenue"])
        #print(hashmap["Net Margin"])

        outL = []
        for idx in range (0, len(hashmap["Net Margin"])):
            if hashmap["Net Margin"][idx] > 0:
                outL.append(hashmap["Net Margin"][idx])


        MedianMargin = statistics.mean(outL)
        #print(MedianMargin)

        ev = (hashmap["enterpriseValue"])

        ProjectedIncome_to_enterpriseValue = (LastRevenue * MedianMargin) / ev
        #print("ProjectedIncome to enterpriseValue : " + ProjectedIncome_to_enterpriseValue)

        hashmap["ProjectedIncome to enterpriseValue"] = ProjectedIncome_to_enterpriseValue




    def createDataInfo(self, symbol, hashmap:dict):
        # Leggi il file JSON
        with open(YahooProcessor.OUTPUTDIR + symbol + ".json", 'r') as file:
            json_data = file.read()

        # Converti il JSON in un dizionario
        my_dict = json.loads(json_data)
        hashmap.update(my_dict)


    def createDataBS(self, symbol, hashmap):

        df = pd.read_csv( YahooProcessor.OUTPUTDIR + symbol + "_BS.csv")
        
        for index, row in df.iterrows():

            values = []
            for index in range (1, len(row)):
                values.append(row[index])

            hashmap[row[0]] = values

        hashmap["Dates"] = df.columns[1:].tolist()
        #print(hashmap["Dates"])

        hashmap["Book Per Share Value"] = self.getRatio(hashmap["Common Stock Equity"], hashmap["Ordinary Shares Number"])
        #print(hashmap["Book Per Share Value"])

        hashmap["Tangible Book Per Share Value"] = self.getRatio(hashmap["Tangible Book Value"], hashmap["Ordinary Shares Number"])
        #print(hashmap["Tangible Book Per Share Value"])

        hashmap["Total Debt Per Share Value"] = self.getRatio(hashmap["Total Debt"], hashmap["Ordinary Shares Number"])
        #print(hashmap["Total Debt Per Share Value"])

        return hashmap
    
    def createDataIS(self, symbol, hashmap):

        df = pd.read_csv( YahooProcessor.OUTPUTDIR + symbol + "_IS.csv")
        for index, row in df.iterrows():

            values = []
            for index in range (1, len(row)):
                values.append(row[index])

            hashmap[row[0]] = values

        hashmap["Dates"] = df.columns[1:].tolist()
        #print(hashmap["Dates"])

        hashmap["Revenue Per Share Value"] = self.getRatio(hashmap["Total Revenue"], hashmap["Diluted Average Shares"])
        #print(hashmap["Revenue Per Share Value"])

        hashmap["Net Margin"] = self.getRatio(hashmap["Net Income From Continuing Operation Net Minority Interest"], hashmap["Total Revenue"])
        #print(hashmap["Net Margin"])

        return hashmap
    
if __name__ == "__main__":

    yp = YahooProcessor()
    yp.createData("AAPL")

