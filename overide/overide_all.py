class Mylist(object):
    def __init__(self,iterator=()):
        self.data=[x for x in iterator]

    def __str__(self):
        return "Myobj(%s)"%str(self.data)

    def __repr__(self):
        return "Myobj(%s)"%self.data

    def __abs__(self):
        return Mylist((abs(x) for x in self.data))

    def __len__(self):
        return len(self.data)

    def __reversed__(self):
        l=self.data
        l.reverse()
        return l

    def __round__(self, n=None):
        return Mylist((round(x) for x in self.data))

    def __bool__(self):
        # return False
        return True

obj=Mylist([100.6,-200.3,300,-400])

# 重写__str__
print(obj)

# 重写__abs__
print(abs(obj))

# 重写__len__
print(len(obj))

# 重写__reverse__
print(reversed(obj))

# 重写__round__
print(round(obj))

# 重写__bool__
print(bool(obj))



