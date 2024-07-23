import statistics
numbers : list = [(num := int (input("Please enter a number"))) for i in range (2)];
print (f"The average of the numbers you entered is {statistics.mean (numbers)}");
