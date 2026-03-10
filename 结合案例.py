# 定义商品名称（字符串）、单价（浮点数）、数量（整数）、是否有折扣（布尔值）；
# 计算：原价总价 = 单价 × 数量；若有折扣，总价打 8 折；
# 格式化输出结果（如 “商品：苹果，单价：5.5 元，数量：3 个，原价：16.5 元，折后价：13.2 元”）

product_name ="苹果"
price = 5.6
count = 3
has_discount = True

original_total = price * count
if has_discount:
    final_total = original_total * 0.8
else:
    final_total = original_total

print(f"商品：{product_name}")
print(f"单价：{price}元，数量：{count}个")
print(f"原价：{original_total:.1f}元")
print(f"是否有折扣：{has_discount}，折后价：{final_total:.1f}元")