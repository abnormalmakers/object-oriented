class A():
    def __init__(self):
        self.__p1 = 2

    def test(self):
        print(self.__p1)
        self.__m1()

    def __m1(self):
        print("我是A类的私有成员")


a = A()
# print(a.__p1)
# a.__m1()
a.test()



