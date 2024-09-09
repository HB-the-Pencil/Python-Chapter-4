# I like buffets... they aren't my favorite, but they're pretty good.
buffet = ("Coleslaw", "Rolls", "Green Beans", "Ham", "Scrambled Eggs")
# Print out the list (I cannot think of a reason to ever not use list comprehension.
# It's like my obsession with f-strings).
[print(food) for food in buffet]

# Dang! Python won't let me get rid of that horrible coleslaw!
# buffet[0] = "Applesauce"  # This does throw an error, you can uncomment to test it.

# Guess we just have to totally redo our menu to get rid of coleslaw.
buffet = ("Applesauce", "Rolls", "Baked Beans", "Ham", "Scrambled Eggs")

# Do not let Melody see how old-mannish my list is
[print(food) for food in buffet]