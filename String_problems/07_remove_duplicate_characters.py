def remove_duplicates(s):
    result = ""
    seen = set()

    for char in s:
        if char not in seen:
            result += char
            seen.add(char)

    return result

# Example
print(remove_duplicates("programming"))