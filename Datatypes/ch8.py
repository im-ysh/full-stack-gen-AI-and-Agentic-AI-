ingredients = ["water","milk","black tea"]
ingredients.append("sugar")
print(f"Ingredients are : {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger","cardamom"]
chai_ingredients = ["water" , "milk"]
chai_ingredients.extend(spice_options)
print(f"chai : {chai_ingredients}")
chai_ingredients.insert(2,"black tea")
print(f"chai : {chai_ingredients}")
last_added = chai_ingredients.pop()
print(f"{last_added} is the last added")
print(f"chai: {chai_ingredients}")
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"chai : {chai_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar levels: {max(sugar_levels)}")
print(f"Minimum sugar levels: {min(sugar_levels)}")

base_liquid = ["water","milk"]
extra_flavour = ["ginger"]

full_liuid_mix = base_liquid + extra_flavour
print(f"Liquid mix: {full_liuid_mix}")

strong_brew = ["black Tea" , "water"] * 3
print(f"Strong brew: {strong_brew}")

raw_spice_data = bytearray(b"Cinnamon")
print(f"raw spice data : {raw_spice_data}")
#
raw_spice_data = raw_spice_data.replace(b"Cinna",b"card")
print(f"raw spice data : {raw_spice_data}")
print(f"bytes : {raw_spice_data}")

