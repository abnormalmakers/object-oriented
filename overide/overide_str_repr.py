class MyNuber():
    def __len__(self):
        for iterabel in [str,list,set,dict,tuple]:
            if isinstance(self, iterabel):
                return len(self)
        return 100


n=MyNuber()
print(len(n))

s="python"
s1=repr(s)
s2=str(s)

print("s1:",s1,type(s1))
print("s2:",s2,type(s2))

s3=eval(s1)
print("s3",s3)

try:
    s4=eval(s2)
except Exception as e:
    print(e)

print("=================================")
class Test():
    def __init__(self,value):
        self.value=value
        print(self.__class__)

    def __str__(self):
        return self.value

    def __repr__(self):
        return "Test(%s)"%self.value

t=Test('100')
print(str(t))
print(repr(t))
