num: int = int (input("Please enter a number. [Enter -99 to exit]"));
numbers: list = []
numbers.append(num)
while num > 0:
    num = int(input("Please enter a number. [Only positive numbers please!!]"));
    numbers.append(num)
if num == -99:
    numbers.remove(-99)
    print(f" your highest number was {None}");
    print(f"your lowest number was {None}");
elif num <= 0:
    numbers.remove(num)
    print(f"your highest number was {max(numbers)}");
    print (f"your lowest number was {min(numbers)}");

