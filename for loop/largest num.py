numbers = list(int(input("Enter numbers: ")))

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("Largest =", largest)