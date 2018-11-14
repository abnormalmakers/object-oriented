class Mylist(list):

    def insert_head(self,num):
        self.insert(0,num)
        return self


L=Mylist(range(1,5))
print(L)
L.insert_head(0)
print(L)