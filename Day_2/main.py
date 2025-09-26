import os
import csv
import datetime

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR,"Students_Data.csv")

s_list = []
with open(file_path, newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        s_list.append(row)

# print(s_list)

now = datetime.date.today()

year = now.year;
print(year)

above_18 = [(i[0],year-int(i[1])) for i in s_list if (year-int(i[1]))>=18]
print(above_18)