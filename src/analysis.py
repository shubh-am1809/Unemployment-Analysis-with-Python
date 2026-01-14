def covid_period_data(df):
    return df[
        (df['Date'] >= '2020-03-01') &
        (df['Date'] <= '2020-11-30')
    ]
