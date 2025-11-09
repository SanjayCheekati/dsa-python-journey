from collections import defaultdict

# Approach 1: Using defaultdict to count frequencies
li = [1,2,1,2,2,5,1,9,9,5,2]
freq_dict = defaultdict(int)
for num in li:
    freq_dict[num] += 1
print(freq_dict)
print(dict(freq_dict))

# Approach 2: Using standard dict with manual key checks
freq = {}
for ele in li:
    if ele not in freq:
        freq[ele] = 1
    else:
        freq[ele] += 1
print(freq)