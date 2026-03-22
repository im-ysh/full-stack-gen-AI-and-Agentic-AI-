name_list = ["ysh","rapline","maknaeline"]
bills = [1000,34000,40000]

for name,amt in zip(name_list,bills):
    print(f"{name} paid {amt}")
