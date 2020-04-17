class C:
    def __init__(self, x=6):
        self.x = x


c1 = C()
print(hasattr(c1, 'x'))  # 返回对象中是否有指定的属性
print(getattr(c1, 'x'))  # 返回对象指定的属性值或者默认的属性值
setattr(c1, 'x', 9)  # 设置对象属性值
print(getattr(c1, 'x'))
delattr(c1, 'x')  # 删除对象属性
print(getattr(c1, 'x'))  # 删除之后再输出会报错
