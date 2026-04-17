def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    longest_sub = ""

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        if right - left + 1 > max_length:
            max_length = right - left + 1
            longest_sub = s[left:right+1]

    return longest_sub, max_length

# Example
result, length = longest_unique_substring("abcabcbb")
print("Substring:", result)
print("Length:", length)