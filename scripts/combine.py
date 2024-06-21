import csv
import os

csv_file_path = "../xiangsheng_theme.csv"
file_directory = "../xiangsheng/"
xiangsheng_type= ["传统节目", "新编节目", "当代节目"]
# Open the CSV file
with open(csv_file_path, "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Get the filename from the first column
        if len(row) < 1 or row[0].strip == "标题":
            continue
        filename = row[0].strip()
        # print(filename)
        prefix = filename[0:3]

        # Read the file from the xiangsheng directory
        file_path = file_directory + filename
        finished = False
        if not os.path.exists(file_path):
            # print(f"File not found: {file_path}")
            find_same_prefix = False
            for file_name in os.listdir(file_directory):
                if file_name.startswith(prefix):
                    filename = file_name
                    find_same_prefix = True
                    break
            file_path = file_directory + filename
            if not find_same_prefix:
                continue
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if finished:
                    break
                for t in xiangsheng_type:
                    if t in line:
                        print(filename + "," + t + "," + row[1].strip())    
                        finished = True
                        break

        # with open(file_path, "r", encoding="utf-8") as file:
        #     for line in file:
        #         if finished:
        #             break
        #         for t in xiangsheng_type:
        #             if t in line:
        #                 print(t)
        #                 finished = True
        #                 break

            # Process the file contents here
            # ...