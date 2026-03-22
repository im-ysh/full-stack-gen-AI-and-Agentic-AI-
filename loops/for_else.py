staff = [("amit",16),("zara",27),("raj",23)]
#list of tuples

for name,age in staff:
    if age >= 18:
        print(f"{name} is eligible for staff mangagement")
        break
    else:
        print("Ineligible")
        