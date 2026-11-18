import os
import chromadb
import requests
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")
with open("long_doc.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
client = chromadb.PersistentClient(path="./my_vector_db")
model_name ='BAAI/bge-small-zh-v1.5'
chroma_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
collection = client.get_or_create_collection(name="my_knowledge",embedding_function=chroma_ef)
print("正在把文档存入数据库（自动转换为向量）...")
collection.add(documents=lines,ids=[str(i) for i in range(len(lines))] )
print("入库完成！")
question = input("请输入关于文档的问题: ")
results = collection.query(query_texts=[question],n_results=2)
retrieved_docs = results['documents'][0]
context = "\n".join(retrieved_docs)
print(f"\n 找到的相关段落：\n{context}\n")
prompt = f"""你是一个严谨的问答助手。请严格根据以下背景信息回答问题，如果找不到，就说不知道。
【背景信息】：{context}【问题】：{question}"""
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
data = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}
response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=data)
if response.status_code == 200:
    print("AI 回答：", response.json()["choices"][0]["message"]["content"])
else:
    print("响应码：",response.status_code)