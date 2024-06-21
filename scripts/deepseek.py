import requests
import json
import os

# Define the source and destination directories
source_dir = "../xiangsheng"
destination_dir = "../xiangsheng_copy"

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

destination_file = "../xiangsheng_theme.txt"
json_data = []
start_processing = False

# Iterate over the files in the source directory
with open(destination_file, "a", encoding="utf-8") as fout:
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        # destination_file = os.path.join(destination_dir, filename)

        if not start_processing:
            if filename == "打砂锅 - 彭国良.txt":
                start_processing = True
            continue

        # Open the source file for reading
        with open(source_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Extract lines 30 to 200 and remove empty lines
        extracted_lines = [line for line in lines[29:79] if line.strip()]

        content = "".join(extracted_lines)
        line_data = {'title': filename, 'content': content}
        json_data.append(line_data)
        url = "https://api.deepseek.com/chat/completions"
        json_to_string = json.dumps(line_data)

        payload = json.dumps({
        "messages": [
            {
            "content": "我下面将会发送一个json给你，包含一篇相声的标题和内容，格式为(title: xxx.txt, content: content)。请你对其内容进行主题分类，可选的主题包括【经济, 教育，科学，社会，政治，体育，娱乐，历史】，如果涉及到经济相关问题请选为经济主题，时政问题请选为政治主题，如果是历史上发生的事选为历史主题。返回的结果格式为“标题, 分类”，不需要返回其他内容。",
            "role": "system"
            },
            {
            "content": json_to_string,
            "role": "user"
            }
        ],
        "model": "deepseek-coder",
        "frequency_penalty": 0,
        "max_tokens": 2048,
        "presence_penalty": 0,
        "stop": None,
        "stream": False,
        "temperature": 1,
        "top_p": 1,
        "logprobs": False,
        "top_logprobs": None
        })
        headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer sk-f8a39c30aab1410f9b29900e141aa8fc'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        # append the result to xiangsheng_theme.txt
        response = response.json()
        if "choices" in response and response["choices"]:
            if "message" in response["choices"][0] and "content" in response["choices"][0]["message"]:
                print(response["choices"][0]["message"]["content"])
                fout.write(response["choices"][0]["message"]["content"]+"\n")
        else:
            print("No valid response received.")
        import time
        
        time.sleep(0.3)
        