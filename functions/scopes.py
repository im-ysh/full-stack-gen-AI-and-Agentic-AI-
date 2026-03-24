# def serve_chai():
#     chai_type = "Masala"
#     print(f"Inside fxn : {chai_type}")

# chai_type = "lemon"
# print(f"outside fxn:{chai_type}")
# serve_chai()


def chai_ctr():
    chai_type = "ginger"
    def print_order():
        chai_type = "choco"
        print(f"inside fxn: {chai_type}")
    print_order()
    print(f"outside fxn: {chai_type}")

chai_type = "mint"
chai_ctr()
print(f"global scope : {chai_type}")