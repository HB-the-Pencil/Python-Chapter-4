# Make a list of the multiples of three from 3 to 30.
threes = list(range(3, 31, 3))

# Loop through the list and print it.
for three in range(len(threes)):
    print(threes[three])

# Using "for three in threes" does not work. I wonder if there's another way to loop through the list.

# Here's another way to make the list using modulo (which is probably much less efficient):
threes = []
for number in range(1, 31):
    if number % 3 == 0:
        threes.append(number)

# Then print it out.
for three in range(len(threes)):
    print(threes[three])

# There's no way this is more efficient. I mostly just did it for fun, to see if I could use modulo
# to achieve the same effect. I use modulo a lot in JavaScript for frame-based animations.
# For example:
#
# if (frame % 5 === 0) {
#     background(255);
# }
# else {
#     background(0);
# }
#
# This code would make a background that flashes white every 5 frames.
# Just one use of modulo that I especially enjoy :D