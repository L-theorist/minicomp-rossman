import pandas as pd
#import datetime dt

features = ['DayOfWeek', 'WeekNumber', 'Month', 'DayOfYear', 'SalesPerCustomer', 'Customers']

def df_add_features(df):
    df['WeekNumber'] = df['Date'].dt.week
    df['Month'] = df['Date'].dt.month
    df['DayOfYear'] = df['Date'].dt.dayofyear
    df['SalesPerCustomer'] = df['Sales'] /  df['Customers']
    return df
    