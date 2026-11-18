import json
user={"name":"张三","age":25,"skills":["Python","AI"]}
with open("user.json","w",encoding="utf-8") as f:
    json.dump(user,f,ensure_ascii=False,indent=4)
