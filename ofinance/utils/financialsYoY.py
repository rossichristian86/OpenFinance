import yfinance as yf
import pandas as pd

## Tutti questi metodi prendono obj_financials e ci aggiungono label

# Calcola il Revenue Per Share Growth 1Y per ogni anno (eccetto il primo) e aggiungilo al DataFrame
def add_revenue_grow_1y(obj_financials, label):
    
    obj_financials[label] = None  # Inizializza la colonna
    for i in range(len(obj_financials) - 1):
        # Calcola la crescita di Revenue Per Share rispetto all'anno successivo
        if pd.notna(obj_financials.iloc[i]["Total Revenue"]) and pd.notna(obj_financials.iloc[i + 1]["Total Revenue"]):
            current_revenue = obj_financials.iloc[i]["Total Revenue"]
            previous_revenue = obj_financials.iloc[i + 1]["Total Revenue"]
            
            if previous_revenue != 0:
                revenue_per_share_grow_1y = (current_revenue / previous_revenue) - 1
                obj_financials.at[obj_financials.index[i], label] = revenue_per_share_grow_1y


# Calcola il Revenue Per Share Growth 1Y per ogni anno (eccetto il primo) e aggiungilo al DataFrame
def add_revenue_per_share_grow_1y(obj_financials, label):
    
    obj_financials[label] = None  # Inizializza la colonna
    for i in range(len(obj_financials) - 1):
        # Calcola la crescita di Revenue Per Share rispetto all'anno successivo
        if pd.notna(obj_financials.iloc[i]["Revenue Per Share"]) and pd.notna(obj_financials.iloc[i + 1]["Revenue Per Share"]):
            current_revenue = obj_financials.iloc[i]["Revenue Per Share"]
            previous_revenue = obj_financials.iloc[i + 1]["Revenue Per Share"]
            
            if previous_revenue != 0:
                revenue_per_share_grow_1y = (current_revenue / previous_revenue) - 1
                obj_financials.at[obj_financials.index[i], label] = revenue_per_share_grow_1y


# Calcola il Revenue Per Share Growth 1Y per ogni anno (eccetto il primo) e aggiungilo al DataFrame
def add_diluted_revenue_per_share_grow_1y(obj_financials, label):

    obj_financials[label] = None  # Inizializza la colonna
    for i in range(len(obj_financials) - 1):
        # Calcola la crescita di Revenue Per Share rispetto all'anno successivo
        if pd.notna(obj_financials.iloc[i]["Diluted Revenue Per Share"]) and pd.notna(obj_financials.iloc[i + 1]["Diluted Revenue Per Share"]):
            current_revenue = obj_financials.iloc[i]["Diluted Revenue Per Share"]
            previous_revenue = obj_financials.iloc[i + 1]["Diluted Revenue Per Share"]
            
            if previous_revenue != 0:
                revenue_per_share_grow_1y = (current_revenue / previous_revenue) - 1
                obj_financials.at[obj_financials.index[i], label] = revenue_per_share_grow_1y

