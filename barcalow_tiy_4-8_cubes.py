# aha! we cannot simply use list(range()) for this one!
cubes = []

# We need a for loop to pass values.
for base in range(1,11):
    cubes.append(base ** 3)

# Loop through the list and print each number.
for cube in range(len(cubes)):  # range(len()) still feels like something I'm not supposed to use yet...
    print(cubes[cube])