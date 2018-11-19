class Mylist:
    def __init__(self,iterable):
        self.l=list(iterable)

    def __repr__(self):
        return str(self.l)

    def __mul__(self, other):
        return self.l*other

    def __rmul__(self, other):
        return self.l*other


l=Mylist([1,2,3])
print(l)
print(l*2)
print(3*l)