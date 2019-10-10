# Elizabeth Fuller
# 10/9/19
# while loops

i = 0
numbers = []
while i < 6:
    print(f"At yje top i is {i}")
    numbers.append(i)
    i = i + 1
    print(f"Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
