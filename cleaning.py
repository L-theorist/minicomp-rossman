import pandas as pd
def df_clean(df):
    # Change Date from string to DateTime64
    df['Date'] = pd.to_datetime(df['Date'])
    # Drop NaNs
    df = df.dropna()
    # Remove days when stores were closed
    df = df[df['Open'] == 1]
    # Remove zero sale days
    df = df[~(df[['Sales']] == 0).any(axis=1)]
    # Reset index after
    df = df.reset_index(drop=True)
    return df

def store_wash(df):
    store_interest = df[['Store', 'StoreType', 'Assortment', 'CompetitionDistance']]
    store_interest['CompetitionDistance'] = df.fillna(df['CompetitionDistance'].mean())
    return df

def clean_dishes(df1, df2):
    df_clean(df1)
    store_wash(df2)
    total_data = pd.concat([df1, df2], axis=1, sort=False)
    #getting 2 columns with same name, deleting extra store column 
    old = list(total_data.columns)

    old[9] = 'bad-store'

    total_data.columns = old

    total_data = total_data.drop('bad-store', axis=1)
    
    return total_data