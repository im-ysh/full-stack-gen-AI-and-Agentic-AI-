flavours = ["tulasi","vanilla","chocolate","strawberry","out of stcok","dicontinued"]

for flavour in flavours:
    if flavour == "out of stock":
       continue
    if flavour == "dicontinued":
       break
    print(f"{flavour} item found")

print("outside of the loop")