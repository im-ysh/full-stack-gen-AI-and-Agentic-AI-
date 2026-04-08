class Chai:

    def __init__(self,type_,strength):
        self.type = type_
        self.strength = strength


# this is called code duplication, we are repeating the same code 
# class GingerChai(Chai):
#     def  __init__(self,type_, strength):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level

# this is explicit call
# class GingerChai(Chai):
#     def __init__(self,type_,strength,spice_level):
#         Chai.__init__(self , type_, strength)
#         self.spice_level = spice_level


# super() constructor call
class GingerChai(chai):
    def __init__(self,type_,strength,spice_level):
       super().__init__(type_,strength)
       self.spice_level = spice_level
