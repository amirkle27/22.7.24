import statistics
numbers: list = []
num: int = int (input("Please enter a number [-99 to exit]"));
if num == -99:
    print (None)
else:
    while num != -99:
        numbers.append(num)
        num = int(input("Please enter a number [-99 to exit]"));
    (print (sum(numbers)))