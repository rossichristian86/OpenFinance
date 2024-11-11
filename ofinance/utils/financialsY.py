import yfinance as yf
import pandas as pd

## Tutti questi metodi prendono obj_financials e ci aggiungono label

# Calcola il Revenue Per Share per ogni anno e lo aggiungi al DataFrame principale
def add_revenue_per_share(obj_financials, label):
   
    obj_financials[label] = None  # Inizializza la colonna
    for i in range(len(obj_financials)):
        # Calcola Revenue Per Share se i dati necessari sono disponibili
        if "Total Revenue" in obj_financials.columns and "Basic Average Shares" in obj_financials.columns:
            total_revenue = obj_financials.iloc[i]["Total Revenue"]
            basic_average_shares = obj_financials.iloc[i]["Basic Average Shares"]
            if pd.notna(total_revenue) and pd.notna(basic_average_shares) and basic_average_shares != 0:
                revenue_per_share = total_revenue / basic_average_shares
                obj_financials.at[obj_financials.index[i], label] = revenue_per_share

def add_net_margin(obj_financials, label):
   
    obj_financials[label] = None  # Inizializza la colonna
    for i in range(len(obj_financials)):
        # Calcola Revenue Per Share se i dati necessari sono disponibili
        if "Total Revenue" in obj_financials.columns and "Net Income" in obj_financials.columns:
            total_revenue = obj_financials.iloc[i]["Total Revenue"]
            net_income = obj_financials.iloc[i]["Net Income"]
            if pd.notna(total_revenue) and pd.notna(net_income) and net_income != 0:
                revenue_per_share = net_income / total_revenue
                obj_financials.at[obj_financials.index[i], label] = revenue_per_share

def add_operating_margin(obj_financials, label):
   
    obj_financials[label] = None  # Inizializza la colonna
    for i in range(len(obj_financials)):
        # Calcola Revenue Per Share se i dati necessari sono disponibili
        if "Total Revenue" in obj_financials.columns and "Operating Income" in obj_financials.columns:
            total_revenue = obj_financials.iloc[i]["Total Revenue"]
            operating_income = obj_financials.iloc[i]["Operating Income"]
            if pd.notna(total_revenue) and pd.notna(operating_income) and operating_income != 0:
                revenue_per_share = operating_income / total_revenue
                obj_financials.at[obj_financials.index[i], label] = revenue_per_share

# Calcola il Revenue Per Share per ogni anno e lo aggiungi al DataFrame principale
def add_diluted_revenue_per_share(obj_financials, label):
    
    obj_financials[label] = None  # Inizializza la colonna
    for i in range(len(obj_financials)):
        # Calcola Revenue Per Share se i dati necessari sono disponibili
        if "Total Revenue" in obj_financials.columns and "Diluted Average Shares" in obj_financials.columns:
            total_revenue = obj_financials.iloc[i]["Total Revenue"]
            basic_average_shares = obj_financials.iloc[i]["Diluted Average Shares"]
            if pd.notna(total_revenue) and pd.notna(basic_average_shares) and basic_average_shares != 0:
                revenue_per_share = total_revenue / basic_average_shares
                obj_financials.at[obj_financials.index[i], label] = revenue_per_share

