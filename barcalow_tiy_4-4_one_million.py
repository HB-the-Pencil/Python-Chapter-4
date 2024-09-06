# I'm glad I figured out how to use scientific notation in ranges earlier. It's much more condensed.
one_million = list(range(1, int(1e6+1)))

# Loop through the whole list and print one number at a time.
for value in range(len(one_million)):
    print(one_million[value])

# I think it would have been faster to just print the list, but whatever.
# Also, why couldn't I just make a loop (1-1M) and add each value and print it at the same time?