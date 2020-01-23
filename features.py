def df_add_features(df):
    df['WeekNumber'] = df['DateTime'].dt.week
    df['Month'] = df['DateTime'].dt.month
    df['DayOfYear'] = df['DateTime'].dt.dayofyear
    df['SalesPerCustomer'] = df['Sales'] /  df['Customers']
    return df
    