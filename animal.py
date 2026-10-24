class Enimal:
    def __init__(self, name, age, height ):
        self .height = height
        self.name = name
        self.age = age

    def grow(self, height):
        self.height += height

fox = Enimal(name='Fox', age=1, height=40 )
print("Height" ,fox.height)
print("Name" ,fox.name)
print("Age" ,fox.age)

fox.grow(height=4)
print("Height" ,fox.height)
