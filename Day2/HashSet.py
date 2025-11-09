# Approach 1: Create a set from a list to remove duplicates
li = [1, 2, 1, 2, 2, 5, 1, 9, 9, 5, 2]
hashset = set()

for ele in li:
    hashset.add(ele) 

print(hashset)  # Output: {1, 2, 5, 9}

# Approach 2: Create a set from a string to get unique characters
hs = set("sanjay")
print(hs)  # Output: {'a', 'j', 'y', 's', 'n'}
