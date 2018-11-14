class Mylist(object):
    def __init__(self,iterator=()):
        self.data=list(iterator)

    def __str__(self):
        return "Mylist(%s)"%self.data

    def __iter__(self):
        """有此方法就是可迭代对象，但要求必须返回迭代器 return一个迭代器"""
        return Myiterator(self.data)


class Myiterator():
    """用此类创建一个迭代器对象，用此迭代器对象可访问Mylist类型数据"""
    def __init__(self,data):
        self.cur=0
        self.data=data

    def __next__(self):
        if self.cur>=len(self.data):
            raise StopIteration
        data=self.data[self.cur]
        self.cur+=1
        return data


l=Mylist([1,2,3,4,5])
print(l)
print(iter(l))
it=iter(l)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
for i in l:
    print(i)




