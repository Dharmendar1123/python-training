import pandas as pd

workOut = pd.read_csv('resources/workoutData.csv')
df = pd.DataFrame(workOut)

noNull = df.fillna(0)
# print(noNull)

removeIndex = df.set_index('Duration')
print(removeIndex)