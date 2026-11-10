import requests
AI_KEY="sk-14ad417c476c42d28847e7a64f02e863"
headers={"Authorization":f"Bearer {AI_KEY}","Content_Type":"application/json"}
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