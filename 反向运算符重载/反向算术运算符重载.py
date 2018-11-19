class Mylist:
    def __init__(self,iterable):
        self.l=list(iterable)

    def __repr__(self):
        return str(self.l)

    def __mul__(self, other):
        return self.l*other

    def __rmul__(self, other):
        return self.l*other

    def __add__(self, other):
        return self.l+other

    def __radd__(self, other):
        return other+self.l


l=Mylist([1,2,3])
print(l)
print(l*2)
print(3*l)

print(l+[4,5,6])
print([4,5,6]+l)