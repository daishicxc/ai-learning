import os
import gradio as gr
import chromadb
import requests
from dotenv import load_dotenv
from chromadb.utils import embedding_functions

load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")
print("正在启动系统并加载知识库...")
doc_folder = "my_docs"
all_chunks = []
def split_text(text, chunk_size=200, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += (chunk_size - overlap)
    return chunks
for filename in os.listdir(doc_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(doc_folder, filename), "r", encoding="utf-8") as f:
            all_chunks.extend(split_text(f.read()))
client = chromadb.PersistentClient(path="./my_vector_db_pro")
chroma_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name='BAAI/bge-small-zh-v1.5')
client.delete_collection("my_knowledge_pro") # 权宜之计：每次启动重建
collection = client.get_or_create_collection(name="my_knowledge_pro", embedding_function=chroma_ef)
collection.add(documents=all_chunks, ids=[str(i) for i in range(len(all_chunks))])
print("知识库准备就绪！")
def chat_with_docs(message, history):
    """这个函数接收用户的输入，返回 AI 的回答"""
    results = collection.query(query_texts=[message], n_results=2)
    docs=results['documents'][0]
    if docs:
        context = "\n---\n".join(docs)
    else:
        return "本次文档中没有找到相关信息。"
    system_prompt = f"你是一个严谨的问答助手。请严格根据以下背景信息回答问题，如果找不到，就说不知道。\n【背景信息】：\n{context}"
    messages = [{"role": "system", "content": system_prompt}]
    for chat in history:
      if isinstance(chat, dict):  # 新版 Gradio
         messages.append({"role": chat["role"], "content": chat["content"]})
      elif isinstance(chat, list) or isinstance(chat, tuple): # 旧版 Gradio
        messages.append({"role": "user", "content": chat[0]})
        messages.append({"role": "assistant", "content": chat[1]})
    messages.append({"role": "user", "content": message})
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {"model": "deepseek-chat", "messages": [{"role": "user", "content":messages}]}
    
    try:
        response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"请求失败，状态码：{response.status_code}"
    except Exception as e:
        return f"发生错误：{str(e)}"
demo = gr.ChatInterface(
    fn=chat_with_docs,
    title="📚 我的专属 AI 知识库",
    description="基于本地文档的智能问答系统，问我关于文档里的任何问题！",
)
if __name__ == "__main__":
    demo.launch()