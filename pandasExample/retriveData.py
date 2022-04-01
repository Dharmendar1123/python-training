import pandas as pd

workOut = pd.read_csv('resources/workoutData.csv')

sizeWorkOut = workOut.shape  # get number of rows and column
# print(sizeWorkOut)

indexWorkOut = workOut.index  # get index details
# print(indexWorkOut)

columnWorkOut = workOut.columns  # get the names of the column
# print(columnWorkOut)

# infoWorkOut = workOut.info()  # gets the information the file like no. column, non-null vales, type etc
# print(infoWorkOut)

NullWorkOut = workOut.count()  # gets the no. of non-null values
print(NullWorkOut)
