a = [2, 4, 6, 8, 10]

# Initialize total sum to zero
total_sum = 0

# Iterate over each element in list
# and accumulate sum
for val in a:
    total_sum += val

# Calculate average by dividing total sum
# by length of list
avg = total_sum / len(a)

print(avg)