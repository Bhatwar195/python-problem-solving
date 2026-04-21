def is_anagram(s1, s2):
    # remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)

# Example
print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "world"))     # False