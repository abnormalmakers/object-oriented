class Student(object):
    count=68
    class_name='2班'

    @classmethod
    def all_student(cls):
        """类方法不能访问实例变量"""
        return cls.count

    def __init__(self,name,count):
        self.name=name
        self.count=count

    def re_count(self):
        return self.count

    def re_classname(self):
        return self.class_name

    @staticmethod
    def re_score(score):
        score+=10
        return score

s=Student('张三',70)
print(s.name)
print(s.all_student())
print(Student.all_student())
print(s.re_count())
print(Student.re_count(s))
print(s.re_score(50))
print(Student.re_score(50))

print(s.class_name)
print(s.re_classname())