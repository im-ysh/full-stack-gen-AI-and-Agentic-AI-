chai_order = dict(type="masala chai",size = "large",sugar=2)
print(f"chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"recipe base: {chai_recipe['base']}")
print(f"recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"recipe : {chai_recipe}")

print(f" Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "ginger chai", "size":"medium","sugar":1}
print(f"order details(keys): {chai_order.keys()}")
print(f"order details (values): {chai_order.values()}")
print(f"order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"last item removed: {last_item}")


extra_recipe = {"cardamom":"crushed","ginger":"sliced"}
chai_recipe.update(extra_recipe)

print(f"updated chai recipe: {chai_recipe}")

customer_note = chai_order.get("size","NO Note")
print(f"chai size: {customer_note}")