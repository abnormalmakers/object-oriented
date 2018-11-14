class Prime():
    def __init__(self,n):
        self.n=n

    def __iter__(self):
        self.cur=0
        self.a=self.b=2
        return self

    def __next__(self):
        if self.cur>=self.n:
            raise StopIteration
        self.cur+=1

        self.b+=1

        while True:
            for i in range(2,self.b):
                if self.b%i==0:
                    self.b+=1
                    break
            else:
                return self.b



p=Prime(5)
print(p,type(p))
for i in p:
    print(i)
    # 2,3,5,7,11

l=[x for x in Prime(10)]
print(l)