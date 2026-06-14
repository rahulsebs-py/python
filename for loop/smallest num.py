numbers = list(int(input("Enter numbers: ")))

largest = numbers[0]

for i in numbers:
    if i < small:
        small = i

print("small =", small)