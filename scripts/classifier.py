from transformers import BertTokenizer, BertForSequenceClassification, pipeline

# set labels


# 加载预训练的BERT模型和tokenizer
model_name = 'bert-base-uncased'
model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

# 定义分类任务的pipeline
classifier = pipeline('text-classification', model=model, tokenizer=tokenizer)

# 准备新的文本数据
new_text = "Your new text here"

# 使用BERT模型进行分类预测
result = classifier(new_text)

print(result)