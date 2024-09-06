# I've never used list comprehension before... let's see if I can get it without looking at the book.
cubes = [base ** 3 for base in range(1, 11)]

# haha! I remembered it! Let's print it and see if I did it right.
for cube in range(len(cubes)):
    print(cubes[cube])