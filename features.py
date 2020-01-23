def df_add_features(df):
    
    df['Sales/Cust'] = df['Sales'] /  df['Customers']
    return data
    