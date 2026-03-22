# value = 13
# remainder = value % 5

# if remainder:
#     print(f"remainder is {remainder}")


# value = 13
# if(remainder:=value%5):
#     print(f"remainder is {remainder}")
    


# available_sizes = ["small","medium","large"]

# if(req_size := input(f"enter req size : ")) in available_sizes:
#     print(f"the requested size : {req_size} is available")
# else:
#     print(f"not available - {req_size}")


flav = ["masala","ginger","lemon","mint"]
print("availble flavours: ",flav)

while(f := input("enter the flavour you want:" )) not in flav:
    print(f"sorry {f} is not available")

print(f"{f} chai is available")