import requests
username="torvalds"
url=f"https://api.github.com/users/{username}"
print(f"正在向github请求{username}的信息...")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
r=requests.get(url,headers=headers)
if r.status_code==200:
    print(f"响应状态码：{r.status_code}")
    data=r.json()
    print("_"*20)
    print("用户名：", data["login"])
    print("注册时间：", data["created_at"])
    print("公开仓库数：", data["public_repos"])
    print("粉丝数：", data["followers"])
    print("_"*20)
else:
    print("请求失败，状态码：", r.status_code)