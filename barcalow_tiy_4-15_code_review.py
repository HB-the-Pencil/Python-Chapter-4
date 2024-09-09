# Code Modified: Summing a Million (TIY 4-5)

# Reuse the same list code.
# This code feels broken or like I'm cheating for some reason...
one_million = list(range(1, int(1e6+1)))

# Print the min and max of the list (just to make sure it's really a million).
print(f"Min: {min(one_million)}")
print(f"Max: {max(one_million)}")  # F-strings are my best friend :D

# Finally, let's sum the numbers... fingers crossed that it doesn't crash!!
sum_one_million = sum(one_million)
print(f"Sum of 1-1000000: {sum_one_million}")

# a) That was shockingly fast.
# b) It's really weird but cool that the sum is 500000500000: a five, followed
# by five zeroes, followed by a five, followed by five zeroes.


# Code Modified: Cubes (TIY 4-8)

# Aha! We cannot simply use list(range()) for this one!
cubes = []

# We need a for loop to pass values.
for base in range(1, 11):
    cubes.append(base ** 3)

# Loop through the list and print each number.
for cube in range(len(cubes)):
    print(cubes[cube])

# range(len()) still feels like something I'm not supposed to use yet...


# Code Modified: My Pizzas, Your Pizzas (TIY 4-11)

# Ye olde list of pizzas. That was so long ago...
pizzas = ["supreme", "sausage", "hawaiian", "pepperoni"]

# My friend has good tastes.
friend_pizzas = pizzas[:]
pizzas.append("taco")
friend_pizzas.append("cheese")

# Huzzah! List comprehensions!
print("My favorite pizzas are:")
[print(pizza) for pizza in pizzas]

print("My friend's favorite pizzas are:")
[print(pizza) for pizza in friend_pizzas]