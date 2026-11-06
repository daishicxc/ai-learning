import json
import os
FILE_NAME="contact.json"
if os.path.exists(FILE_NAME):
    with open(FILE_NAME,"r",encoding="utf-8") as f:
         contacts=json.load(f)
else:
     contacts={}
     print("没读取到，新建了一个")
name=input("输入名字：")
number=input("输入号码：")
contacts[name]=number
with open(FILE_NAME,"w",encoding="utf-8") as f:
     json.dump(contacts,f,ensure_ascii=False)
     print("保存成功")