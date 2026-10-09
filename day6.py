
with open("numbers.text","w") as f:
    f.write("10\n20\n30\n")


with open("numbers.text","r") as f:
    content = f.read()

print(content)
print(type(content))

lines = content.split("\n")
print(lines)

total = 0
for line in lines:
    if line !="":
        total = total + int(line)

print("总和是：",total)

with open("result.txt","w",encoding="utf-8") as f:
    f.write("总和是：" + str(total))
