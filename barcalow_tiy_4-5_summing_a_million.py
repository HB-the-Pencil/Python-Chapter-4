# Reuse the same list code. This code feels broken or like I'm cheating for some reason...
one_million = list(range(1,int(1e6+1)))

# Print the minimum and maximum of the list (just to make sure it's really a million).
print(f"Min: {min(one_million)}")
print(f"Max: {max(one_million)}")  # f-strings are my best friend :D

# Finally, let's sum the numbers... fingers crossed that it doesn't crash!!
sum_one_million = sum(one_million)
print(f"Sum of 1-1000000: {sum_one_million}")

# a) that was shockingly fast
# b) it's really weird but cool that the sum is 500000500000. 5, 5 zeroes, 5, 5 zeroes.