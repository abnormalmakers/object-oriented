class Mylist(object):
    def __init__(self,value):

        self.lists=value
        print(self.lists)

    def __str__(self):
        return str([x for x in self.lists])

l=Mylist(range(10))
print(l)