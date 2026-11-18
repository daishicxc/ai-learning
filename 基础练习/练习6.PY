A={"cxc":123,"cxz":234,"cxx":345,"cxv":456}
a=input("请输入名称：")
if a in A:
    print(A[a])
else:
    print("未查询到")