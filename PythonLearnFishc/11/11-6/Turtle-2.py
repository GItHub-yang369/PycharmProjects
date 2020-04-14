"""
类、类对象、实例对象
"""


class Turtle:
    count = 0


t = Turtle()
b = Turtle()
n = Turtle()
print(t.count, b.count, n.count, end=" <初始值\n")  # 实例对象输出值

"""实例对象改变值之后输出值"""
t.count += 10
print(t.count, b.count, n.count, end=" <实例对象t.count加10改变值之后输出值\n")

"""类对象该表值之后输出值"""
Turtle.count += 20
print(t.count, b.count, n.count, end=" <类对象更改值加20之后输出值\n")  # 可以看到实例t的变量值count没有改变

"""再次更改实例值之后输出"""
b.count += 10
print(t.count, b.count, n.count, end=" <再次更改实例b.count值之后输出\n")  # b的变量count在类变量count值的基础上增加值

"""类对象再次该表值之后输出值"""
Turtle.count += 30
print(t.count, b.count, n.count, end=" <类对象更改值加30之后输出值\n")

# 可以看到只要实例对象值没有赋值，则就输出类对象值，当实例对象赋值之后则类对象无法再改变实例对象值
