text = input("Enter a string: ")
count = 0
for char in text:
    if char not in "aeiou":
        count += 1
print("Consonants:", count)