# 完成：字符串转整数 / 浮点数、数值转字符串、数值转布尔值；
# 尝试转换无效值（如str("abc")转整数），并捕获异常（可选，新手可先注释）；
# 打印转换结果和类型。

# 1. 字符串转数值
str_num = "123"
int_from_str = int(str_num)
float_from_str = float(str_num)
print(f"字符串'{str_num}' 转整数{int_from_str}，类型:{type({int_from_str})}")
print(f"字符串'{str_num}' 转浮点数{float_from_str},类型：{type({float_from_str})}")

# 数值转字符串
num = 456.7
str_from_num = str(num)
print(f"数值{num}转字符串:'{str_from_num}' ,类型{type({str_from_num})}")

# 3. 数值转布尔值（0/0.0为False，其余为True）
print(f"0转布尔值:{bool(0)}")
print(f"100转布尔值：{bool(100)}")
print(f"0.0转布尔值：{bool(0.0)}")
print(f"-5.8转布尔值:{bool(-5.8)}")

