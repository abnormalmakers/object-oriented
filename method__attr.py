class Student(object):
    count=68
    class_name='2班'
    _s=123
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
# 访问实例属性
print(s.name)

# 访问类方法
print(s.all_student())
print(Student.all_student())

# 访问实例方法
print(s.re_count())
print(Student.re_count(s))

# 访问静态方法
print(s.re_score(50))
print(Student.re_score(50))

# 访问类变量
print(s.class_name)

# 访问实例方法
print(s.re_classname())
print('s._s',s._s)