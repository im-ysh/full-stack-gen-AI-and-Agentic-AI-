class ChaiUtils:
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
raw = " water , milk  , ginger , honey "

# obj = ChaiUtils()
# obj.clean_ingredients(raw)
# usal way to create object and call method but here we can call method without creating object because its static method

# sttaic methods doesnt need object creation

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)