string = input("Enter a string with num: ")

char = input("Enter a character to search for: ")

count = 0

for c in string:

    if c == char:

     count += 1

print(f"The character '{char}' appears {count} times in the string.")