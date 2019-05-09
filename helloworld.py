# https://algorithm.joho.info/programming/python/sample-code-py/
# -*- coding: utf-8

# print練習
print("Hello World!")
print("こんにちは世界")

# 変数代入
a = 2  # 整数
b = 1.23  # 実数
c = "savar"  # 文字列
d = 1 + 2j  # 複素数
e = True  # 論理値
print(d)

# while練習
i = 0
while i < 5:
    i += 1
print(i)

# for練習
for i in range(0, 5, 1):
    print(i)

# if練習
i = 3
if i == 1:
    print("i = 1")
elif i == 2:
    print("i = 2")
elif i == 3:
    print("i = 3")
else:
    print("i = 4")

# 関数定義


def fanc(a, b):
    c = a + b
    return c


x = fanc(1, 2)
print(x)

# list練習
list1 = [1, 2, 3, 4, 5]
print(list1)  # [1, 2, 3, 4, 5]
print(list1[1])  # 2

# 異なるデータ型の要素をもてる
list2 = [1, 'two', 3, 'four', 5]
# スライスで2～3番要素のみ取り出して表示
print(list2[2:4])  # [3, 'four']
