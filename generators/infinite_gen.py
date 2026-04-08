def infinite_generator():
    cnt = 1
    while True:
        yield f"Refill #{cnt}"
        cnt += 1

refill = infinite_generator()
user2 = infinite_generator()
 
print("refill:")
for _ in range(5):
    print(next(refill))

print("user 2:")
for _ in range(6):
    print(next(user2))