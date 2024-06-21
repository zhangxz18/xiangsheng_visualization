import csv
import os

csv_file_path = "../theme_and_time.csv"
KEYS = [
    "经济", "教育", "科学", "社会", "政治", "体育", "娱乐", "历史"
]

with open(csv_file_path, "r", encoding="utf-16") as csv_file:
    csv_reader = csv.reader(csv_file)
    data = []
    xiangsheng_type= ["传统节目", "新编节目", "当代节目"]
    for type in xiangsheng_type:
        data.append({"time": type})

    # Iterate over each row in the CSV file
    for row in csv_reader:
        if row[0] == "标题":
            continue
        time = row[1].strip()
        theme = row[2].strip()
        if time == "传统节目":
            if theme in data[0]:
                data[0][theme] += 1
            else:
                data[0][theme] = 1
        elif time == "新编节目":
            if theme in data[1]:
                data[1][theme] += 1
            else:
                data[1][theme] = 1
        elif time == "当代节目":
            if theme in data[2]:
                data[2][theme] += 1
            else:
                data[2][theme] = 1
    for d in data:
        for key in KEYS:
            if key not in d:
                d[key] = 0
    print(data)
