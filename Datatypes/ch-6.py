chai_type = "Ginger Chai"
customer_name = "vaishu"

print(f"order for {customer_name}:{chai_type} please!")

chai_description = "aromatic and bold"
print(f"first word:{chai_description[0:8:1]}")
print(f"first word:{chai_description[0:7]}")
print(f"first word:{chai_description[:8]}")
print(f"last word:{chai_description[12:]}")
print(f"last word:{chai_description[::-1]}")

label_text = "chai spécial"
encoded_label = label_text.encode("utf-8")
print(f"non encoded label:{label_text}")
print(f"encoded label:{encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"decoded label:{decoded_label}")
