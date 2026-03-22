snack = input("enter your preferred snack: ").lower()

print(f"user said: {snack}")

# The input() function in Python is used to take user input from the keyboard. It pauses program execution
#  until the user types something and presses Enter, then returns the entered value as a string by default.

if snack=="cookies" or snack=="samosa":
   print(f"great choice! we wil serve you")
else:
    print("sorry not available")