def update_order():
    chai_type = "elachi"
    def kitchen():
        nonlocal chai_type
        chai_type = "kesar"
    kitchen()
    print("after kitchen update",chai_type)



update_order()