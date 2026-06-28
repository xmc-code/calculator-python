def main():
    try:
        num1 = float(input("请输入第一个数字："))
        op = input("输入运算符：（+，-，*，/）：")
        num2 = float(input("输入第二数字："))
    except ValueError:
        print("【异常捕获】错误：你必须输入合法的数字！程序终止。")
        return
    
    operator_name = ""
    if op == '+':
        result = num1 + num2
        operator_name = "加法"  #  print("运算类型：加法")
    elif op == '-':
        result = num1 - num2
        operator_name = "减法"  #  print("运算类型：减法")
    elif op == '*':
        result = num1 * num2
        operator_name = "乘法"  #  print("运算类型：乘法")
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
            operator_name = "除法"  #  print("运算类型：除法")
        else:
            print("错误：除数不能为零！")
    else:
        print(f"错误：无效运算符号'{op}',仅支持+，-，*，/")
        return
    
    print(f"运算类型：{operator_name}")
    print(f"计算结果：{result:.2f}")

if __name__ == "__main__":
    main()
        