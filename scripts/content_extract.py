import os

# Define the source and destination directories
source_dir = "../xiangsheng"
destination_dir = "../xiangsheng_copy"

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

destination_file = "../xiangsheng.json"
json_data = []

# Iterate over the files in the source directory
for filename in os.listdir(source_dir):
    source_file = os.path.join(source_dir, filename)
    # destination_file = os.path.join(destination_dir, filename)

    # Open the source file for reading
    with open(source_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Extract lines 30 to 200 and remove empty lines
    extracted_lines = [line for line in lines[29:199] if line.strip()]

    content = "".join(extracted_lines)
    line_data = {'title': filename, 'content': content}
    json_data.append(line_data)

# write json data to /xiangsheng.json
import json
with open(destination_file, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

