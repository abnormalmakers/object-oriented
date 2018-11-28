# class Fibnacci(object):
#     def __init__(self,n):
#         self.n=n
#
#     def __iter__(self):
#         return Fibiterator(self.n)
#
# class Fibiterator(object):
#     def __init__(self,n):
#         self.n=n
#         self.a=0
#         self.b=1
#         self.cur=0
#
#     def __next__(self):
#         if self.cur>=self.n:
#             raise StopIteration
#
#         self.cur+=1
#         self.a,self.b=self.b,self.a+self.b
#         return self.a
#
#
# fib=Fibnacci(10)
#
# for i in fib:
#     print(i)
#
# l=[x for x in fib]
# print(l)


print("===================第二种方法======================")
class Fibnacci(object):
    def __init__(self,n):
        self.n=n

    def __iter__(self):
        print("iter调用")
        self.cur = 0
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        print('next调用')
        if self.cur>=self.n:
            raise StopIteration

        self.cur+=1
        self.a,self.b=self.b,self.a+self.b
        return self.a


fib=Fibnacci(10)

for i in fib:
    print(i)

# l=[x for x in fib]
# print(l)




