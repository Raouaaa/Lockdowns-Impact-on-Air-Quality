import pandas as pd
import datetime as dt

def load_data(period):
    """
    Input
    period - Quarter
    :returns
    returns data frame for the selected period with correct date type
    """
    data = pd.read_csv(f"../data/raw/waqi-covid19-airqualitydata-{period}.csv",skiprows=4, encoding='ISO-8859-1')
    data['Date'] = pd.to_datetime(data['Date']) 
    return data