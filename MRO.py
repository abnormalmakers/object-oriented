class A():
    def m(self):
        print('A.m')

class B(A):
    def m(self):
        print('B.m')
        # 这里的super是按照mro顺序调用的
        super().m()

class C(A):
    def m(self):
        print('C.m')

class D(B,C):
    def m(self):
        print('D.m')
        super().m()


d=D()
for i in D.__mro__:
    print(i)
d.m()
