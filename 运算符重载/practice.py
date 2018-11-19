class Mylist():
    def __init__(self,iterable):
        self.l=list(iterable)

    def __add__(self, other):
        result=self.l+other.l
        return Mylist(result)

    def __mul__(self, other):
        return self.l*other
        # result=[x for x in map(self.fn,self.l)]
        # return result

    # def fn(self,l):
    #     return l*2

    def __add__(self, other):
        result=self.l+other.l
        return result

    def __str__(self):
        return str(self.l)


a=Mylist([1,2,3])
print(a*2)
# print(2*a)
b=Mylist([4,5,6])
c=a+b
print(c)


l=[1,2,3]
def fn(l):
    return l*2
arr=[x for x in map(fn,l)]
print(arr)
