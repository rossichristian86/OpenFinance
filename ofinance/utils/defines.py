from enum import Enum


class Info(Enum):

    #Basic
    EnterpriseValue = 'enterpriseValue'
    MarketCap = 'marketCap'
    SharesOutstanding = 'sharesOutstanding'
    TrailingEps = 'trailingEps'
    ForwardEps = 'forwardEps'
    TotalRevenue = 'totalRevenue'
    TotalDebt = 'totalDebt'
    OperatingMargins = 'operatingMargins'

    #Custom
    #####


class Quarterlyfinancials(Enum):
    TotalRevenue = 'Total Revenue'


class Financials(Enum):

    #Basic
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

    #Custom
    RevenuePerShare = 'Revenue Per Share'
    DilutedRevenuePerShare = 'Diluted Revenue Per Share'
    RevenueGrowth1Y = 'Revenue Growth 1Y'
    RevenuePerShareGrowth1Y = 'Revenue Per Share Growth 1Y'
    DilutedRevenuePerShareGrowth1Y = 'Diluted Revenue Per Share Growth 1Y'
    NetMargin = "Net Margin"    # net_income/total_revenues
    OperatingMargin = "Operating Margin"    # operating_income/total_revenues


    '''TODO da aggiungere se serve a info
        'address1', 'city', 'state', 'zip', 'country', 'phone', 'website', 'industry', 'industryKey', 'industryDisp', 'sector', 
        'sectorKey', 'sectorDisp', 'longBusinessSummary', 'fullTimeEmployees', 'companyOfficers', 'auditRisk', 'boardRisk',
        'compensationRisk', 'shareHolderRightsRisk', 'overallRisk', 'governanceEpochDate', 'compensationAsOfEpochDate', 
        'maxAge', 'priceHint', 'previousClose', 'open', 'dayLow', 'dayHigh', 'regularMarketPreviousClose', 'regularMarketOpen', 
        'regularMarketDayLow', 'regularMarketDayHigh', 'dividendRate', 'dividendYield', 'exDividendDate', 'payoutRatio', 'beta', 
        'trailingPE', 'forwardPE', 'volume', 'regularMarketVolume', 'averageVolume', 'averageVolume10days', 'averageDailyVolume10Day',
        'fiftyTwoWeekLow', 'fiftyTwoWeekHigh', 'priceToSalesTrailing12Months', 'fiftyDayAverage', 'twoHundredDayAverage',
        'trailingAnnualDividendRate', 'trailingAnnualDividendYield', 'currency', 'enterpriseValue', 'profitMargins', 'floatShares',
        'sharesOutstanding', 'sharesShort', 'sharesShortPriorMonth', 'sharesShortPreviousMonthDate', 'dateShortInterest',
        'sharesPercentSharesOut', 'heldPercentInsiders', 'heldPercentInstitutions', 'shortRatio', 'shortPercentOfFloat',
        'impliedSharesOutstanding', 'bookValue', 'priceToBook', 'lastFiscalYearEnd', 'nextFiscalYearEnd', 'mostRecentQuarter', 
        'earningsQuarterlyGrowth', 'netIncomeToCommon',  'pegRatio', 'lastSplitFactor', 'lastSplitDate',
        'enterpriseToRevenue', 'enterpriseToEbitda', '52WeekChange', 'SandP52WeekChange', 'lastDividendValue', 'lastDividendDate', 
        'exchange', 'quoteType', 'symbol', 'underlyingSymbol', 'shortName', 'longName', 'firstTradeDateEpochUtc', 'timeZoneFullName', 
        'timeZoneShortName', 'uuid', 'messageBoardId', 'gmtOffSetMilliseconds', 'currentPrice', 'targetHighPrice', 'targetLowPrice', 
        'targetMeanPrice', 'targetMedianPrice', 'recommendationMean', 'recommendationKey', 'numberOfAnalystOpinions', 
        'totalCash', 'totalCashPerShare', 'ebitda',  'quickRatio', 'currentRatio',  'debtToEquity',
        'revenuePerShare', 'returnOnAssets', 'returnOnEquity', 'earningsGrowth', 'revenueGrowth', 
        'grossMargins', 'ebitdaMargins',  'financialCurrency', 'trailingPegRatio'
    '''


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