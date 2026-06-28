# def main():
#     print("Hello,徒儿！Python  环境就绪，准备开战！")
# if __name__ == "__main__":
#     main()


# print("你好")
# print('nihao')
# name = "孙悟空"
# name2 = '猪八戒'
# age = 500
# print(f"名字：{name},{name2};年龄：{age}")

# name3 = input("请输入你的名字")
# print(name3)

# s = "123"
# n = int(s)
# f = float(s)

# print(s,n,f)

a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

if a > b:
    print("a大")
elif a == b:
    print("相等")
else:
    print("b大")



try:
    n = float(input("请输入数字："))  
except ValueError:
    print("输入错误：请输入数字")