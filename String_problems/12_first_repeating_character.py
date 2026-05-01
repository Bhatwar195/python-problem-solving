def first_repeating(s):
    seen = set()

    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)

    return None  # if no repeating character

# Example
print(first_repeating("abcaed"))