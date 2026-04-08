# pure fxn
# def pure_chai(cups):
#     return cups*10

# total_chai = 0


# not reccomeneded - impure fxn
# def impure_chai(cups):
#     global total_chai
#     total_chai += cups

# def pour_chai(n):
#     if n == 0:
#         return "all cups poured"
#     return pour_chai(n-1)


# print(pour_chai(6))

# chai_types = ["light","kadak","ginger","kadak"]
# strong_chai = list(filter(lambda chai: chai =="kadak", chai_types))
# print(strong_chai)


def chai_flavour(flavour = "masala"):

    """return the flavour of chai"""
    return flavour


print(chai_flavour.__doc__)
print(chai_flavour.__name__)
# help(len)

def gen_bill(chai=0,bis = 0):
    """
    calculate the total bill for chai and samosa
    :param chai: no of chai cups (10 rupees each)
    : return (total amt, thank you msg)
    """

    total = chai*10 + bis*15
    return total, " thank you for visiting"
