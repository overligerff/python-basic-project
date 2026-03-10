# 1. 变量与数据类型
name = "AI开发学习"
age = 22
score = 95.5
is_student = True

# 打印所有变量
print(f"名称：{name}，类型：{type(name)}")
print(f"年龄：{age}，类型：{type(age)}")
print(f"分数：{score}，类型：{type(score)}")
print(f"是否学生：{is_student}，类型：{type(is_student)}")

# 2. 列表与切片
nums = [1, 2, 3, 4, 5]
print("列表前3个元素：", nums[:3])
print("列表倒序：", nums[::-1])

# 3. 字典操作
student = {"name": "张三", "age": 20, "score": 88}
print("学生姓名：", student["name"])
student["score"] = 90  # 修改分数
print("修改后分数：", student["score"])