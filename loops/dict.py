# 1. The users Variable
# users is a list of dictionaries.
# ✔ List
# A list is written using [] and stores multiple items:
# [ item1, item2, item3 ]

# ✔ Dictionary
# A dictionary is written using {key: value}, where each key stores some data.


users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id":2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]

# discounts is a dictionary, where:

# key = coupon code (e.g., "P20")
# value = a tuple describing the discount and A tuple is written using () and holds fixed values:


discounts = {
    "P20": (0.2,0),
    "F10": (0,10),
    "P50": (0.5,0),
}

for user in users:
    percent,fixed = discounts.get(user["coupon"],(0,0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")
