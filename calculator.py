def calculate(num1, op, num2):
    """专门负责算数，不负责打印，算完直接返回结果"""
    if op == '+':
        return num1 + num2, "加法"  # 返回结果和运算类型
    elif op == '-':
        return num1 - num2, "减法"
    elif op == '*':
        return num1 * num2, "乘法"
    elif op == '/':
        if num2 != 0:
            return num1 / num2, "除法"
        else:
            return None, "错误：除数不能为零！"
    else:
        return None, f"错误: 无效运算符 '{op}'"

def main():
    """只负责跟人聊天、接受输入、并调用上面的 calculate"""
    try:
        num1 = float(input("请输入第一个数字: "))
        op = input("请输入运算符 (+, -, *, /): ")
        num2 = float(input("请输入第二个数字: "))
    except ValueError:
        print("【异常捕获】错误：您必须输入合法的数字！程序终止。")
        return
    
    result, msg = calculate(num1, op, num2)
    
    if result is None:  # 如果算出错误，直接打印错误信息
        print(msg)
    else:               # 如果算对了，打印结果
        print(f"运算类型: {msg}")
        print(f"计算结果: {result:.2f}")

if __name__ == "__main__":
    main()