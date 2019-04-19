class A():
    def fn(self):
        print("A被调用")

    def run(self):
        print('A run')

class B(A):
    def fn(self):
        print("B被调用")

    def run(self):
        super(B,self).run()
        super(__class__,self).run()
        super().run()


a = A()
a.fn()
b = B()

b.fn()
b.__class__.__base__.fn(b)
print('aaaa')
super(B,b).fn()
print('aaaa')
b.run()

