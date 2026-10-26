char=input("Enter a character: ")
def unique_characters(s):
    unique_chars = ""
    for c in s:
        if c not in unique_chars:
            unique_chars += c
    return unique_chars

result = unique_characters(char)
print(f"Unique characters in {char}: {result}")