
fruits = ["苹果","香蕉","橙子"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])

fruits.append("葡萄")
print(fruits)
print(len(fruits))

print(fruits[0])
print(fruits[-1])
print(fruits[1:3])

person = {"name":"xiaoming","age":18}
print(person)
print(person["name"])
print(person["age"])

person["age"] = 20
person["city"] = "xian"
print(person)
print(person["age"])
print(person["city"])

for f in fruits:
    print(f)

for k in person:
    print(k,person[k])

