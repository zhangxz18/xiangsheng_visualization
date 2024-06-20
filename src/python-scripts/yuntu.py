import os
import re
import json
import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import uuid
import sys
import json
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#字符清洗函数
def clean_content(content):
    # 去除所有特殊字符
    content = re.sub(r'\s+', '', content)
    content = re.sub(r'[^\w]', '', content)
    content = re.sub(r'\d+', '', content)
    # 移除指定字符
    remove_chars = '一甲乙这儿是么们篇个辑有吗不版说回知出什过时起主少样因地'
    content = re.sub(f"[{remove_chars}]", '', content)
    content = content.split('来源信息')[1]
    return content
#本地查询文件
def find_text(input):
        filepath = json.loads(input)
        

        text_list = []
        for file in filepath:
            file_path = file['path']
            try:
                file_path = os.path.normpath(file_path)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                processed_text = clean_content(content)
                text_list.append(processed_text)
            except Exception as e:
                print(f"Failed to process {file_path}: {e}")
        result_string = ''.join(text_list)
        return result_string

#分词函数
def jieba_cut(text):
    precise_words = jieba.lcut(text, cut_all=False)
    filtered_words = [word for word in precise_words if len(word) > 1]
    precise_counter = Counter(filtered_words)
    sorted_counter = dict(precise_counter.most_common())
    return sorted_counter
#云图函数
def generate_wordcloud(counter, title, output_path):
    if not counter:
        raise ValueError("Empty counter object. Cannot generate word cloud.")
    font_path = 'simhei.ttf'
    
    wordcloud = WordCloud(font_path=font_path, max_words=100, width=1000, height=1000,).generate_from_frequencies(counter)
    plt.figure(figsize=(20, 10))
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title)
    plt.axis('off')
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()
def generate_bar_chart(counter, title, output_path):
    if not counter:
        raise ValueError("Empty counter object. Cannot generate bar chart.")

    # 取出前20个词频最高的词
    top_20 = dict(Counter(counter).most_common(20))

    # 绘制直方图
    plt.figure(figsize=(20, 10))
    plt.bar(top_20.keys(), top_20.values(), color='skyblue')

    # 处理中文显示问题
    plt.xticks(rotation=45, fontsize=12, family='SimHei')
    plt.yticks(fontsize=12)
    plt.xlabel('词语', fontsize=14, family='SimHei')
    plt.ylabel('频率', fontsize=14, family='SimHei')
    plt.title(title, fontsize=18, family='SimHei')

    # 保存图像为jpg格式
    plt.savefig(output_path, format='jpg', bbox_inches='tight')
    plt.close()


def main():
    # 从标准输入读取数据

    input_data = sys.stdin.buffer.read().decode('utf-8')
    result_s=find_text(input_data)
    c=jieba_cut(result_s)



    #base_path = r'D:\jupyter_notebook_exam\xiangsheng_visualization-master\public'#需要自行修改，这里存放你的项目下面public文件夹绝对路径，不要有中文路径
    base_path = os.path.join(os.path.dirname(__file__), '../../public')
    
    uu=uuid.uuid4()
    wordcloud_image_path = os.path.join(base_path,f"{uu}.png")
    d=generate_wordcloud(counter=c,title="",output_path= wordcloud_image_path)
    wordbar_image_path = os.path.join(base_path,f"{uu}.jpg")
    e=generate_bar_chart(counter=c,title="", output_path=wordbar_image_path)
    word_freq_path = os.path.join(base_path, f"{uu}.json")
    with open(word_freq_path, 'w', encoding='utf-8') as json_file:
        json.dump(c, json_file, ensure_ascii=False, indent=2)

    result = {
            'uuid': os.path.basename(wordcloud_image_path).split('.')[0],
            'wordcloud_image': wordcloud_image_path,
            'wordbar_image_path':wordbar_image_path,
            'word_freq_path': word_freq_path
        }
    print(json.dumps(result))


if __name__ == '__main__':
    main()