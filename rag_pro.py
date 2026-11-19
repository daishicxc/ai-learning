import os
import chromadb
import requests
from dotenv import load_dotenv
from chromadb.utils import embedding_functions
load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")
def split_text(text, chunk_size=200, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += (chunk_size - overlap)
    return chunks
all_chunks = []
doc_folder = "my_docs"
print("正在处理文件...")
for filename in os.listdir(doc_folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(doc_folder, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            file_chunks = split_text(content)
            all_chunks.extend(file_chunks) 
print("\n正在存入数据库（如果模型已下载会很快）...")
client = chromadb.PersistentClient(path="./my_vector_db_pro")
chroma_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name='BAAI/bge-small-zh-v1.5')
collection = client.get_or_create_collection(name="my_knowledge_pro", embedding_function=chroma_ef)
client.delete_collection("my_knowledge_pro")
collection = client.get_or_create_collection(name="my_knowledge_pro", embedding_function=chroma_ef)
collection.add(documents=all_chunks,ids=[str(i) for i in range(len(all_chunks))])
question = input("\n请输入关于这些文档的问题: ")
results = collection.query(query_texts=[question],n_results=2) # 找最像的2块
if results['documents'] and len(results['documents'][0]) > 0:
    context = "\n---\n".join(results['documents'][0])
    print(f"\n检索到的知识：\n{context}\n")
else:
    print("未检索到相关背景信息")
prompt = f"""你是一个严谨的问答助手。请严格根据以下背景信息回答问题，如果找不到，就说不知道。
【背景信息】：
{context}
【问题】：
{question}"""
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
data = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}
response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=data)
if response.status_code == 200:
    print("AI 回答：", response.json()["choices"][0]["message"]["content"]) 
else:
    print("状态码：",response.status_code)