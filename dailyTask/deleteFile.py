import os
from datetime import datetime

time_period = int(input("Enter days: "))
required_path = r"C:\Users\Dharmendar.Parmar\Desktop\deleteFile\crud-operation\crud-operation"

today = datetime.now()
for each_file in os.listdir(required_path):
    each_file_path = os.path.join(required_path, each_file)
    if os.path.isfile(each_file_path):
        file_creation_date = datetime.fromtimestamp(os.path.getctime(each_file_path))
        diff_days = (today-file_creation_date).days
        if diff_days >= time_period:
            os.remove(each_file_path)
            print(each_file_path, diff_days)