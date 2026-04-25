def to_uppercase(s):
    result = ""

    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch

    return result

# Example
print(to_uppercase("hello world"))