# chai = "Ginger Tea"

# def prepare(order):
#     print("Preparing" , order)

# prepare(chai)
# print(chai)

# list is immutable

def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)


make_chai("Darjeeling","Yes","Low")  #positional
make_chai(tea="green",sugar="medium",milk="no") #keywords

def spl_chai(*ingredients,**extras):
    print("Ingredients",ingredients)
    print("Extras",extras)

# args and kargs
spl_chai("cinnamon","cardamom",sweetener="Honey",foam="yes")


def chai_order(order = None):
    # order.append("Masala")
    if order is None:
        order = []
        
    print(order)

chai_order()
chai_order()
#  You CAN use default arguments if the value is IMMUTABLE.
#  You SHOULD NOT use default arguments if the value is MUTABLE.
    