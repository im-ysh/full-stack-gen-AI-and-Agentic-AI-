class chai:
    origin = "India"

print(chai.origin)

#if any variable goes inside a class it becomes a property 


chai.is_hot = True
print(chai.is_hot)

masala = chai()
print(masala.origin)
print(masala.is_hot)

masala.is_hot = False
print(chai.is_hot)
print(masala.is_hot)