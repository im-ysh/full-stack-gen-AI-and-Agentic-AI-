def add_vat(price,vat_rate):
    price = price - (price * vat_rate/100)
    return price

orders = [12000,10000,8000]

for order in orders:
    final_amt = add_vat(order,10)
    print(f"original price: {order} and final price with VAT : {final_amt}")


