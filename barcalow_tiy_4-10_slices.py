# A list of fruit copied from foods.py. It was my longest list.
fruits = ["mango", "kiwi", "pineapple", "blueberry", "strawberry", "peach", "lemon", "apple"]

# Find the middle of the list.
mid_fruits = len(fruits)//2  # Integer division because we can't use a float index.

# Let's spice this up a bit!
fruits.sort()

# I. Love. F-strings.
print(f"The first three fruits alphabetically are: {fruits[:3]}")
print(f"The last three fruits alphabetically are: {fruits[-3:]}")
# Since it's non-inclusive of the last number, we need to add 2 to the middle instead of 1.
print(f"Three fruits from the middle of the list are: {fruits[mid_fruits-1:mid_fruits+2]}")