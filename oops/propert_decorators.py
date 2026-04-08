class TeaLeaf:
    def __init__(self,age):        self.age = age

# Methods inside __init__ are local functions
# They are NOT part of the class
# Python will never register them as properties
# Properties must be defined at the class level, not inside __init__.


    @property
    def age(self):
        return self._age + 2
        
    @age.setter
    def age(self,age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")
            

leaf = TeaLeaf(2)
print(leaf.age)
