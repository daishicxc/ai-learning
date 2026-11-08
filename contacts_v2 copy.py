import json
import os
def 存号码():
 FILE_NAME="contact2.json"
 try:
    os.path.exists(FILE_NAME)
    with open(FILE_NAME,"r",encoding="utf-8") as f:
         contacts=json.load(f)
 except Exception as e:
     contacts={}
     print("错误原因：")
     print("已新建")
 while True:
   print("_"*20)
   print("输入q结束")
   name=input("输入名字：").strip()
   if name=="q":
      break
   if name=="":
    print("名字不能为空")
    continue
   else:
    number=input("输入号码：").strip()
    if number=="" or not number.isdigit():
     print("号码不能为空且需为纯数字")
     continue
    else:
       contacts[name]=number
       print("已存入")
 try:
    with open(FILE_NAME,"w",encoding="utf-8") as f:
     json.dump(contacts,f,ensure_ascii=False)
     print("保存成功") 
 except Exception as e:
     print("保存失败")
def main():
  存号码()
if __name__ == "__main__":
    main()