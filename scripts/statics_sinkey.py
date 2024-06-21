import csv
import os
import numpy as np

csv_file_path = "../theme_and_time.csv"
xiangsheng_type= ["传统节目", "新编节目", "当代节目"]
keys = [
    "经济", "教育", "科学", "社会", "政治", "体育", "娱乐", "历史"
]

nodes = []
links = []
index = 0
name2index = {}
for type in xiangsheng_type:
    nodes.append({"name": type})
    name2index[type] = index
    index += 1
for key in keys:
    nodes.append({"name": key})
    name2index[key] = index
    index += 1

with open(csv_file_path, "r", encoding="utf-16") as csv_file:
    csv_reader = csv.reader(csv_file)
    data = []
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
        for key in keys:
            if key in d:
                result = np.log(d[key])
                if result <= 0.0001:
                    result = 0.01
                links.append({
                    "source": name2index[d["time"]],
                    "target": name2index[key],
                    "value": result
                })
    json_data = {
        "nodes": nodes,
        "links": links
    }
    print(json_data)