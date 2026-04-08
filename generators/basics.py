# def serve_chai():
#     yield "cup 1: masala chai"
#     yield "cup 2: masala chai"
#     yield "cup 3: elachi chai"



# stall = serve_chai()

# for cup in stall:
#     print(cup)

def get_chai_gen():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"



chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))