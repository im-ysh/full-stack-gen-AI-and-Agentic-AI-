# def make_chai():
#     return "this is masala chai"


# return_value = make_chai()

# print(return_value)

# # print(make_chai())


def chai_status(cups_left):
    if cups_left == 0:
        return "sorry! chai over"
    return "chai is ready"
    print("chai")

# here it is not printing chai because return statement is there before print statement so its early from a function 
print(chai_status(0))
print(chai_status(6))


def chai_report():
    return 10,20


sold,remaining = chai_report()
print("sold: ",sold)
print("remaining:",remaining)