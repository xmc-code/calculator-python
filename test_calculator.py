from calculator import calculate

def test_add():
    result, msg = calculate(5, '+', 3)
    assert result == 8.0

def test_subtract():
    result, msg = calculate(5, '-', 3)
    assert result == 2.0

def test_multiply():
    result, msg = calculate(5, '*', 3)
    assert result == 15.0

def test_divide_by_zero():
    result, msg = calculate(5, '/', 0)
    assert result is None             # 除数为0，应该返回None
    assert msg == "错误：除数不能为零！"

def test_invalid_op():
    result, msg = calculate(5, '^', 3)
    assert result is None
    assert msg == "错误: 无效运算符 '^'"