numbers: list = [];
for i in range (5):
    num: int = int (input("Enter a number"))
    numbers.append(num)
print(numbers)
print(f"The index position of the highest number is: {numbers.index(max(numbers))}")
