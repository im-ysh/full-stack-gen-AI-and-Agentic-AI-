order = int(input("enter amount: "))
print(f"type of order : {type(order)}")
if order <= 300:
    del_fee = 30
    print(f"{del_fee} delivery free")
else:
    del_fee = 0
    print(f"{del_fee} delivery fee")


delivery_fees = 30 if order < 300 else 0
print(f"{delivery_fees} delivery fees")