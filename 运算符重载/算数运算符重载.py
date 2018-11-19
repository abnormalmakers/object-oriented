class Mynumber(object):
    def __init__(self,v):
        self.data=v

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        result=self.data+other.data
        return Mynumber(result)

    def __sub__(self, other):
        result=self.data-other.data
        return Mynumber(result)

    def __mul__(self, other):
        result=self.data*other.data
        return Mynumber(result)

    def __truediv__(self, other):
        result=self.data/other.data
        return Mynumber(result)

    def __floordiv__(self, other):
        result = self.data // other.data
        return Mynumber(result)

add_a=Mynumber(100)
add_b=Mynumber(200)
add_c=add_a+add_b
print(add_b)

sub_a=Mynumber(100)
sub_b=Mynumber(200)
sub_c=sub_a+sub_b
print(sub_c)

mul_a=Mynumber(100)
mul_b=Mynumber(200)
mul_c=mul_a*mul_b
print(mul_c)

truediv_a=Mynumber(100)
truediv_b=Mynumber(200)
truediv_c=truediv_a/truediv_b
print(truediv_c)


truediv_a=Mynumber(100)
truediv_b=Mynumber(200)
truediv_c=truediv_a//truediv_b
print(truediv_c)

str