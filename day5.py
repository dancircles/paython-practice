
with open("test.txt","w") as f:
    f.write("你好，文件")
    
    

with open("test.txt", "r") as f:
    content = f.read()
    print(content)

try:
    with open("不存在的文件.txt", "r") as f:
        content = f.read()
        print(content)
except:
    print("文件读不了，出错了")