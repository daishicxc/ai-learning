import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("DEEPSEEK_API_KEY")
headers={"Authorization":f"Bearer {API_KEY}","Content_Type":"application/json"}
data={"model":"deepseek-chat","messages":[{"role":"user","content":"你好呀，用一句话介绍一下自己吧"}]}
url="https://api.deepseek.com/chat/completions"
r=requests.post(url,headers=headers,json=data)
if r.status_code==200:
    print("响应状态码：",r.status_code)
    result=r.json()
    reply=result["choices"][0]["message"]["content"]
    print("AI回答：",reply)
else:
    print("出错了，状态码是：",r.status_code)
    print(r.text)