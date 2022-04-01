import pandas as pd
import requests as rs
import json
from pathlib import Path


def gettingData():
    response = rs.get("http://api.open-notify.org/astros.json")
    df_json = pd.DataFrame(response.json())
    df = pd.DataFrame()
    # data = response.json()
    for col in df_json.columns:
        if col == 'people':
            dt = csvConversion(df_json['people'])
            # print(dt)
            df = pd.concat([df, dt])
        else:
            df = pd.concat([df, df_json])
    writeToCsv(df)
    # data = response.json()
    # csvConversion(data)
    # writeToCsv(df)
    # print(df)


def csvConversion(data):
    df = pd.DataFrame()
    for d in data:
        result = pd.json_normalize(d)
        df = pd.concat([df, result])
    # writeToCsv(df)
    # print(df)
    return df

def writeToCsv(data):
    filePath = Path("csvFiles/astro.csv")
    data.to_csv(filePath, index=False)


if __name__ == "__main__":
    gettingData()
