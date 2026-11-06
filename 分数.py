def XXX():
 分数=int(input("请输入你本次分数："))
 if 分数>=90:
  return "A"
 elif 分数>=80:
  return "B"
 elif 分数>=60:
  return "C"
 elif 分数>100 or 分数<0:
  return "输入有误"
 else:
  return "D"
X=XXX()
print(X)