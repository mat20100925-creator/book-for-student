class Student:
    def __init__(self, name, age, height ):
        self .height = height
        self.name = name
        self.age = age

    def grow(self, height):
        self.height += height

matvii = Student(name='Matvii', age=13, height=180 )
print("Height" ,matvii.height)
print("NAme" ,matvii.name)
print("Age" ,matvii.age)

matvii.grow(height=5)
print("Height" ,matvii.height)





