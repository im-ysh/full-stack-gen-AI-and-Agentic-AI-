menu = ["green" , "lemon", "spiced" , "mint"]
list_menu = list(enumerate(menu,start=1))
for idx,m in list_menu:
    print(f"menu item is {idx} : {m}")