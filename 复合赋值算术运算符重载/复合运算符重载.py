class Mylist():
    def __init__(self,iterable):
        self.l=list(iterable)

    def __add__(self, other):
        return Mylist(self.l+other.l)

    def __repr__(self):
        return "Mylist("+str(self.l)+")"

    def __iadd__(self, other):
        self.l.extend(other.l)
        return self

l1=Mylist([1,2,3])
l2=Mylist([4,5,6])
print(l1+l2)
l1+=l2
print(l1)
