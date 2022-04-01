import pandas as pd
from pathlib import Path


def writeToCSV(sortedData):
    location = Path('csvFiles/sortedFile.csv')
    df = pd.DataFrame(sortedData)
    df.to_csv(location, index=False)


def insertionSorting(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > key:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            j = j - 1


def readCSV():
    sortingData = pd.read_csv("csvFiles/data.csv")
    df = pd.DataFrame(sortingData)
    values = df.squeeze().array
    insertionSorting(values)
    writeToCSV(values)


if __name__ == "__main__":
    readCSV()
