import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")
with open("long_doc.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
question = input("请输入关于文档的问题: ")
keyword = question[:2] 
relevant_chunks = []
for line in lines:
    if keyword in line:
        relevant_chunks.append(line)
if relevant_chunks:
    context = "\n".join(relevant_chunks[:3])
    print(f"检索到 {len(relevant_chunks)} 个相关段落，正在发送")
else:
    context = "没有找到相关信息。"
    print("没找到相关段落。")
prompt = f"""
你是一个严谨的问答助手。请严格根据以下背景信息回答问题，如果找不到，就说不知道。
【背景信息】：{context}
【问题】：{question}"""
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
data = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}
response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=data)
if response.status_code == 200:
    print("\nAI 回答：", response.json()["choices"][0]["message"]["content"])