class C:
    def __init__(self):
        print("__init__方法")

    def __del__(self):
        print("__del__方法")


c1 = C()
c2 = c1
c3 = c2
print("c1调用输出：")
del c1
print("c2调用输出：")
del c2
print("c3调用输出：")  # 当所有对该对象的引用都不再指向该对象的时候才进行回收
del c3
