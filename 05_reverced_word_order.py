def reverse_words(s):
    words = s.split()      # split string into words
    reversed_words = words[::-1]  # reverse list
    return " ".join(reversed_words)

# Example
print(reverse_words("Hello World Python"))