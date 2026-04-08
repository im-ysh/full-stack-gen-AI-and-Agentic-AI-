def chai_customer():
    print("welcome ! what chai would you like?")
    order = yield
    while True:
        print(f"preparing {order} chai")
        order = yield 


stall = chai_customer()
next(stall) #start the generator

stall.send("masala")