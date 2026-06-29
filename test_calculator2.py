import pytest
import builtins
from calculator import main

def test_add(monkeypatch, capsys):
    inputs = iter(["5", "+", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    # 这里的 .strip() 是终极绝招，去除所有隐藏的换行符和空格
    assert "运算类型: 加法" in captured.out.strip()
    assert "计算结果: 8.00" in captured.out.strip()

def test_sub(monkeypatch, capsys):
    inputs = iter(["5", "-", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "运算类型: 减法" in captured.out.strip()
    assert "计算结果: 2.00" in captured.out.strip()

def test_div_by_zero(monkeypatch, capsys):
    inputs = iter(["5", "/", "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "错误：除数不能为零！" in captured.out.strip()

def test_invalid_op(monkeypatch, capsys):
    inputs = iter(["5", "^", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "错误: 无效运算符 '^'" in captured.out.strip()