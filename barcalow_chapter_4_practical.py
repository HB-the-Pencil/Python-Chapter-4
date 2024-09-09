"""TODO:
[X] Loop through the list and create a print statement that tell me this is
    the candy your group would like.

[X] Create a second list that shows the cost of 6 of each types of candy. You
    will have to find that information. (Try Amazon)

[X] Concatenate the two list to show the cost of each type of candy. If you
    can do this as a loop that would be great but not necessary.

[X] Create a copy of the candy list and call it alternate candy. You will
    append the list and add two other types of candy that we can order if the
    second and third types of candy in your list are not available.

[X] Take the second and third types of candy out and create a print statement
    using your list that will say "if item 2 is not available then" replace it
    with one of the new types you entered into you list. Do this again for the
    third item in you list. Make sure you alternate items are not the same.

[X] At the end of your program print candy_list and alternate_candy. They
    should be different.
"""

# Initialize the list. I modified the list to replace a duplicate Twix with
# 3 Musketeers instead.
favoriteCandies = ["Lemonheads", "Milky Way", "Twix", "3 Musketeers",
                   "Reese's", "Airheads", "Almond Joy"]

# Print a list of the candies we want.
print("For Halloween this year, we would like the following candies:")
for candy in favoriteCandies:
    print(candy)
print()  # Create a blank line before the next block of print statements.

# Create a list showing how much it costs to buy this candy. I looked for bulk
# prices, enough for our entire class. You should be able to find these prices
# on the first page at Amazon.
candyPrices = [11.81, 19.99, 24.99, 9.99, 26.95, 9.84, 6.99]

# Print the cost of each piece of candy. I predict that this will eventually
# become a dictionary.
print("Prices:")
for index in range(len(favoriteCandies)):
    print(favoriteCandies[index] + ": $" + str(candyPrices[index]))
print()

# Create a copy of the list that removes the second and third items and
# replaces them with other candies.
altCandies = favoriteCandies[:]
del altCandies[1]
del altCandies[1]  # The item at index 3 is now at index 2.
altCandies.append("Twizzlers")
altCandies.append("Dots")

# Inform Mr. McKinstry of our alternate choices.
print(f"If {favoriteCandies[1]} bars are not available, please buy "
      f"{altCandies[-2]} instead.")
print(f"If {favoriteCandies[2]} bars are not available, please buy "
      f"{altCandies[-1]} instead.")

# Prove that the lists are different.
print(favoriteCandies)
print(altCandies)