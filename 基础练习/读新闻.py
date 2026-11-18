with open("新闻.txt","r",encoding="utf-8") as f:
    print(len(f.read()))    
    f.seek(0)
    line=f.readlines()
    print(f"{len(line)}行")