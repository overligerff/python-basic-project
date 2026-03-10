
# 定义 2 个整数（如a = 10、b = 3）和 2 个浮点数（如c = 10.5、d = 2.0）；
# 依次计算：加法、减法、乘法、除法、取余、幂运算；
# 打印每个运算的结果，并打印结果的类型（用type()函数）。


a = 10
b = 3
c = 10.6
d = 2.0

print("整数计算：")
add_int = a + b
print(f"{a} + {b} = {add_int}, 类型：{type(add_int)}")
sub_int = a - b
print(f"{a} - {b} = {sub_int}, 类型：{type(sub_int)}")
mul_int = a * b
print(f"{a} * {b} = {mul_int}, 类型：{type(mul_int)}")
div_int = a / b
print(f"{a} /{b} = {div_int}, 类型：{type(div_int)}")
mod_int = a % b
print(f"{a} % {b} = {mod_int}, 类型：{type(mod_int)}")
pow_int = a ** b
print(f"{a} ** {b} = {pow_int}, 类型{type(pow_int)}")
print("-------------------------------------------------")
print("浮点计算：")
add_float = c + d
print(f"{c} + {d} = {add_float},类型{type(add_float)}")
sub_float = c - d
print(f"{c} - {d} = {sub_float} , 类型{type(sub_float)}")
mul_float = c * d
print(f"{c} * {d} = {mul_float} , 类型{type(mul_float)}")
div_float = c / d
print(f"{c} / {d} = {div_float} , 类型{type(div_float)}")
mod_float = c % d
print(f"{c} % {d} = {mod_float} , 类型{type(mod_float)}")
pow_float = c ** d
print(f"{c} ** {d} = {pow_float} , 类型{type(pow_float)}")
