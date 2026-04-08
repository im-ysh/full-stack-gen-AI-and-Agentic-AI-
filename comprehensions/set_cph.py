# fav_chai = [
#     "masala chai","green tea", "lemon tea",
#     "green tea","elachi chai"
# ]

# unique_chai = {chai for chai in fav_chai}
# print(unique_chai)

recipes = {
    "masala chai" : ["ginger","cardamom","clove"],
    "elachi chai" : ["cardamom" , "milk"],
    "spicy chai" : ["ginger","black pepper","clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)