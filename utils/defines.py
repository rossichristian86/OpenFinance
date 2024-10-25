from enum import Enum

class Info(Enum):
    EnterpriseValue = 'enterpriseValue'
    MarketCap = 'marketCap'
    SharesOutstanding = 'sharesOutstanding'


class Financials(Enum):
    RevenuePerShare = 'Revenue Per Share'
    DilutedRevenuePerShare = 'Diluted Revenue Per Share'
    RevenueGrowth1Y = 'Revenue Growth 1Y'
    RevenuePerShareGrowth1Y = 'Revenue Per Share Growth 1Y'
    DilutedRevenuePerShareGrowth1Y = 'Diluted Revenue Per Share Growth 1Y'
    NetMargin = "Net Margin"
    OperatingMargin = "Operating Margin"

    #Basics
    BasicAverageShares = 'Basic Average Shares'
    DilutedAverageShares = 'Diluted Average Shares'
    Revenues = 'Total Revenue'
    GrossProfit = 'Gross Profit'
    OperatingIncome = 'Operating Income'
    NetIncome = 'Net Income'
    DiluitedEPS = 'Diluted EPS'
    EPS = 'Basic EPS'
    OperatingRevenue = 'Operating Revenue'
    CostOfRevenue = 'Cost Of Revenue'



    ''' TODO da aggiungere se serve ai financials

       'Tax Effect Of Unusual Items', 'Tax Rate For Calcs',
       'Normalized EBITDA',
       'Net Income From Continuing Operation Net Minority Interest',
       'Reconciled Depreciation', 'Reconciled Cost Of Revenue', 'EBITDA',
       'EBIT', 'Net Interest Income', 'Interest Expense', 'Interest Income',
       'Normalized Income',
       'Net Income From Continuing And Discontinued Operation',
       'Total Expenses', 'Total Operating Income As Reported', 'Diluted NI Availto Com Stockholders',
       'Net Income Common Stockholders',
       'Net Income Including Noncontrolling Interests',
       'Net Income Continuous Operations', 'Tax Provision', 'Pretax Income',
       'Other Income Expense', 'Other Non Operating Income Expenses',
       'Net Non Operating Interest Income Expense',
       'Interest Expense Non Operating', 'Interest Income Non Operating',
       'Operating Expense', 'Research And Development',
       'Selling General And Administration',

    '''