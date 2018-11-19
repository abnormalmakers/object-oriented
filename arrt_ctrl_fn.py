class Dog():
    color="white"
    def __init__(self,color):
        self.color=color

dog=Dog("red")
print("===================getattr=====================")
print(getattr(dog,"color"))
print(getattr(dog,"size",'middle'))


print("===================hasattr=====================")
print(hasattr(dog,"color"))
print(hasattr(dog,"age"))


print("===================setattr=====================")
setattr(dog,"color","black")
print(getattr(dog,"color"))
setattr(dog,"age","12")
print(getattr(dog,"age"))


print("===================delattr=====================")
delattr(dog,"color")
print(getattr(dog,"color"))