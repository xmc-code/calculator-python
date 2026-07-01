import math
def calculate(num1, op, num2=None):
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
    elif op == '^':
        return math.pow(num1, num2), "幂运算"  
    elif op == 's':
        return math.sin(math.radians(num1)), "正弦函数" 
    elif op == 'c':
        return math.cos(math.radians(num1)), "余弦函数"    
    else:
        return None, f"错误: 无效运算符 '{op}'"

def main():
    """只负责跟人聊天、接受输入、并调用上面的 calculate"""
    while True:                         
        try:                            
            op = input("请输入运算符 (+, -, *, /, ^, s=sin, c=cos, q=退出): ")  

            if op == 'q':              
                print("计算器已关闭，再见！")
                return                  # 退出 main 函数，程序结束

            if op in ('s', 'c'):        
                num1 = float(input("输入角度（度）: "))  
                num2 = None             # 三角函数不需要第二个数字
            else:
                num1 = float(input("输入第一个数字: "))  
                num2 = float(input("输入第二个数字: "))

        except ValueError:              
            print("【异常捕获】错误：您必须输入合法的数字！请重新输入。")
            continue                    # 跳回 while True 开头

        result, msg = calculate(num1, op, num2)  

        if result is None:              
            print(msg)                  # 打印错误信息
        else:
            print(f"运算类型: {msg}")
            print(f"计算结果: {result:.2f}")

        choice = input("是否继续？(y/n): ")  
        if choice.lower() == 'n':           
            print("计算器已关闭，再见！")
            return

if __name__ == "__main__":
    main()