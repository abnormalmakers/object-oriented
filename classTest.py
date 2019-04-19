class Test():
    a=1
    __b=2

    @classmethod
    def clsfn(cls):
        print('it is clsfn---------------')
        print("访问类变量",cls.a)
        print("访问私有属性", cls.__b)
        # cls.staticfn(cls.a,cls.__b)

    def fn(self):
        print('it is selffn----------------')
        # self.staticfn(self.a,self.__b)
       

    @staticmethod
    def staticfn(a,b):
        print('it is staticfn-----------------')
        print(a)
        print(b)



t=Test()
t.clsfn()
# 私有属性类的外部无法访问
# print(t.__b)
t.fn()





