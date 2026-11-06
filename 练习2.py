体重=float(input("体重："))
身高=float(input("身高："))
bmi=体重/身高**2
if bmi>32:
    print("严重肥胖")
elif bmi>=28:
    print("肥胖")
elif bmi>=25:
    print("超重")
elif bmi>=18.5:
    print("正常")
else:
    print("过轻")