class Human():
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def infos(self):
        print(self.name)
        print(self.age)


class Student(Human):
    def __init__(self, n, a, s):
        self.score = s
        super(__class__, self).__init__(n, a)

    def infos(self):
        super().infos()
        print(self.score)


s=Student('张三',24,100)
s.infos()