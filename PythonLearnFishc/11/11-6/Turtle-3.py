class C:
    def x(self):
        print("Hello Python !")


a = C()
a.x()

a.x = 1
print(a.x)

# 当方法名称被变量名称覆盖之后则无法再调用原方法，如下方法执行会报错
# a.x()
