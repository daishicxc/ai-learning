import random
def playgame():
  A=random.randint(1,10)
  C=0
  D=[]
  E={}
  while True:
    B=int(input("请输入"))
    C=C+1
    D.append(B)
    E[B]=E.get(B,0)+1
    if B>A:
        print("大了")
    elif B<A:
        print("小了")
    else:
        print("猜对了：")
        print(f"本次猜了{C}次")
        print("本次猜过的数字是：")
        print(sorted(list(set(D))))
        for x in E:
            print("数字",x,"猜了",E[x])
        break
def main():
   playgame()
if __name__ =="__main__":
     main()