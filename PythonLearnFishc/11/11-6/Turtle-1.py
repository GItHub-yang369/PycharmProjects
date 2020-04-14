# 组合实例演示,组合：接把需要的类放进去实例化
class Turtle:
    def __init__(self, x):
       self.num = x


class Fish:
    def __init__(self, y):
        self.num = y


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def printXY(self):
        print("一共有 %d 只乌龟，%d 条鱼" % (self.turtle.num, self.fish.num))


pp = Pool(1, 2)
pp.printXY()
