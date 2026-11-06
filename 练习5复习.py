import random
A=random.randint(1,100)
C=[]
D=0
E={}
while True:
    B=int(input("请输入一个数字："))
    C.append(B)
    D=D+1
    E[B]=E.get(B,0)+1
    if B>A:
        print("您的猜测偏大")
    elif B<A:
        print("您的猜测偏小")
    else:
        print("恭喜您猜对了！本次答案是：",B)
        print(f"您本次共猜测{D}次")
        print("您本次猜测过的数字是",sorted(list(set(C))))
        for x in E:
            print("您本次猜测",E[x],"次数字",x)
        break
