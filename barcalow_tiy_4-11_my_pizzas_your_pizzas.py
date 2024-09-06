# Ye olde list of pizzas. That was so long ago...
pizzas = ["supreme", "sausage", "hawaiian", "pepperoni"]

# My friend has good tastes.
friend_pizzas = pizzas[:]

pizzas.append("taco")  # an underrated pizza in my opinion
friend_pizzas.append("cheese")  # an overrated pizza in my opinion

# huzzah! list comprehensions!
print("My favorite pizzas are:")
[print(pizza) for pizza in pizzas]

print("My friend's favorite pizzas are:")
[print(pizza) for pizza in friend_pizzas]