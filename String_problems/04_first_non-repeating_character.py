def first_non_repeating(s):
    freq = {}

    # Step 1: Count frequency
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Step 2: Find first non-repeating
    for char in s:
        if freq[char] == 1:
            return char

    return None  # if no unique character

# Example
print(first_non_repeating("aabbcde"))