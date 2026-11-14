import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")
with open("my_doc.txt", "r", encoding="utf-8") as f:
    doc_content = f.read()
question = input("针对这份文档，你想问什么？: ")
prompt = f"""你是一个智能问答助手。请**严格根据**下面提供的背景信息来回答问题。如果背景信息中没有提及相关内容，请直接回答“根据提供的资料，我找不到答案”，绝对不要自己编造。
【背景信息】：
{doc_content}
【用户问题】：
{question}"""
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
data = {"model": "deepseek-chat","messages": [{"role": "user", "content": prompt}]}
response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=data)
if response.status_code == 200:
    reply = response.json()["choices"][0]["message"]["content"]
    print("\nAI 回答：", reply)
else:
    print("请求失败：", response.status_code)