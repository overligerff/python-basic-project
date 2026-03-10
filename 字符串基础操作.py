


# 定义一个字符串（如s = "Hello, Python!"）；
# 完成：拼接另一个字符串、重复 3 次、取第 5 个字符、切片取前 5 个字符、转大写 / 小写、计算长度；
# 打印所有操作结果。


s = "Hello World"
# 字符串拼接
concat_str = s + " let is go to learn"
print("拼接结果",concat_str)
# 字符串重复
repeat_str = s * 2
print("重复2次" , repeat_str)
# 索引（注意：Python索引从0开始）
index_char =s[4]
print("第五个字符是：" ,index_char)
# 切片（左闭右开）
slice_str = s[0:5]
print("前五个字符：",slice_str)
# 转大写/小写
upper_str = s.upper()
lower_str = s.lower()
print("转大写",upper_str)
print("转小写",lower_str)
# 计算长度
str_len = len(s)
print("字符串长度",str_len)
