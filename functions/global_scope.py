chai_type = "Plain"

def front_desk():
    def Kitchen():
        global chai_type
        chai_type = "Irani"

    Kitchen()

front_desk()
print("Final global chai: ", chai_type)