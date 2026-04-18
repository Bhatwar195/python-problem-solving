def char_frequency(s):
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

# Example
print(char_frequency("banana"))
print(char_frequency("Apple"))