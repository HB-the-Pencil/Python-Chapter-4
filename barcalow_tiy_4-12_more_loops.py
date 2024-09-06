# Copy over the list of foods again.
fruits = ["mango", "kiwi", "pineapple", "blueberry", "strawberry", "peach", "lemon", "apple"]

# Oh no! I have to print them all! whAtEveR wIlL I dO??

# method number one (learned from the list comprehension video)
print("Method 1")
for fruit in fruits:
    print(fruit)

print()
# method number two (learned on my own)
print("Method 2")
for fruit in range(len(fruits)):
    print(fruits[fruit])

print()
# method number three (list comprehension)
print("Method 3")
[print(fruit) for fruit in fruits]