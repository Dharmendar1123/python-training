import objectpath
import pandas as pd
import requests as rs
import json
from pathlib import Path


def gettingData():
    response = rs.get("http://api.open-notify.org/astros.json")
    df_json = pd.DataFrame(response.json())
    df = pd.DataFrame()
    data = response.json()
    jsonnn_tree = objectpath.Tree(data)
    for col in df_json.columns:
        if col == 'people':
            name_list = list(jsonnn_tree.execute('$..name'))
            craft_list = list(jsonnn_tree.execute('$..craft'))
            message_list = list(jsonnn_tree.execute('$..message'))
            number_list = list(jsonnn_tree.execute('$..number'))
            name_series = pd.Series(name_list)
            craft_series = pd.Series(craft_list)
            message_series = pd.Series(message_list)
            number_series = pd.Series(number_list)
            df.insert(loc=0, column='message', value=message_series)
            df.insert(loc=1, column='name', value=name_series)
            df.insert(loc=2, column='craft', value=craft_series)
            df.insert(loc=3, column='number', value=number_series)
    writeToCsv(df)


# def csvConversion(data):
#     df = pd.DataFrame()
#     for d in data:
#         result = pd.json_normalize(d)
#         df = pd.concat([df, result])
#     # writeToCsv(df)
#     # print(df)
#     return df

def writeToCsv(data):
    file_path = Path("csvFiles/astro.csv")
    data.to_csv(file_path, index=False)


if __name__ == "__main__":
    gettingData()
