import os
import requests
from dotenv import load_dotenv
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")
with open("long_doc.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
def cut_words(text):
    return list(jieba.cut(text))
print("正在计算文档向量（极速完成）...")
vectorizer = TfidfVectorizer(tokenizer=cut_words)
tfidf_matrix = vectorizer.fit_transform(lines)
question = input("\n请输入关于文档的问题: ")
question_vec = vectorizer.transform([question])
scores = cosine_similarity(question_vec, tfidf_matrix).flatten()
top_indices = scores.argsort()[-2:][::-1] 
relevant_docs = []
for idx in top_indices:
    if scores[idx] > 0:
        relevant_docs.append(lines[idx])
if relevant_docs:
    context = "\n".join(relevant_docs)
    print(f"\n 找到 {len(relevant_docs)} 个相关段落：")
    print(f"【{relevant_docs[0][:30]}...】(只显示前30字)")
else:
    context = "没找到相关内容。"
    print("\n没有找到相关段落。")
if relevant_docs:
    prompt = f"""你是一个严谨的助手。请严格根据以下背景信息回答问题，如果找不到，就说不知道。
【背景信息】：{context}
【问题】：{question}"""
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]} 
    print("正在请求大模型...")
    response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=data)
    if response.status_code == 200:
        print("\nAI 回答：", response.json()["choices"][0]["message"]["content"])
    else:
        print("状态码：",response.status_code)