def df_clean(df):
    # Change Date from string to DateTime64
    train['Date'] = pd.to_datetime(train['Date'])
    # Drop NaNs
    train_nona = train.dropna()
    # Remove days when stores were closed
    df = df[df['Open'] == 1]
    # Remove zero sale days
    df = df[~(df[['Sales']] == 0).any(axis=1)]
    # Reset index after
    df = df.reset_index(drop=True)
    return df
