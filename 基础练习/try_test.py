try:
   num=int(input("请输入一个数字："))
   print("您输入的是：",num)
except ValueError:
   print("错误，您输入的不是数字")