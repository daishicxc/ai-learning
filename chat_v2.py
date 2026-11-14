import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("DEEPSEEK_API_KEY")
messages=[]
while True:
    user_input=input("你：")
    if user_input=="quit":
        break
    messages.append({"role":"user","content":user_input})
    headers={"Authorization":f"Bearer {API_KEY}","Content-Type":"application/json"}
    data={"model":"deepseek-chat","messages":messages}
    r=requests.post("https://api.deepseek.com/chat/completions",headers=headers,json=data)
    if r.status_code==200:
        reply=r.json()["choices"][0]["message"]["content"]
        print("AI:",reply)
        messages.append({"role":"assistant","content":reply})
        print("_"*20)
    else:
        print("响应码：",r.status_code)